from lib import categoria, entrada

# ───────────────────────── 10 VIDRIERA ─────────────────────────
c = categoria("10_vidriera", "Vidriera", "modamod:guardarropas", 9,
              "Guardarropas, maletín y maniquí: guardar outfits, ponértelos al toque y exhibirlos como corresponde.")

e = entrada(c, "guardarropas", "Guardarropas", "modamod:guardarropas", 0)
e.spot("modamod:guardarropas", "Guardarropas",
       "**Tu outfit completo, con nombre y apellido.**",
       "Guarda lo que llevás puesto y te lo vuelve a poner entero cuando quieras. Es un mueble con puerta: se abre hacia afuera mientras alguien mira adentro.", receta=True)
e.img("modamod:textures/gui/libro/guardarropas_gui.png", titulo="El Guardarropas abierto")
e.txt(
    "**La pantalla.** A la izquierda, la misma pantalla de Ropa del jugador: los lugares de ropa del mod, la armadura real y la cosmética con sus interruptores, y tu inventario. A la derecha, la lista de outfits guardados. Hay lugar para doce.",
    "**Guardar.** Escribís un nombre (si lo dejás vacío se llama //Outfit N//) y apretás //Guardar//: todo lo que llevás puesto, ropa del mod, armadura y cosmética, se mueve al mueble y te quedás sin esas prendas. Si ya hay uno con ese nombre, se le suma un número (//Gala 2//).",
    "**Verlo antes de ponértelo.** Al tocar el nombre de un outfit, tu muñeco se ve con ese outfit puesto, de mentira: no te cambia nada.",
    "**Poner.** Te pone el outfit entero de una vez. Lo que llevabas puesto no se pierde: si era un outfit guardado, vuelve a la lista con su nombre, al final. Si era ropa suelta, queda guardado como //Anterior//, siempre el primero de la lista, con exactamente lo que tenías puesto. Tocarlo te lo devuelve. Si ya había un //Anterior// sin usar, pasa a //Anterior 2//.",
    "**Compartido.** Los outfits son de todos los que abren ese Guardarropas, y también de los Maletines vinculados a él. Con el candado cerrado, solo el dueño, los operadores y los jugadores en creativo pueden guardar, poner o desarmar; los demás pueden abrirlo y ver la lista.",
    "{{Fe de erratas:}} el mueble no te deja agarrar prendas sueltas: guarda y devuelve outfits enteros, y las tolvas ya no meten ni sacan nada.",
)

e = entrada(c, "maletin", "Maletín de outfits", "modamod:maletin", 1)
e.spot("modamod:maletin", "Maletín de outfits",
       "**Tu guardarropas, con asa.**",
       "Un maletín de cuero con cierres dorados para vestirte con los outfits de un Guardarropas desde cualquier lado.", receta=True)
e.txt(
    "**Vincular.** Shift + clic sobre un Guardarropas. Desde ahí, el maletín usa el mismo almacenamiento que el mueble: lo que guardás en uno aparece en el otro. Funciona aunque el mueble esté lejos o descargado, porque los outfits viven en el mundo, no dentro del bloque.",
    "**Usarlo.** Clic derecho abre una lista con solo los nombres de los outfits (sin muñeco, sin slots): tocás uno y te lo pone entero. Shift + clic derecho te pone el siguiente al instante, con humo, destellos y una campanita. Repetido, hace la ronda por todos.",
    "**Apoyarlo.** Clic derecho sobre un bloque lo deja parado, con la manija arriba, mirando hacia vos. Apoyado, el clic derecho abre la lista igual y Shift + clic derecho lo levanta. Al romperlo cae con todo: vínculo, colores, patrones y apliques.",
    "**Teñirlo y decorarlo.** Tiene tres zonas, como el sombrero: cuero, costuras y manija, y herrajes. En la Estación de Tintes (categoría //Maletín//) lleva colores y patrones por zona; en la Estilista, colores y apliques sobre cualquier cara.",
    "{{Fe de erratas:}} no sirve para guardar, combinar ni desarmar: eso se hace en el Guardarropas. El maletín tampoco tiene candado propio: si el mueble está cerrado, igual viste con sus outfits.",
)

e = entrada(c, "maniqui", "Maniquí", "modamod:maniqui", 2)
e.spot("modamod:maniqui", "Maniquí",
       "**Un outfit sin nadie adentro, pero con mucho carácter.**",
       "Exhibe un outfit completo en el mundo. La figura es de tamaño normal: con el plato mide casi dos bloques y medio, así que necesita lugar libre arriba.", receta=True)
e.img("modamod:textures/gui/libro/maniqui_gui.png", titulo="La pantalla del Maniquí")
e.txt(
    "**Qué lleva.** Tres lugares por categoría de prenda, la columna de armadura y lugares para sombrero, calzado, delantal, capa, cinto y collar. Todo se ve puesto en la figura.",
    "**Cómo se usa.** //Clic derecho con una prenda o armadura:// se la pone en el primer lugar libre de su categoría. //Mano vacía:// abre la pantalla. //Agachado con la mano vacía// (o el botón //Girar//): el plato gira, una vuelta cada 14 segundos. //Intercambiar conmigo:// la ropa del maniquí pasa a vos y la tuya a él, lugar por lugar. No se pierde nada.",
    "**Pose.** Parado, En jarra, Saludo, Brazos abiertos, Pasarela o Sentado. Los sliders de la derecha mueven cabeza, brazos y piernas por separado; al tocar uno, la pose pasa a //Libre//.",
    "**Figura.** //Maniquí// (liso, color madera), //tu skin//, las nueve skins de Mojang (Steve, Alex, Ari, Efe, Kai, Makena, Noor, Sunny y Zuri) o la **skin de otro jugador**: escribís el nombre y apretás //Ir//. El servidor la busca; tiene que existir.",
    "**Candado.** Quien coloca el Maniquí es el dueño. Cerrado, solo el dueño, los operadores y los jugadores en creativo pueden poner o sacar ropa, intercambiar, girar o romperlo; las tolvas no meten ni sacan y las explosiones no lo rompen. Los demás ven en la vista previa **su propio personaje con el outfit puesto**, para probárselo. Ideal para tiendas.",
    "**Armadura.** Se ve como en un jugador, con el teñido del cuero, los trims y el brillo del encantamiento. La calabaza, las cabezas y los bloques van en la cabeza. Los élitros todavía no se dibujan. Al romperlo, todo cae al piso.",
)

# ───────────────────────── 11 RECETARIO ─────────────────────────
c = categoria("11_recetario", "Recetario", "minecraft:crafting_table", 10,
              "Todas las grillas de crafteo, sin literatura. L = lana, H = hilo, C = cuero, T = tijeras, I = hierro, P = papel, R = redstone, M = tablones, V = vidrio.")

e = entrada(c, "leyenda", "Cómo leer las recetas", "minecraft:crafting_table", 0)
e.txt(
    "**La clave de las grillas.** L = lana de cualquier color, H = hilo, C = cuero, T = tijeras, I = lingote de hierro, P = papel, R = bloque de redstone, M = tablones, V = vidrio.",
    "Las prendas de lana toman el color del promedio de las lanas. Las medias y los calentadores de brazo salen de a tres. Las cintas, de a diez.",
    "**Dos cosas sin receta.** El hoodie no se craftea: se arma desde una remera en la Modeladora. Los Estrógenos y la Testosterona se le compran al clérigo aprendiz (6 esmeraldas cada una).",
    "{{Fe de erratas:}} las máquinas creativas, los kits y los moldes personalizados no tienen receta a propósito.",
)

e = entrada(c, "recetas_prendas", "Prendas", "modamod:remera", 1)
e.craft("modamod:remera", "modamod:pantalon").craft("modamod:pollera", "modamod:capa") \
 .craft("modamod:socks_solid", "modamod:calientabrazos").craft("modamod:delantal", "modamod:sombrero_bruja") \
 .craft("modamod:borcegos", "modamod:cinto")

e = entrada(c, "recetas_maquinas", "Máquinas", "modamod:modelado", 2)
e.craft("modamod:modelado", "modamod:tinturas").craft("modamod:sublimadora", "modamod:estilista") \
 .craft("modamod:telar", "modamod:guardarropas").craft("modamod:maniqui", "modamod:maletin")

e = entrada(c, "recetas_logistica", "Cintas y tubos", "modamod:cinta", 3)
e.craft("modamod:cinta", "modamod:empalme").craft("modamod:tubo", "modamod:empalme_tubo") \
 .craft("modamod:extractor", "modamod:valvula")

e = entrada(c, "recetas_papeleria", "Papelería", "modamod:molde_en_blanco", 4)
e.craft("modamod:molde_en_blanco", "modamod:patron_en_blanco").craft("modamod:mascara_en_blanco", "modamod:trama_en_blanco") \
 .craft("modamod:plantilla_en_blanco", "modamod:diseno_en_blanco").craft("modamod:retazo_aplique")

e = entrada(c, "recetas_tramas", "Tramas y materiales", "modamod:molde_red_encaje", 5)
e.craft("modamod:molde_material_cuero", "modamod:molde_material_denim").craft("modamod:molde_material_pana", "modamod:molde_red_arnes_bandas") \
 .craft("modamod:molde_red_arnes_tirantes", "modamod:molde_red_arnes_x").craft("modamod:molde_red_encaje", "modamod:molde_red_escocesa") \
 .craft("modamod:molde_red_fina", "modamod:molde_red_gruesa").craft("modamod:molde_red_hexagonal", "modamod:molde_red_perforada") \
 .craft("modamod:molde_red_rayas")

e = entrada(c, "recetas_patrones", "Patrones y motivos", "modamod:pattern_vichy", 6)
e.craft("modamod:pattern_argyle", "modamod:pattern_camuflaje").craft("modamod:pattern_camuflaje_digital", "modamod:pattern_cebra") \
 .craft("modamod:pattern_corazones", "modamod:pattern_dalmata").craft("modamod:pattern_diplomaticas", "modamod:pattern_estrellas") \
 .craft("modamod:pattern_jirafa", "modamod:pattern_lenador").craft("modamod:pattern_leopardo", "modamod:pattern_lunares") \
 .craft("modamod:pattern_pata_de_gallo", "modamod:pattern_rayas").craft("modamod:pattern_serpiente", "modamod:pattern_tartan") \
 .craft("modamod:pattern_tigre", "modamod:pattern_vaca").craft("modamod:pattern_ventana", "modamod:pattern_vichy") \
 .craft("modamod:pattern_zigzag")

e = entrada(c, "recetas_apliques", "Apliques y correas", "modamod:molde_aplique_mono", 7)
e.craft("modamod:molde_aplique_bolsillo", "modamod:molde_aplique_bolsillo_jean").craft("modamod:molde_aplique_bolsillo_tapa", "modamod:molde_aplique_boton") \
 .craft("modamod:molde_aplique_botonera", "modamod:molde_aplique_canguro").craft("modamod:molde_aplique_corbata", "modamod:molde_aplique_cordones") \
 .craft("modamod:molde_aplique_flor", "modamod:molde_aplique_mariposa").craft("modamod:molde_aplique_mono", "modamod:molde_aplique_parche_corazon") \
 .craft("modamod:molde_aplique_parche_estrella", "modamod:molde_aplique_parche_rayo").craft("modamod:molde_aplique_tacha", "modamod:molde_aplique_tachas") \
 .craft("modamod:molde_correa_cadena", "modamod:molde_correa_cadena_fina").craft("modamod:molde_correa_cordon", "modamod:molde_correa_lisa") \
 .craft("modamod:molde_correa_ojalillos")

# ───────────────────────── 12 CHULETA ─────────────────────────
c = categoria("12_chuleta", "Chuleta de bolsillo", "minecraft:command_block", 11,
              "Teclas, comandos, lo que solo existe en creativo y el catálogo de errores clásicos.")

e = entrada(c, "teclas", "Teclas y comandos", "minecraft:command_block", 0)
e.txt(
    "**Las tres teclas.** **K** abre la pantalla de Ropa. **H** sube y baja la capucha. **R** hace girar la pollera. Se cambian en //Controles → ModaMod//.",
    "**Para todos los jugadores:** **/modamod elegir** reabre la pantalla de elegir cuerpo. Es el único comando sin permisos especiales.",
    "**Para operadores (nivel 2, o en un mundo propio con trucos activados):**\n- **/modamod cuerpo <tipo>:** cambia el cuerpo directo.\n- **/modamod interior arriba|abajo|color:** ropa interior.\n- **/modamod tono skin|<número>:** tono de piel.\n- **/modamod busto <0..7>:** talle de busto (0 vuelve al del cuerpo).",
    "- **/modamod definicion <0..200>:** cuánto se marcan los músculos.\n- **/modamod volumen redondeado|voxel|grueso:** volumen del cuerpo y la tela.\n- **/modamod ver:** muestra tu configuración.\n- **/modamod reset:** todo vuelve al valor por defecto.\n- **/modamod moldes:** tus moldes personalizados, y los de otros jugadores.",
)

e = entrada(c, "errores", "Errores clásicos", "minecraft:barrier", 1)
e.txt(
    "**“No me deja Modelar.”** Revisá cuatro cosas: que haya prenda en la Entrada, que haya algo fijado, que tengas tijeras en la máquina y que la Salida esté libre. Casi siempre es la tercera.",
    "**“La máquina no abre.”** Está trabajando. Esperá a que termine o apagá la línea del frente y probá de nuevo. No metas la mano.",
    "**“La prenda se pasó de largo.”** Con la línea prendida, una máquina que no tiene nada fijado para esa prenda la saltea. No es un bug: es una cadena de montaje con carácter.",
    "**“Mi patrón no aparece en la Modeladora.”** Los patrones, los motivos y los colores viven en la Estación de Tintes. La Modeladora corta; Tintes pinta.",
    "**“Las fotos no se ven.”** La Sublimadora necesita Camerapture para tener fotos. Con el mod instalado, la foto sale de la cámara o del botón //Escanear estampa//.",
    "**“Las medias salen al revés.”** En todos los esquemas, la izquierda del dibujo es el lado derecho del jugador. Se lee como un espejo.",
)

e = entrada(c, "creativo", "Solo creativo y operadores", "minecraft:structure_block", 2)
e.txt(
    "**Cosas que existen pero no se consiguen jugando.** Las dejamos listadas para que no te vuelvas loco buscándolas.",
    "**Máquinas creativas.** Una versión creativa de cada máquina: no esperan, no piden insumos y vienen cargadas una vez con un ejemplar de cada molde o patrón. Se distinguen por la madera violeta nacarada y los herrajes dorados. Vienen también tres //kits// en cajas de shulker: todos los patrones, todos los moldes e insumos.",
    "**Apliques de objeto.** En la Estilista creativa, cualquier ítem o bloque de cualquier mod puede ser un aplique: calabazas talladas, cabezas, velas, una espada. Se ajustan con un panel lateral de colocación (cara de contacto, profundidad, rotación, escala) y de movimiento (pivote, velocidad, amplitud).",
    "**Moldes personalizados.** En la Estilista creativa, el botón //Crear molde// guarda un aplique con toda su configuración en un molde que se usa después en la Estilista normal. Los moldes se guardan a tu nombre, y **/modamod moldes** los lista (hasta 50 por jugador).",
)
