from lib import categoria, entrada

# ───────────────────────── 07 ESTAMPADO DE AUTOR ─────────────────────────
c = categoria("07_estampa", "Estampado de autor", "modamod:sublimadora", 6,
              "La Sublimadora: fotos sobre prendas, máscaras con forma y hasta banners. Cuidado con lo que fotografiás.")

e = entrada(c, "sublimadora", "Fotos en tu ropa", "modamod:sublimadora", 0)
e.spot("modamod:sublimadora", "Sublimadora",
       "**Tu foto, tu remera, tu responsabilidad.**",
       "La Sublimadora imprime fotos del mod //Camerapture// sobre remeras, pantalones, medias, calientabrazos, polleras y capas.", receta=True)
e.txt(
    "**Paso a paso.**\n1. Elegí la prenda (o ponela en la Entrada: la categoría la sigue sola).\n2. Poné una foto en //Frente// o //Espalda//. Tocar un casillero elige esa cara.\n3. Ajustá //Escala//, //X//, //Y// y //Ángulo//.",
    "4. Fijá con la chincheta cada cara que quieras imprimir: solo se estampan las caras fijadas que tienen foto.\n5. Prenda en la Entrada y **Prensar**: la tapa baja y arranca. Cerrar la tapa a mano también arranca.",
    "**Escala.** A escala mínima la foto queda chica y centrada, tipo logo. A escala máxima cubre la prenda entera, recortada a la silueta: es el full print, para quienes no creen en los márgenes.",
    "**Escanear estampa.** Abre el explorador de archivos de tu compu (PNG, JPG, WebP, BMP o GIF), igual que //Cargar imagen// de la cámara, pero sin la cámara. La imagen se achica y se comprime con los mismos límites, se vuelve una foto de Camerapture firmada por vos y gasta una hoja del tanque de papel. Queda en //Frente// si está vacío; si no, en //Espalda//; si tampoco, en el almacén.",
    "**Qué se gasta.** Cada cara estampada gasta una dosis de cada color de tinta, y cada prensado, una hoja de papel. Las fotos nunca se gastan: quedan cargadas para reimprimir.",
    "**Simetría lateral.** En medias y calientabrazos, con //Simetría: Sí// el lado izquierdo lleva el espejo de la derecha: un logo corrido hacia afuera queda hacia afuera en las dos piernas. {{Ojo:}} un texto dentro de la foto se lee al revés en el lado espejado.",
)

e = entrada(c, "mascaras", "Máscaras y capas", "modamod:molde_mascara_circulo", 1)
e.spot('modamod:molde_mascara_circulo,modamod:molde_mascara_cuadrado,modamod:molde_mascara_estrella,modamod:molde_mascara_franja,modamod:molde_mascara_triangulo', 'Máscaras de sublimado', '**La foto, con forma.**', 'Cinco formas, un molde por cada una.', receta=True)
e.txt(
    "**La foto, con forma.** Con un molde de máscara en su casillero (columna derecha, abajo), la foto se estampa solo adentro de una forma: cuadrado, franja, círculo, estrella o triángulo. El molde no se gasta.",
    "**Editar: imagen / máscara.** Este botón decide qué mueven //Escala//, //X//, //Y// y //Ángulo//. En //imagen//, mueven la foto adentro de la máscara (escala 100 % = la foto cubre la máscara). En //máscara//, mueven la forma sobre la prenda. Cada cara tiene su propio ajuste.",
    "**La chincheta cambia de oficio.** Con máscara, ya no fija la cara entera: **agrega una capa** con esa foto, esa forma y esos ajustes. La foto queda en su casillero, así podés fijar otra capa con la misma foto, cambiar de forma o cambiar de foto.",
    "**Hasta 12 capas** entre frente y espalda. La lista //Capas (n/12)// las muestra en orden: “3F” es la capa 3 del frente y “5E” la 5 de la espalda. La de más arriba en la lista se pinta encima. Clic elige una capa, ▲▼ la mueven y ✕ la borra.",
    "{{Fe de erratas:}} los moldes de máscara, por ahora, solo se consiguen en la pestaña creativa.",
)

e = entrada(c, "banners", "Banners y escudos con foto", "minecraft:white_banner", 2)
e.txt(
    "**Para la gente que quiere flamear una foto.** Un banner puede llevar una foto de Camerapture, dibujada con dieciséis veces la resolución de vanilla. Un escudo hecho en la mesa de crafteo con ese banner hereda la foto.",
    "**Cómo.** En la Sublimadora, cargá el banner como si fuera una prenda y poné la foto en //Frente//: el banner no tiene espalda. Ajustás escala, posición y ángulo como siempre y la vista previa te muestra el banner terminado.",
    "Al romper el banner, la foto se conserva. En la Estación de Tintes el banner tiene su propia categoría, así que también se tiñe. Lo que no existe es estamparlo sobre una prenda: son dos cosas distintas con la misma máquina.",
)

# ───────────────────────── 08 DETALLES Y ACCESORIOS ─────────────────────────
c = categoria("08_detalles", "Detalles y accesorios", "modamod:estilista", 7,
              "La Estilista: apliques, correas, cadenas y acabados que brillan. Donde lo simple se vuelve sospechosamente elaborado.")

e = entrada(c, "estilista", "La Estilista", "modamod:estilista", 0)
e.spot("modamod:estilista", "Estilista",
       "**Los detalles son el 90 % del outfit.**",
       "La Estilista pega apliques 3D, correas y acabados sobre cualquier prenda. Trabaja con hilo y cuero, y recuerda lo que hiciste con cada tipo de prenda.", receta=True)
e.txt(
    "**El editor.** Poné la prenda en la **Entrada**: esa prenda es la muestra. A la izquierda tenés la vista 3D grande y tres pestañas (//Aplique//, //Correa// y //Acabado//); a la derecha, el panel de la máquina con entrada, salida y //Aplicar//. Editar es gratis: el costo real se paga al aplicar.",
    "**Último por prenda.** Cada tipo de prenda tiene un diseño //Último// que se guarda solo: es lo que se aplica cada vez. Al poner una prenda nueva sin diseño, la muestra arranca con el último de su tipo.",
    "**Diseños con nombre.** Hasta ocho por tipo de prenda. Escribís el nombre, apretás //Guardar con nombre// y queda en la lista. Clic en uno lo carga en el editor y pasa a ser el último. La ✕ lo borra.",
    "**Qué cuesta.** Los insumos se cargan en dos contadores, hilo y cuero, de hasta 64 unidades cada uno (soltando el ítem sobre el contador, con shift-clic, con la mano sobre el bloque o por tolva o cinta). Un hilo rinde cuatro apliques; un cuero, dos correas. Al aplicar, lo que la prenda ya traía vuelve a los contadores.",
    "**Entrada y salida.** La prenda entra por arriba o por la izquierda (cinta, tolva o la máquina de al lado) y sale por la derecha. Con la línea prendida, una prenda que llega con diseño arranca sola (13 segundos de pórtico); sin diseño, pasa de largo. Si falta algo, espera en la entrada hasta que lo repongas.",
)

e = entrada(c, "apliques", "Apliques", "modamod:molde_aplique_mono", 1)
e.txt(
    "**El aplique es el pequeño crimen del outfit.** Un modelo 3D que se pega sobre la tela, mira hacia afuera de la cara que tocaste y se mueve con vos. Cada uno nace de una plantilla (una por forma) y de un retazo de tres colores. Hasta doce por prenda.",
    "**Moños y compañía.** //Moño// (con dos cintas anchas de punta en V), //mariposa// (las alas baten solas), //flor// (pétalos, centro y hojas), //canguro// (el bolsillo del hoodie, en parche) y //corbata// (nudo y hoja que cuelga y se curva).",
    "**Botones y bolsillos.** //Botón//, //botonera// (cuatro botones en fila), //bolsillo parche//, //bolsillo con tapa// y //bolsillo trasero de jean//. **Tachas y parches:** //tacha//, //tira de tachas// y parches bordados de corazón, estrella y rayo. También hay //cordones//.",
    "**Retazos.** El color de cada aplique sale de un retazo de tres zonas. Se craftea con lana e hilo (da cuatro blancos) y se tiñe en la Estación de Tintes, en la categoría //Retazo de aplique//: poné el retazo en la entrada, elegí los cuadraditos 1, 2 y 3 y teñí. Las zonas sin fijar conservan el color.",
    "**Tela blanda.** Con //Blandura// mayor a cero, el aplique se mueve con la inercia de quien lo lleva: las colas del moño se curvan, las alas de la mariposa baten, los pétalos se inclinan y las hojas cuelgan. A cero, queda rígido. //Sacudir// alterna sacudones fuertes para ver cómo pendulea.",
    "**Giro, tamaño y fila.** Con un aplique elegido de la lista: //Giro// de a 15°, //Tamaño// de 50 a 250 %, //Quitar// (devuelve el retazo) y //Fila//, que repite el aplique hasta ocho veces hacia abajo con la separación que quieras.",
)

e = entrada(c, "correas", "Correas y cadenas", "modamod:molde_correa_cadena", 2)
e.spot('modamod:molde_correa_lisa,modamod:molde_correa_cadena,modamod:molde_correa_cadena_fina,modamod:molde_correa_ojalillos,modamod:molde_correa_cordon', 'Moldes de correa', '**Cinco estilos para lo que cuelga.**', receta=True)
e.txt(
    "**Para cuando un aplique no alcanza.** Una correa es una cinta o cadena que recorre una prenda entre dos puntos, o que cuelga de uno solo. Se hacen con un molde de correa en el casillero del molde, y se pagan en cuero. Hasta ocho por prenda.",
    "**Cuatro modos.**\n- **Pegada:** da la vuelta por la superficie entre dos puntos, como un arnés.\n- **Colgante:** el primer punto la sujeta y cuelga hacia el segundo con tela blanda.\n- **Anclada:** un solo clic; cuelga hacia abajo con el largo elegido y se balancea.\n- **Colgada:** dos clics y cuelga en curva con la gravedad.",
    "**Ancho y largo.** El ancho va de 1 a 4 px. El largo (solo en Anclada y Colgada) va de 2 a 32 px, de a 2. Con una correa elegida de la lista, //Modo//, //Ancho// y //Largo// cambian esa correa; //Recolorear// le pasa los colores del retazo y //Quitar// la saca.",
    "**Cinco estilos.** //Lisa// (cuero o tela con borde y puntadas), //cadena// (eslabones alternados), //cadena fina// (bolitas de metal), //ojalillos// (tira con agujeros) y //cordón// (con puntas de herraje: ideal para la capucha de un hoodie).",
)

e = entrada(c, "acabados", "Acabados con trims", "minecraft:netherite_upgrade_smithing_template", 3)
e.txt(
    "**Brillo, reflejos y movimiento. En una remera.** Un molde de trim de vanilla, puesto en el casillero del molde, le da a la prenda entera un acabado animado, con un efecto propio por patrón. El botón de acabado lo pone (y gasta el molde) o lo quita si la prenda ya lo lleva.",
    "**Los dieciocho efectos.** //Sentry// acero con barrido de luz; //Dune// arena que centellea; //Coast// espuma de olas; //Wild// venas de hoja; //Ward// latido de sculk; //Eye// ojos del End que parpadean; //Vex// niebla espectral; //Tide// cáusticas profundas; //Snout// magma; //Rib// brasas.",
    "//Spire// iridiscencia del End; //Wayfinder// haz de brújula que gira; //Shaper// líneas de cantera con pulso; //Silence// oscuridad con puntitos pálidos; //Raiser// calor que asciende; //Host// runas que se encienden de a una; //Flow// remolinos de viento; //Bolt// arcos de cobre. Los patrones de otros mods dan brillo metálico.",
    "**Material (opcional).** Un material de trim en su casillero (hierro, cobre, oro, netherita, cuarzo, redstone, lapislázuli, esmeralda, diamante o amatista) cambia los colores del efecto. Gasta una unidad. Sin material, cada patrón usa su paleta de fábrica. Con molde y sin material nuevo, el botón cambia solo el material.",
    "**Dónde funciona.** En cualquier prenda del mod, en el sombrero, en las bandas y en los borcegos. Todo se calcula a la resolución de la propia tela y se anima a diez cuadros por segundo. Cada efecto suelta además sus propias partículas alrededor de quien lo lleva, y también del Maniquí.",
    "**Texturas de tela.** Los moldes de textura (//fruncido// y //acolchado//) se ponen igual, en el casillero del molde: el botón //Textura// le da relieve a la prenda, o se lo saca. El molde no se gasta.",
)

# ───────────────────────── 09 PRODUCCIÓN EN SERIE ─────────────────────────
c = categoria("09_serie", "Producción en serie", "modamod:telar", 8,
              "Telar automático, cintas, empalmes y tubos: cómo hacer que la ropa se haga sola mientras vos hacés otra cosa.")

e = entrada(c, "telar", "Telar automático", "modamod:telar", 0)
e.spot("modamod:telar", "Telar automático",
       "**Una fábrica de prendas básicas, con lana e hilo.**",
       "Teje remera, pantalón, medias, calientabrazos, pollera, capa, delantal, borcegos, cinto y sombrero. Lisas, del color de la lana.", receta=True)
e.img("modamod:textures/gui/libro/telar_abierto.png", titulo="El telar abierto")
e.txt(
    "**Paso a paso.**\n1. Cargá **lana** (cualquiera de las 16) e **hilo** en sus dos casilleros: a mano, con shift-clic, con el ítem en la mano sobre el bloque, o por tolva o cinta desde cualquier lado menos la derecha.\n2. Tildá las prendas que querés: son casillas, podés elegir varias. Las teje de a una, en orden, y salta la que no alcance.",
    "3. Elegí el **lote**: la cantidad total de prendas (−10, −, +, +10; 0 es sin límite). Al terminar, la máquina se detiene; ↻ lo reinicia.\n4. La prenda sale por la **derecha** (a la cinta o a la próxima máquina) o la retirás con la mano vacía.",
    "**Lo que cuesta.** Lo mismo que su receta de crafteo: remera 7 lanas, pantalón 7, medias 2 lanas y 1 hilo, calientabrazos 2 y 1, pollera 6 y 3, capa 7 y 2, delantal 5, borcegos 2 hilos y 4 cueros, cinto 2 cueros, sombrero 2 lanas y 3 cueros.",
    "{{Fe de erratas:}} con la línea prendida, el telar arranca la prenda siguiente apenas termina, así que con stock casi no se puede abrir la pantalla. Apagá la línea (botón del frente) si necesitás meter mano.",
)

e = entrada(c, "cintas", "Cintas y empalmes", "modamod:cinta", 1)
e.spot("modamod:cinta,modamod:empalme", "Cintas y empalmes",
       "**Un camino de lana para tu lana.**",
       "La cinta lleva un ítem por bloque hacia adelante y lo entrega al inventario de enfrente: otra cinta, una máquina, un cofre o una tolva.", receta=True)
e.txt(
    "**Se arma sola.** Las curvas se forman como un riel: si por atrás no le llega nada y por un costado sí, la cinta se curva hacia ese lado. Las rampas aparecen cuando adelante, a la misma altura, no hay nada pero sí una cinta o máquina un nivel más arriba (rampa de subida) o más abajo (de bajada). No se curva y sube a la vez: primero rampa y después curva.",
    "**Cómo entra y sale.** Recibe por atrás, por los costados y por arriba (tolvas). Entra a una máquina por su cara izquierda y sale de la máquina por la derecha. Clic derecho con la mano vacía saca lo que lleva; con un ítem en la mano, lo pone si está libre. Lleva cualquier ítem, de a uno por bloque.",
    "**El empalme.** Junta hasta tres entradas (atrás y los dos costados) y una tolva por arriba, y las saca por una sola salida, el frente. Es rotativo: alterna entre las entradas que tienen algo esperando. También se frena con redstone.",
    "**Subite, no pasa nada.** La cinta lleva a quien se para encima, sin que camine: te deslizás con las piernas quietas, como sobre hielo. Con hielo compacto debajo, el empuje es doble; con hielo azul, triple (los ítems también viajan más rápido). Con la cinta parada por redstone, caminás normal.",
)

e = entrada(c, "tubos", "Tubos, extractor y válvula", "modamod:tubo", 2)
e.spot("modamod:tubo,modamod:extractor,modamod:valvula,modamod:empalme_tubo", "Tubos de transporte",
       "**Cañerías de cristal para ítems con rumbo.**",
       "Los tubos llevan ítems en vertical y en cualquier dirección, y se conectan solos con los tubos y empalmes vecinos.", receta=True)
e.txt(
    "**El tubo.** Un caño de vidrio liso, sin sentido propio: donde conecta, el vidrio sigue sin borde; en las puntas libres lleva una tapa de cobre. Con un vecino es tramo recto, con dos es recto o codo, con más es un nudo. Cada punta muestra qué hace: una //boca// (aro de cobre con agujero) larga o toma cosas de un contenedor; una //tapa cerrada// no da a nada.",
    "**Cerrar una cara.** Shift + clic derecho con la mano vacía sobre un brazo del tubo lo cierra con una tapa de cobre; otra vez, lo abre. Sirve para separar dos tramos que corren pegados.",
    "**Agua.** En los tramos verticales, el sentido lo manda el agua: con un balde de agua, el tubo (y toda la columna conectada) se llena de burbujitas y los ítems suben, más despacio; con un balde vacío se vacía y los ítems bajan. Es un estado del bloque, no agua real: no se derrama.",
    "**Empalme de tubo.** Un nudo de seis caras con un casillero de filtro por cara. Con un ítem en la mano apuntando a la cara, lo pone de filtro; con la mano vacía lo borra; con shift y mano vacía filtra por //tag//. Un ítem registrado sale por las caras cuyo filtro lo deja pasar; uno no registrado se reparte entre las caras sin filtro. Nunca sale por donde entró.",
    "**Extractor.** Se pega a la cara del contenedor que apuntás (agachado, al revés) y cada ocho ticks saca un ítem para pasarlo al de adelante: tubo, cinta, cofre o máquina. Saca de costado o hacia arriba, cosa que la tolva no hace. Tiene filtro (por ítem o por tag) y se pausa con redstone. De las máquinas del mod saca solo lo que ellas dejan sacar.",
    "**Válvula antirretorno.** Un tramo de tubo con sentido fijo, en forma de embudo: recibe solo por atrás y entrega solo por el pico, que apunta hacia donde mirás al ponerla (agachado, al revés). Un tubo nunca le manda nada por el pico.",
    "{{Fe de erratas:}} los tubos todavía no se pausan con redstone, y el hielo no los afecta: eso vale solo para las cintas.",
)

e = entrada(c, "linea", "Tu primera línea de producción", "modamod:cinta", 3)
e.txt(
    "**De lana a outfit sin tocar nada.** Un esquema posible, de izquierda a derecha, para armar con las cinco máquinas y unas cintas:",
    "**1. Telar.** Teje la prenda básica con lana e hilo que le llegan por tolva.\n**2. Modeladora.** Recibe la prenda por su cara izquierda y aplica el corte guardado. Necesita tijeras.\n**3. Tintes.** La pinta con el diseño fijado.\n**4. Sublimadora.** Le imprime la foto.\n**5. Estilista.** Le pega los detalles. La prenda sale por la derecha, a un cofre.",
    "**Reglas de la cadena.** Con la **línea prendida** en cada máquina, la prenda pasa directo a la siguiente. Una máquina que no tiene nada fijado para esa prenda (sin corte, sin cuadraditos, sin fotos, sin diseño) la saltea y la prenda sigue de largo. La Sublimadora, con fotos fijadas, espera a que cierre su tapa.",
    "{{Fe de erratas:}} la línea viene apagada de fábrica en cada máquina. Si tu cadena no avanza, revisá el botón de línea de cada una antes de culpar a la cinta.",
)
