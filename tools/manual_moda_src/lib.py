"""Mini DSL para escribir el Manual de Moda y paginarlo midiendo con el layout de Patchouli.

Uso: python tools/manual_moda_src/run.py  (regenera patchouli_books/manual_moda/en_us/{categories,entries}).
El texto vive en content_*.py; los JSON se generan, no se editan a mano.
"""
import json
import re
import shutil
import sys
from pathlib import Path

WT = Path(__file__).resolve().parents[2]  # raiz del repo
sys.path.insert(0, str(WT / "tools"))
import check_desborde as cd  # noqa: E402

BOOK = WT / "patchouli_books/manual_moda"
LANG = BOOK / "en_us"
BASE, LINK = "000000", "963e86"
MARGEN = 9  # una linea de colchon: el estimador de ancho no es exacto

PENDIENTES = []  # capturas que faltan: (nombre, entrada, que mostrar)
CATS = []     # dicts de categoria
ENTRIES = []  # dicts de entrada


def md(s):
    """Markup propio -> macros de Patchouli. **negrita**, //cursiva//, {{rojo}}, '- ' lista, linea en blanco = br2."""
    s = s.strip("\n")
    s = re.sub(r"\*\*(.+?)\*\*", r"$(l)\1$()", s, flags=re.S)
    s = re.sub(r"//(.+?)//", r"$(o)\1$()", s, flags=re.S)
    s = re.sub(r"\{\{(.+?)\}\}", r"$(4)\1$()", s, flags=re.S)
    s = re.sub(r"\n- ", "$(li)", s)
    s = re.sub(r"^- ", "$(li)", s)
    s = s.replace("\n\n", "$(br2)").replace("\n", "$(br)")
    return s


def entra(texto, y):
    paras = cd.parse(texto, BASE, LINK)
    _, escala, _ = cd.layout(paras, y + MARGEN)
    return escala >= 1.0


BR2 = "$(br2)"


def unir(piezas):
    """Piezas (texto, unión con la anterior). La unión de la primera pieza de una página se ignora."""
    return "".join((j if i else "") + t for i, (t, j) in enumerate(piezas))


def visible(t):
    return re.sub(r"\$\([^)]*\)", "", t)


ABREV = ("Cosm.", "etc.", "Ej.")


def cortes_de_oracion(t):
    """Posiciones donde se puede cortar entre oraciones sin romper numeraciones, abreviaturas ni dejar huerfanos."""
    cortes = []
    for m in re.finditer(r"\s+", t):
        previo = t[:m.start()]
        if not re.search(r"[.!?](?:\$\(\))?$", previo):
            continue
        ult = re.split(r"\s", previo)[-1]
        if re.fullmatch(r"(?:\$\([^)]*\))*\d+\.(?:\$\([^)]*\))*", ult) or ult.endswith(ABREV):
            continue
        if not re.match(r"[A-ZÁÉÍÓÚÑ¿¡“\"\d]|\$\(", t[m.end():m.end() + 6]):
            continue
        if len(visible(previo)) < 90 or len(visible(t[m.end():])) < 50:  # ni cabeza corta ni cola huerfana
            continue
        cortes.append(m)
    return cortes


def trozos(pieza):
    """Parte una pieza que no entra: en items de lista, en lineas, o en oraciones (en ese orden)."""
    t, j = pieza
    items = [x for x in re.split(r"(?=\$\(li\))", t) if x]
    if len(items) > 1:  # la cabeza va pegada al primer item: nunca queda un “...:” solo
        return [(items[0] + items[1], j)] + [(x, "") for x in items[2:]]
    lineas = t.split("$(br)")
    if len(lineas) > 1:
        out, i = [], 0
        while i < len(lineas):
            linea = lineas[i]
            while len(visible(linea)) <= 40 and i + 1 < len(lineas):  # titulito corto: pegado a la linea que sigue
                i += 1
                linea += "$(br)" + lineas[i]
            out.append((linea, j if not out else "$(br)"))
            i += 1
        if len(out) > 1:
            return out
    cortes = cortes_de_oracion(t)
    if not cortes:
        return None
    out, ini = [], 0
    for m in cortes:
        out.append((t[ini:m.start()], j if not out else " "))
        ini = m.end()
    out.append((t[ini:], " "))
    return out


def fluir(bloques, y_de_pagina):
    """Reparte bloques (ya en macros) en paginas; y_de_pagina(n) = y de inicio de la n-esima pagina nueva."""
    paginas, actual = [], []
    n = 0
    cola = [(b, BR2) for b in bloques]
    while cola:
        p = cola.pop(0)
        if entra(unir(actual + [p]), y_de_pagina(n)):
            actual.append(p)
            continue
        ts = trozos(p)
        if ts and entra(unir(actual + [ts[0]]), y_de_pagina(n)):
            cola = ts + cola
            continue
        if actual:
            paginas.append(unir(actual))
            actual, n = [], n + 1
            cola.insert(0, p)
            continue
        if not ts:
            raise ValueError(f"bloque demasiado largo y sin cortes: {p[0][:80]}")
        cola = ts + cola
    if actual:
        paginas.append(unir(actual))
    return paginas


class Entrada:
    def __init__(self, cat, id_, nombre, icono, orden):
        self.cat, self.id, self.nombre, self.icono, self.orden = cat, id_, nombre, icono, orden
        self.paginas = []
        self.pendiente = []  # sobrante de una spotlight: sigue con el proximo txt()

    def vaciar(self):
        if self.pendiente:
            for texto in fluir(self.pendiente, lambda n: -4):
                self.paginas.append({"type": "patchouli:text", "text": texto})
            self.pendiente = []

    def txt(self, *bloques, titulo=None):
        bloques = self.pendiente + [md(b) for b in bloques]
        self.pendiente = []
        primera = {"v": True}

        def y(n):
            i = len(self.paginas) + n
            if i == 0:
                return 22
            return 12 if (titulo and n == 0) else -4

        for n, texto in enumerate(fluir(bloques, y)):
            i = len(self.paginas)
            pag = {"type": "patchouli:text", "text": texto}
            if i == 0:
                pag["title"] = self.nombre
            elif titulo and n == 0:
                pag["title"] = titulo
            self.paginas.append(pag)
        return self

    def spot(self, items, titulo, *bloques, receta=False):
        self.vaciar()
        bloques = [md(b) for b in bloques]
        cabe, resto = [], list(bloques)
        # lo que entre debajo del item (y=40) va en la spotlight; el resto sigue en paginas de texto
        while resto and entra(BR2.join(cabe + [resto[0]]), 40):
            cabe.append(resto.pop(0))
        self.paginas.append({"type": "patchouli:spotlight", "item": items, "title": titulo,
                             "link_recipe": receta, "text": BR2.join(cabe)})
        self.pendiente = resto
        return self

    def img(self, *imagenes, titulo=None):
        self.vaciar()
        pag = {"type": "patchouli:image", "images": list(imagenes), "border": True}
        if titulo:
            pag["title"] = titulo
        self.paginas.append(pag)
        return self

    def foto(self, nombre, titulo, que_mostrar):
        """Pagina de imagen si ya esta la captura en assets/modamod/textures/gui/libro; si no, queda en CAPTURAS.md."""
        if (WT / f"assets/modamod/textures/gui/libro/{nombre}.png").exists():
            return self.img(f"modamod:textures/gui/libro/{nombre}.png", titulo=titulo)
        PENDIENTES.append((nombre, self.nombre, que_mostrar))
        return self

    def craft(self, r1, r2=None):
        self.vaciar()
        pag = {"type": "patchouli:crafting", "recipe": r1}
        if r2:
            pag["recipe2"] = r2
        self.paginas.append(pag)
        return self


def categoria(id_, nombre, icono, orden, descripcion):
    CATS.append({"id": id_, "name": nombre, "description": descripcion, "icon": icono, "sortnum": orden})
    return id_


def entrada(cat, id_, nombre, icono, orden):
    e = Entrada(cat, id_, nombre, icono, orden)
    ENTRIES.append(e)
    return e


def escribir():
    for d in ("categories", "entries"):
        shutil.rmtree(LANG / d, ignore_errors=True)
    (LANG / "categories").mkdir(parents=True)
    for c in CATS:
        out = {k: v for k, v in c.items() if k != "id"}
        (LANG / "categories" / f"{c['id']}.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    for e in ENTRIES:
        e.vaciar()
        d = LANG / "entries" / e.cat
        d.mkdir(parents=True, exist_ok=True)
        out = {"name": e.nombre, "icon": e.icono, "category": f"patchouli:{e.cat}",
               "sortnum": e.orden, "pages": e.paginas}
        (d / f"{e.id}.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    lineas = ["# Capturas que faltan para el Manual de Moda", "",
              "Cada una es una pagina de imagen que ya esta prevista en el libro: cuando dejes el PNG, aparece sola.", "",
              "1. Saca la captura en el juego (F2) o recortala de una captura grande.",
              "2. `python tools/manual_moda_src/preparar_captura.py captura.png <nombre> [--recorte x0,y0,x1,y1]`",
              "3. `python tools/manual_moda_src/run.py`", "",
              "| Nombre | Entrada | Que mostrar |", "|---|---|---|"]
    lineas += [f"| `{n}` | {e} | {q} |" for n, e, q in PENDIENTES]
    (Path(__file__).parent / "CAPTURAS.md").write_text(chr(10).join(lineas) + chr(10), encoding="utf8")
    print(f"{len(CATS)} categorias, {len(ENTRIES)} entradas, {sum(len(e.paginas) for e in ENTRIES)} paginas")
