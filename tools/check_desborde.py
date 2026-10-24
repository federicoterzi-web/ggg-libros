#!/usr/bin/env python3
"""Chequea visualmente que el texto de los libros Patchouli entre en la pagina.

Replica el layout de Patchouli 1.21.1-93 (TextLayouter) con la fuente Unifont de
Minecraft ("uniform", la que usan los libros con use_blocky_font=false). Con
textOverflowMode=RESIZE (el default) el texto que no entra se ENCOGE, asi que el
chequeo es: escala final >= --min-scale. Cada pagina por debajo de 1.0 se dibuja
en PNG (fondo = book_texture, linea roja = fondo de pagina) en tools/_out/desborde/.

Uso: python tools/check_desborde.py [--min-scale 0.85] [--all] [libro ...]
Exit 1 si alguna pagina queda por debajo de --min-scale.
Aproximado: $(li) sin sangria, $(k:..)/$(playername) como texto fijo, y la
escala/wrap salen del bytecode, no de capturas: confirmar una pagina en el juego.
"""
import argparse
import json
import math
import os
import re
import sys
import zipfile

import numpy as np
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_legibilidad import BOOKS, GUI, MC, PAGES  # noqa: E402

MINECRAFT = Path(os.environ.get("MINECRAFT_DIR", Path.home() / "AppData/Roaming/.minecraft"))
VERSION = "1.21.1"
OUT = Path(__file__).resolve().parent / "_out/desborde"

PAGE_W, PAGE_H, LINE_H, Z = 116, 156, 9, 2  # Z = pixeles de lienzo por pixel de juego
PADX, PADY = 1, 6  # margen del lienzo, en pixeles de juego
# Donde empieza el texto segun el tipo de pagina (getTextHeight en Patchouli)
SPOTLIGHT_Y, ENTITY_Y = 40, 115

_hex = {}


def unifont():
    """codepoint -> (filas de 16 bits alineadas a la izquierda, left, right) como UnihexProvider."""
    if _hex:
        return _hex
    ver = json.loads((MINECRAFT / f"versions/{VERSION}/{VERSION}.json").read_text(encoding="utf8"))
    idx = json.loads((MINECRAFT / f"assets/indexes/{ver['assets']}.json").read_text(encoding="utf8"))
    h = idx["objects"]["minecraft/font/unifont.zip"]["hash"]
    z = zipfile.ZipFile(MINECRAFT / f"assets/objects/{h[:2]}/{h}")
    for line in z.read(next(n for n in z.namelist() if n.endswith(".hex"))).decode().splitlines():
        cp, data = line.split(":")
        n = len(data) // 16  # hex chars por fila: 2 (8px) o 4 (16px)
        rows = [int(data[i:i + n], 16) << (16 - 4 * n) for i in range(0, len(data), n)]
        ink = [r for r in rows if r]
        left = min(16 - r.bit_length() for r in ink) if ink else 0
        right = max(16 - (r & -r).bit_length() for r in ink) if ink else 0
        _hex[int(cp, 16)] = (rows, left, right)
    return _hex
    ver = json.loads((MINECRAFT / f"versions/{VERSION}/{VERSION}.json").read_text(encoding="utf8"))
    idx = json.loads((MINECRAFT / f"assets/indexes/{ver['assets']}.json").read_text(encoding="utf8"))
    h = idx["objects"]["minecraft/font/unifont.zip"]["hash"]
    z = zipfile.ZipFile(MINECRAFT / f"assets/objects/{h[:2]}/{h}")
    for line in z.read(next(n for n in z.namelist() if n.endswith(".hex"))).decode().splitlines():
        cp, data = line.split(":")
        n = len(data) // 16  # hex chars por fila: 2 (8px) o 4 (16px)
        rows = [int(data[i:i + n], 16) << (16 - 4 * n) for i in range(0, len(data), n)]
        rows = [r for r in rows if r]
        left = min(16 - r.bit_length() for r in rows) if rows else 0
        right = max(15 - (r & -r).bit_length() + 1 for r in rows) if rows else 0
        _hex[int(cp, 16)] = ([int(data[i:i + n], 16) << (16 - 4 * n) for i in range(0, len(data), n)], left, right)
    return _hex


def advance(ch, bold):
    if ch == " ":
        return 4 + bold
    rows, left, right = unifont().get(ord(ch), unifont()[ord("?")])
    return (right - left + 1) // 2 + 1 + bold


def parse(text, base_color, link_color):
    """Parrafos: lista de (lineBreaks que lo preceden, [(char, bold, color)])."""
    paras, cur, lead = [], [], 0
    bold, color = 0, base_color

    def cut(n):
        nonlocal cur, lead
        paras.append((lead, cur))
        cur, lead = [], n

    pos = 0
    for m in re.finditer(r"\$\(([^)]*)\)", text):
        cur += [(c, bold, color) for c in text[pos:m.start()]]
        pos = m.end()
        cmd = m.group(1)
        key = cmd.split(":")[0]
        if key == "br":
            cut(1)
        elif key in ("br2", "2br", "p"):
            cut(2)
        elif re.fullmatch(r"li\d?", key):
            cut(1)
            cur += [(c, bold, color) for c in "• "]
        elif key in ("l", "bold") and ":" not in cmd:
            bold = 1
        elif key == "l":
            color = link_color
        elif key == "/l":
            color = base_color
        elif key in ("", "reset", "clear", "nocolor"):
            bold, color = 0, base_color
        elif re.fullmatch(r"[0-9a-f]", key):
            color = MC[key]
        elif key.startswith("#"):
            color = key[1:]
        elif key == "playername":
            cur += [(c, bold, color) for c in "Player"]
        elif key == "k" and ":" in cmd:
            cur += [(c, bold, color) for c in "Key"]
        # o/m/n/italic/underline/strike/obf/t/c: no cambian el ancho
    cur += [(c, bold, color) for c in text[pos:]]
    cut(0)
    return paras


def tails(chars):
    """Trozos donde Java BreakIterator permite cortar (despues de espacios y guiones)."""
    s = "".join(c for c, _, _ in chars)
    for m in re.finditer(r"\S*?-(?=\S)|\S+\s*|\s+", s):
        yield chars[m.start():m.end()]


def layout(paras, page_y):
    """Devuelve (palabras [(x, y, char, bold, color)], escala, ancho_final) con modo RESIZE."""
    width = PAGE_W
    while True:
        words, y, overstep = [], page_y, math.inf
        for lead, chars in paras:
            y += lead * LINE_H
            x = 0
            for t in tails(chars):
                w = sum(advance(c, b) for c, b, _ in t)
                if x and x + w > width:
                    acc = x  # ancho de la linea hasta el primer caracter que no entra
                    for c, b, _ in t:
                        acc += advance(c, b)
                        if acc > width:
                            break
                    overstep = min(overstep, acc)
                    y, x = y + LINE_H, 0
                while x + w > width:  # palabra mas ancha que la linea entera: corta por letra
                    n = acc = 0
                    while n < len(t) and acc + advance(t[n][0], t[n][1]) <= width:
                        acc += advance(t[n][0], t[n][1])
                        n += 1
                    n = max(n, 1)
                    overstep = min(overstep, acc + advance(t[n - 1][0], t[n - 1][1]))
                    for c, b, col in t[:n]:
                        words.append((x, y, c, b, col))
                        x += advance(c, b)
                    t, y, x = t[n:], y + LINE_H, 0
                    w = sum(advance(c, b) for c, b, _ in t)
                for c, b, col in t:
                    words.append((x, y, c, b, col))
                    x += advance(c, b)
        overflow = (y + LINE_H - page_y) / (PAGE_H - page_y)
        if overflow * PAGE_W / width <= 1 or overstep == math.inf:
            return words, PAGE_W / width, width
        width = 1 + min(overstep, int(PAGE_W * overflow))


_MASC = {}


def _mascara(cp, rows):
    """Bitmap 16x16 (bool) de un glifo, cacheado."""
    if cp not in _MASC:
        _MASC[cp] = np.array([[bits >> (15 - cx) & 1 for cx in range(16)] for bits in rows], dtype=bool)
    return _MASC[cp]


def sobre_arte(layer, img):
    """Fraccion de pixeles de letra con contraste < 3 contra lo que hay detras (dibujos del libro, bordes)."""
    from check_legibilidad import lum
    la = np.asarray(layer)
    h, w = min(la.shape[0], img.height), min(la.shape[1], img.width)
    la = la[:h, :w]
    bg = np.asarray(img.convert("RGB"))[:h, :w]
    m = la[..., 3] > 128
    if not m.any():
        return 0.0
    lt, lb = lum(la[..., :3][m]), lum(bg[m])
    ratio = (np.maximum(lt, lb) + 0.05) / (np.minimum(lt, lb) + 0.05)
    return float((ratio < 3).mean())


def render(words, scale, width, page_y, book_tex, info, path=None):
    # el lienzo incluye PADX/PADY px de juego de margen: las lineas con y = -4 arrancan arriba del borde de la pagina
    bg = Image.open(GUI / book_tex.split("/")[-1]).convert("RGB").crop((15 - PADX, 18 - PADY, 15 + PAGE_W, 18 + PAGE_H))
    img = bg.resize(((PAGE_W + PADX) * Z, (PAGE_H + PADY) * Z), Image.NEAREST)
    ymax = max([w[1] for w in words] + [page_y]) + LINE_H
    arr = np.zeros(((ymax + PADY) * Z + 20, (width + PADX) * Z + 24, 4), dtype=np.uint8)
    font = unifont()
    for x, y, c, bold, col in words:
        rows, left, _ = font.get(ord(c), font[ord("?")])
        mask = _mascara(ord(c) if ord(c) in font else ord("?"), tuple(rows))
        rgba = [int(col[i:i + 2], 16) for i in (0, 2, 4)] + [255]
        for dx in ((0, Z) if bold else (0,)):
            x0, y0 = (x + PADX) * Z - left + dx, (y + PADY) * Z
            if x0 < 0 or y0 < 0:
                continue
            sub = arr[y0:y0 + 16, x0:x0 + 16]
            sub[mask[:sub.shape[0], :sub.shape[1]]] = rgba
    layer = Image.fromarray(arr, "RGBA")
    layer = layer.resize((max(1, round(layer.width * scale)), max(1, round(layer.height * scale))), Image.LANCZOS)
    arte = sobre_arte(layer, img)
    if path is None:
        return arte
    img.paste(layer, (0, 0), layer)
    d = ImageDraw.Draw(img)
    d.rectangle((PADX * Z, PADY * Z, (PADX + PAGE_W) * Z - 1, (PADY + page_y) * Z - 1), outline=(120, 120, 255)) if page_y > 0 else None
    d.line((PADX * Z, (PADY + PAGE_H) * Z - 1, (PADX + PAGE_W) * Z, (PADY + PAGE_H) * Z - 1), fill=(255, 0, 0))
    d.text((2, 2), info, fill=(255, 0, 0))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    return arte


def text_pages(book):
    """(entrada, nro de pagina, tipo, titulo, texto, y de inicio) de cada pagina con texto."""
    for f in sorted((BOOKS / book).glob("*/entries/**/*.json")):
        pages = json.loads(f.read_text(encoding="utf8")).get("pages", [])
        for i, p in enumerate(pages):
            if not p.get("text"):
                continue
            t = p["type"]
            if t == "patchouli:text":
                y = 22 if i == 0 else 12 if p.get("title") else -4
            elif t == "patchouli:spotlight":
                y = SPOTLIGHT_Y
            elif t == "patchouli:entity":
                y = ENTITY_Y
            else:
                continue
            yield f.stem, i + 1, p["text"], y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("books", nargs="*")
    ap.add_argument("--min-scale", type=float, default=0.85)
    ap.add_argument("--all", action="store_true", help="dibujar tambien las paginas que entran")
    ap.add_argument("--max-arte", type=float, default=0.03,
                    help="maximo de pixeles de letra con contraste <3 contra el fondo (texto sobre dibujos)")
    a = ap.parse_args()
    bad = 0
    for book in a.books or sorted(p.name for p in BOOKS.iterdir() if (p / "book.json").exists()):
        cfg = json.loads((BOOKS / book / "book.json").read_text(encoding="utf8"))
        base = cfg.get("text_color", "000000").lstrip("#")
        link = cfg.get("link_color", "0000EE").lstrip("#")
        n = low = 0
        for entry, num, text, y in text_pages(book):
            words, scale, width = layout(parse(text, base, link), y)
            n += 1
            info = f"{book}/{entry} p{num}  escala {scale:.0%}"
            dibujar = scale < 1 or a.all
            arte = render(words, scale, width, y, cfg["book_texture"], info,
                          OUT / book / f"{entry}_p{num}_{scale:.0%}.png" if dibujar else None)
            if scale < a.min_scale:
                low += 1
                print(f"  FAIL: {book}/{entry} p{num}: escala {scale:.0%} (< {a.min_scale:.0%})")
            if arte > a.max_arte:
                low += 1
                print(f"  FAIL: {book}/{entry} p{num}: {arte:.0%} de la letra sobre el dibujo/borde (> {a.max_arte:.0%})")
        print(f"== {book}: {n} paginas con texto, {low} con problemas")
        bad += low
    print(f"PNG en {OUT}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
