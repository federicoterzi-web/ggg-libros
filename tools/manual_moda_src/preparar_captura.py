#!/usr/bin/env python3
"""Convierte una captura al formato de imagen de Patchouli y la deja en el libro.

Patchouli dibuja las paginas `patchouli:image` tomando los primeros 200x200 px de una textura de
256x256 y mostrandolos a la mitad (100x100 en la pagina). Este script encaja la captura en esos
200x200 (sin deformar, centrada en vertical) y la guarda como RGBA transparente en
assets/modamod/textures/gui/libro/<nombre>.png.

Uso: python tools/manual_moda_src/preparar_captura.py captura.png nombre [--recorte x0,y0,x1,y1]
Despues: python tools/manual_moda_src/run.py  (las paginas de foto que faltaban aparecen solas).
"""
import argparse
from pathlib import Path

from PIL import Image

LIBRO = Path(__file__).resolve().parents[2] / "assets/modamod/textures/gui/libro"


def preparar(origen, nombre, recorte=None):
    im = Image.open(origen).convert("RGBA")
    if recorte:
        im = im.crop(recorte)
    im.thumbnail((200, 200), Image.LANCZOS)
    hoja = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    hoja.paste(im, (0, (200 - im.height) // 2))
    LIBRO.mkdir(parents=True, exist_ok=True)
    destino = LIBRO / f"{nombre}.png"
    hoja.save(destino)
    return destino


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("origen")
    ap.add_argument("nombre")
    ap.add_argument("--recorte", help="x0,y0,x1,y1 en pixeles de la captura original")
    a = ap.parse_args()
    print(preparar(a.origen, a.nombre, tuple(int(v) for v in a.recorte.split(",")) if a.recorte else None))
