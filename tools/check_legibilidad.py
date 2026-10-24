#!/usr/bin/env python3
"""Chequea que el texto de los libros Patchouli sea legible.

Por cada libro mide el contraste WCAG de cada color de texto realmente usado
(text_color, header_color, link_color y los $(#hex) / $(0-f) inline) contra los
pixeles de la pagina en book_texture. Ademas avisa de macros $( ) sin cerrar.
El desborde de paginas se chequea aparte en check_desborde.py.

Uso: python tools/check_legibilidad.py [libro ...]   (exit 1 si hay FAIL)
"""
import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ROOT / "patchouli_books"
GUI = ROOT / "assets/ggg/textures/gui"

FAIL, WARN = 3.0, 4.5  # ratio WCAG: <3 ilegible, <4.5 justo
# Paginas del book_texture (272x180) donde Patchouli dibuja texto
PAGES = [(15, 18, 131, 170), (141, 18, 257, 170)]
# Patchouli: valores por defecto cuando el book.json no los define
DEFAULTS = {"text_color": "000000", "header_color": "333333", "link_color": "0000EE"}
# $(0)..$(f): colores de chat de Minecraft
MC = dict(zip("0123456789abcdef", [
    "000000", "0000AA", "00AA00", "00AAAA", "AA0000", "AA00AA", "FFAA00", "AAAAAA",
    "555555", "5555FF", "55FF55", "55FFFF", "FF5555", "FF55FF", "FFFF55", "FFFFFF"]))


def lum(rgb):
    c = np.asarray(rgb, dtype=float) / 255
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return c @ [0.2126, 0.7152, 0.0722]


def bg_luminances(texture):
    """Luminancia mediana del fondo de las dos paginas (el arte de los bordes no cuenta)."""
    im = np.asarray(Image.open(GUI / texture.split("/")[-1]).convert("RGB"))
    px = np.concatenate([im[y0:y1, x0:x1].reshape(-1, 3) for x0, y0, x1, y1 in PAGES])
    return float(np.median(lum(px)))


def contrast(hexcolor, bg):
    """Ratio WCAG del color contra la luminancia de fondo."""
    l = lum([int(hexcolor[i:i + 2], 16) for i in (0, 2, 4)])
    return (max(l, bg) + 0.05) / (min(l, bg) + 0.05)


def texts(node, key=""):
    """(clave, string) de todo 'text'/'title' dentro de una pagina."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from texts(v, k)
    elif isinstance(node, list):
        for v in node:
            yield from texts(v, key)
    elif isinstance(node, str) and key in ("text", "title"):
        yield key, node


def level(r):
    return "FAIL" if r < FAIL else "WARN" if r < WARN else "ok"


def check_book(book):
    out = []  # (nivel, mensaje)
    cfg = json.loads((BOOKS / book / "book.json").read_text(encoding="utf8"))
    bg = bg_luminances(cfg["book_texture"])

    for k, d in DEFAULTS.items():
        c = cfg.get(k, d).lstrip("#").upper()
        r = contrast(c, bg)
        out.append((level(r), f"book.json {k} #{c} contraste {r:.1f}"))

    inline = {}  # color -> [usos, primer lugar]
    for f in sorted((BOOKS / book).glob("*/**/*.json")):
        rel = f.relative_to(BOOKS / book).as_posix()
        for i, page in enumerate(json.loads(f.read_text(encoding="utf8")).get("pages", [])):
            where = f"{rel} p{i + 1}"
            for key, s in texts(page):
                if len(re.findall(r"\$\(", s)) != len(re.findall(r"\$\([^()]*\)", s)):
                    out.append(("FAIL", f"{where}: macro $( sin cerrar en '{key}'"))
                for m in re.findall(r"\$\((#[0-9A-Fa-f]{6}|[0-9a-fA-F])\)", s):
                    c = m[1:] if m[0] == "#" else MC[m.lower()]
                    inline.setdefault(c.upper(), [0, where])[0] += 1
    for c, (n, where) in sorted(inline.items()):
        r = contrast(c, bg)
        out.append((level(r), f"inline #{c} x{n} (ej. {where}) contraste {r:.1f}"))
    return out


def main():
    books = sys.argv[1:] or sorted(p.name for p in BOOKS.iterdir() if (p / "book.json").exists())
    fails = 0
    for b in books:
        res = check_book(b)
        nf = sum(lvl == "FAIL" for lvl, _ in res)
        print(f"== {b}: {nf} FAIL, {sum(lvl == 'WARN' for lvl, _ in res)} WARN")
        for lvl, msg in res:
            if lvl != "ok":
                print(f"  {lvl}: {msg}")
        fails += nf
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
