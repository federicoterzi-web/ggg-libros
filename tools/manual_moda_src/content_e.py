"""Galerias de spotlights e imagenes que se suman al final de entradas ya escritas."""
from lib import ENTRIES


def m(*ids):
    return ",".join("modamod:" + i for i in ids)


E = {e.id: e for e in ENTRIES}
IMG = "modamod:textures/gui/libro/"

# ── Imagenes que ya existen ──
E["bienvenida"].img(IMG + "look_ejemplo.png", titulo="Un look de ModaMod")
E["maquinas"].img(IMG + "modeladora_abierta.png", titulo="La Modeladora, por dentro")

# ── Capturas que faltan: aparecen solas cuando el PNG existe (ver CAPTURAS.md) ──
E["elegir_cuerpo"].foto("elegir_cuerpo", "Elegí tu cuerpo", "La pantalla Elegí tu cuerpo con la vista previa y la paleta de tu skin.")
E["pantalla_ropa"].foto("pantalla_ropa", "La pantalla de Ropa (K)", "La pantalla K completa: lugares de ropa, armadura real y cosmética.")
E["maquinas"].foto("taller_maquinas", "Las cinco hermanas", "Las cinco máquinas una al lado de la otra, para que se vean los cinco colores.")
E["tintes"].foto("tintes_gui", "La Estación de Tintes", "La Estación con una remera cargada, los cuadraditos y el panel de capas a la vista.")
E["sublimadora"].foto("sublimadora_gui", "La Sublimadora", "La Sublimadora con una foto en Frente y la vista previa.")
E["estilista"].foto("estilista_gui", "La Estilista", "La Estilista con la vista 3D, las tres pestañas y el panel de diseños.")
E["linea"].foto("linea_cintas", "Una línea de verdad", "Telar, Modeladora, Tintes, Sublimadora y Estilista unidos por cintas, vistos desde arriba.")
E["tubos"].foto("tubos_mundo", "Tubos en acción", "Un tramo de tubos con extractor, empalme y válvula.")

# ── Spotlights ──
E["relieve"].spot(m("estrogenos", "testosterona"), "Estrógenos y Testosterona",
                  "**Dos frasquitos, cero recetas.**", "Se le compran al clérigo aprendiz: 6 esmeraldas cada uno.")

E["ruedos"].spot(m("molde_volado_recto", "molde_volado_circular"), "Volados",
                 "**Fruncidos para pollera.**", "Recto: muchas ondas chicas. Circular: pocas y grandes.", receta=True)
E["ruedos"].spot(m("molde_pollera_tubo", "molde_pollera_globo", "molde_pollera_circular", "molde_pollera_tableada"), "Formas de pollera",
                 "**Cuatro moldes, más la campana de fábrica.**", receta=True)

E["tramas"].spot(m("molde_red_encaje", "molde_red_escocesa", "molde_red_fina", "molde_red_gruesa", "molde_red_hexagonal",
                   "molde_red_perforada", "molde_red_rayas"), "Redes", "**Agujeros con intención.**", receta=True)
E["tramas"].spot(m("molde_red_arnes_x", "molde_red_arnes_tirantes", "molde_red_arnes_bandas"), "Arneses",
                 "**Todo abierto, salvo las tiras.**", receta=True)
E["tramas"].spot(m("molde_material_denim", "molde_material_cuero", "molde_material_pana"), "Materiales",
                 "**Denim, cuero y pana.**", "Una prenda lleva trama o material, no los dos.", receta=True)

E["patrones"].spot(m("pattern_argyle", "pattern_tartan", "pattern_pata_de_gallo", "pattern_lenador", "pattern_vichy", "pattern_rayas"),
                   "Clásicos", "**Los que nunca pasan de moda.**", receta=True)
E["patrones"].spot(m("pattern_leopardo", "pattern_cebra", "pattern_tigre", "pattern_vaca", "pattern_jirafa", "pattern_serpiente", "pattern_dalmata"),
                   "Animales", "**Pelaje de temporada.**", receta=True)
E["patrones"].spot(m("pattern_corazones", "pattern_estrellas", "pattern_lunares", "pattern_zigzag", "pattern_ventana",
                     "pattern_camuflaje", "pattern_camuflaje_digital", "pattern_diplomaticas"),
                   "Motivos y más", "**Para el resto del carácter.**", receta=True)

E["tintes"].spot(m("tinte_mezcla"), "Muestra de color", "**El color, en frasco.**", "Es solo la receta: no trae tinta.")

E["apliques"].spot(m("molde_aplique_mono", "molde_aplique_mariposa", "molde_aplique_flor"), "Moños, mariposas y flores",
                   "**El clásico del taller.**", receta=True)
E["apliques"].spot(m("molde_aplique_canguro", "molde_aplique_bolsillo", "molde_aplique_bolsillo_tapa", "molde_aplique_bolsillo_jean"),
                   "Bolsillos", "**Para guardar poco y lucir mucho.**", receta=True)
E["apliques"].spot(m("molde_aplique_boton", "molde_aplique_botonera", "molde_aplique_cordones", "molde_aplique_corbata"),
                   "Botones, cordones y corbata", "**Los que cierran, atan y anudan.**", receta=True)
E["apliques"].spot(m("molde_aplique_tacha", "molde_aplique_tachas", "molde_aplique_parche_corazon", "molde_aplique_parche_estrella",
                     "molde_aplique_parche_rayo"), "Tachas y parches", "**Un poco de actitud.**", receta=True)
E["apliques"].spot(m("retazo_aplique"), "Retazo de aplique", "**El color de cada aplique.**",
                   "Tres zonas; se tiñe en la Estación de Tintes.", receta=True)

trims = ",".join(f"minecraft:{n}_armor_trim_smithing_template" for n in
                 ("sentry", "dune", "coast", "wild", "ward", "eye", "vex", "tide", "snout", "rib", "spire", "wayfinder",
                  "shaper", "silence", "raiser", "host", "flow", "bolt"))
E["acabados"].spot(trims, "Los dieciocho", "**Moldes de vanilla, efectos de ModaMod.**",
                   "Lo nuevo no es el molde: es lo que le hace a tu remera.")
E["acabados"].spot(m("molde_textura_fruncido", "molde_textura_acolchado"), "Texturas de tela", "**Relieve de regalo.**", receta=True)
