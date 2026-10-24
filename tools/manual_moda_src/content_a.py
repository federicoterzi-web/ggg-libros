from lib import categoria, entrada

# ───────────────────────── 01 PORTADA ─────────────────────────
c = categoria("01_portada", "Portada", "modamod:remera", 0,
              "Qué es todo esto y cómo llegar de lana cruda a outfit en seis pasos. Empezá acá.")

e = entrada(c, "bienvenida", "Bienvenida", "modamod:remera", 0)
e.spot("modamod:remera,modamod:pantalon,modamod:pollera,modamod:capa,modamod:borcegos", "ModaMod",
       "**La ropa se viste sobre vos, no a tu lado.**",
       "Remeras, pantalones, polleras, capas, borcegos y hasta sombreros: todo se dibuja en capas sobre tu cuerpo, se superpone con criterio y se rehace cuantas veces quieras.",
       "Este manual es el camino de “lana cruda” a “eso lo hice yo”.")
e.txt(
    "**Cinco oficios, un solo ropero.**\n- **Corte:** la Mesa de Modelado decide largo, mangas, cuello y calce.\n- **Color:** la Estación de Tintes pinta por zonas y por capas.\n- **Estampa:** la Sublimadora imprime fotos.\n- **Detalle:** la Estilista pega apliques, correas y acabados.\n- **Producción:** el Telar, las cintas y los tubos lo hacen todo solos.",
    "**La regla de oro.** Las máquinas no se comen tus prendas ni tus moldes. La prenda sale modificada; los moldes se reusan para siempre. Lo que se gasta son los insumos: tinta, papel, hilo, cuero, tijeras. Traducción: equivocarse sale barato, y vas a equivocarte.",
    "**Cómo leer esto.** Si recién llegás, seguí el orden: //Portada//, //Tu cuerpo//, //Fondo de armario// y //El taller//; de ahí, a la máquina que te dé curiosidad. Si buscás una receta, andá al //Recetario//. Si algo salió mal, la //Chuleta// tiene los errores clásicos. Nadie te va a tomar examen.",
    "{{Fe de erratas:}} el manual sabe más de lo que el servidor te deja hacer. Algunas cosas existen solo en creativo o para operadores; las marcamos para que no las busques en vano.",
)

e = entrada(c, "primer_look", "Tu primer look", "modamod:remera", 1)
e.spot('modamod:remera,modamod:modelado,modamod:tinturas,modamod:sublimadora,modamod:estilista,modamod:guardarropas', 'El kit de arranque', '**Seis ítems, seis pasos.**', 'Una remera y cinco máquinas de las que vas a hablar bien.', receta=False)
e.txt(
    "**Seis pasos, sin drama.** Es el camino más corto de la lana al outfit. Cada paso tiene su capítulo; esto es la versión de ascensor.",
    "**1. Remera.** Ocho lanas en forma de remera (la grilla está en el Recetario). El color sale del promedio de las lanas que pongas: mezclá rojo con amarillo y tené fe.",
    "**2. Vestila.** Apretá **K** (o el botón //Ropa// del inventario) y poné la remera en su lugar. La primera vez te pide elegir cuerpo. Elegí con calma: es el único paso donde te pueden mirar.",
    "**3. Cortala.** Craftéate una Mesa de Modelado, moldes en blanco y unas tijeras. Con un molde de rango y uno de calce, la remera pasa a ser croptop, remerón o musculosa.",
    "**4. Teñila.** La Estación de Tintes pinta por zonas y por capas. La alimentan los tintes de siempre: cian, magenta, amarillo y negro.",
    "**5. Estampala.** Con una foto (hace falta Camerapture), la Sublimadora la plancha sobre la prenda. Sí, se puede poner la cara del amigo. No, no te vamos a frenar.",
    "**6. Guardala.** El Guardarropas guarda tu outfit con nombre y te lo pone entero cuando quieras.",
    "**Lo que lo cambia todo:** cada máquina devuelve la prenda modificada y conserva tus moldes. Podés probar diez cortes en la misma remera hasta que uno te convenza.",
    "{{Fe de erratas:}} la Modeladora no corta sin tijeras: gasta un uso por prenda. Llevá repuesto.",
)

# ───────────────────────── 02 TU CUERPO ─────────────────────────
c = categoria("02_cuerpo", "Tu cuerpo, tu base", "minecraft:player_head", 1,
              "Antes de la ropa, el maniquí sos vos. Cuerpos, colores, volumen y un poco de ciencia ficción.")

e = entrada(c, "elegir_cuerpo", "Elegir cuerpo", "minecraft:player_head", 0)
e.txt(
    "**Antes de la ropa, el maniquí sos vos.** ModaMod dibuja un cuerpo base debajo de la ropa, en lugar de tu skin pintada. Por eso la tela se pega al cuerpo y la piel asoma donde no hay prenda. La cabeza sigue siendo la tuya: acá nadie te reemplaza la cara.",
    "La primera vez que te ponés una prenda del mod se abre **Elegí tu cuerpo**. Si la cerrás con //Ahora no//, vuelve a aparecer la próxima vez que entres. Para reabrirla cuando quieras: **/modamod elegir**.",
    "**El catálogo.** //Mi propia skin// (lisa, con tu tono) y 19 cuerpos dibujados. Humanos: Estándar, Delgado, Atlético, Musculoso, Gordito, Velludo, Fem estándar, Fem atlética, Fem con curvas y Fem gordita. Animales: Cebra, Dálmata, Leopardo, Lobo, Osito, Panda, Tigre, Vaca y Zorro. Sí, hay un cuerpo de vaca. Sí, es una decisión de diseño.",
    "**Colores por zona.** //Base// (piel o pelaje), //Clara// (panza, hocico: solo animales), //Oscura// (rayas y manchas: solo animales) y //Rubor// (rodillas, codos, pecho y cara). Base sale de tu skin; las otras salen solas del color Base y las marca una “A”. El botón //Automática// las devuelve a ese estado.",
    "**De tu skin.** Una paleta con hasta cinco colores sacados de tu skin. Un clic y se lo asignás a la zona elegida: con una skin de osito, el marrón del pelaje va a Base y el beige de la pancita a Clara.",
    "**Ropa interior.** Dos partes que se eligen por separado, cada una con su color: arriba (Nada, Bralette, Deportivo, Binder) y abajo (Nada, Slip, Culotte, Boxer). Es el mínimo indispensable; lo lindo (encaje, estampas, fotos) se hace con prendas.",
    "**Skin siempre.** Con //Sí//, tu cuerpo elegido se ve aunque no lleves nada del mod. Con //No//, solo aparece debajo de la ropa del mod. **Confirmar** guarda todo y la pantalla no vuelve sola.",
)

e = entrada(c, "relieve", "Relieve, busto y volumen", "minecraft:player_head", 1)
e.txt(
    "**Ropa con volumen, y en serio.** El cuerpo y la ropa no son cajas planas: los costados de torso, brazos y piernas tienen relieve. Atlético y Musculoso marcan pectorales, abdominales y brazos; Gordito, Osito y Panda tienen panza; los femeninos suman cintura y nalgas; Lobo y Zorro, pecho de pelaje.",
    "**La ropa sigue al cuerpo según el calce.** Pegado lo copia como una segunda piel; Ajustado casi igual; Normal marca lo que sobresale; Suelto y Oversize apenas. Una prenda nunca queda por dentro de la de abajo.",
    "**Busto.** Dos estilos: //Redondo// (dos cúpulas) o //Cuadrado// (una caja por pecho, al estilo cúbico de Minecraft). Los cuerpos femeninos traen uno de fábrica. Tiene física: rebota al saltar, al caminar y al girar, y la ropa de encima rebota con él.",
    "**Estrógenos y Testosterona.** Dos pociones que se le compran al clérigo aprendiz, a 6 esmeraldas cada una (no tienen receta). Cada Estrógenos sube un talle, hasta siete tomas. Cada Testosterona baja uno. No vencen: te quedás con el talle hasta que decidas cambiarlo.",
    "**Volumen.** El cuerpo y la tela pueden ser //Redondeados// (suaves, de fábrica), //Voxel// (bloquecitos de medio píxel, estilo 3D Skin Layers) o //Voxel grueso// (bloques de 1 px). Se elige en la pantalla de cuerpo y lo ven los demás jugadores.",
)

# ───────────────────────── 03 FONDO DE ARMARIO ─────────────────────────
c = categoria("03_prendas", "Fondo de armario", "modamod:pantalon", 2,
              "Qué hay para ponerse, quién va debajo de quién y por qué tu capa y tu hoodie no se pelean.")

e = entrada(c, "ropero", "El ropero completo", "modamod:remera", 0)
e.spot("modamod:remera,modamod:pantalon,modamod:socks_solid,modamod:calientabrazos,modamod:pollera,modamod:capa,modamod:delantal,modamod:borcegos,modamod:sombrero_bruja,modamod:banda",
       "El ropero completo",
       "**Diez prendas y un orden de llegada.**",
       "Remera, pantalón, medias, calientabrazos, pollera, capa, delantal, borcegos, sombrero y cinto. Cada una tiene su lugar en la pantalla de Ropa.")
e.txt(
    "**Quién va debajo de quién.** Las prendas se dibujan en orden fijo: cuerpo, medias, calientabrazos, pantalón, remera, pollera y, por último, lo que lleves en el lugar de chaqueta. Donde una prenda no tiene tela (una media corta, una remera sin mangas) se ve lo de abajo. Una prenda de arriba nunca queda por dentro de otra.",
    "**Dónde se ponen.** Apretá **K** o el botón //Ropa// del inventario, junto al libro de recetas. Hay tres lugares por prenda (un croptop sobre un remerón, medias de red bajo unas cortas) y un solo ítem por lugar. Hasta 16 prendas idénticas (mismo corte, color, estampa y apliques) se apilan en el inventario.",
    "**Las teclas.** **K** abre la pantalla de Ropa. **H** sube y baja la capucha del hoodie y de la capa. **J** abre y cierra el frente de la chaqueta y del embozo. **R** hace girar la pollera. Se cambian en //Controles → ModaMod//.",
    "{{Fe de erratas:}} las Medias 3/4, las Medias de red y el Traje de Maid de versiones viejas ya no se craftean (las que existían siguen andando). Hoy las medias salen con el largo que quieras y la trama de red va en la Modeladora.",
)

e = entrada(c, "remera", "Remera, hoodie y saco", "modamod:remera", 1)
e.spot('modamod:remera', 'Remera', '**Ocho lanas, mil versiones.**', 'Hoodie, saco, campera y chaleco empiezan todos acá.', receta=True)
e.txt(
    "**Una remera con aspiraciones.** La remera es la única prenda de torso. Hoodie, saco, campera y chaleco no son ítems aparte: son rasgos que cualquier remera puede tener. No hay prendas nuevas; hay remeras que crecieron.",
    "**Cómo se llama.** Cada prenda se nombra por su rasgo más fuerte. Por el corte: **musculosa**, **remerón**, **croptop**. Por el cuello: **polera**, **camisa**. Con capucha: **hoodie**. Con solapas y sin capucha: **saco**. Con el frente abierto: **campera**. Sin mangas: **chaleco**. Manga larga lisa: **buzo**. El resto de los rasgos va al tooltip.",
    "**Dónde la llevás cambia dónde se dibuja.** En el lugar //Remera// va debajo de la pollera. En el lugar //Chaqueta// (el de arriba, junto al muñeco) va por encima de todo. Cualquier remera entra en los dos: así armás remera + saco sin comprar nada más.",
    "**Lo que se corta en la Modeladora.** Capucha (con o sin, en estilo //Cajas// o //Malla//; **H** la sube y la baja), frente (cerrado, abierto, cruzado o abierto hasta el pecho; **J** lo abre y lo cierra), solapas (en pico, redondas o chal) y ruedo y puños ajustados. Las solapas y la apertura siguen el borde real del escote: pegadas a la tela, no flotando por su cuenta.",
    "**El hoodie de fábrica no se craftea.** Se arma desde una remera en la Modeladora: capucha, ruedo y puños ajustados, calce Oversize. Es la comodidad hecha prenda y no hace falta explicarla.",
    "**Un traje completo** se arma con saco (frente abierto, sin capucha, remate recto y solapas), pantalón y remera de cuello camisa. La corbata es un aplique de la Estilista.",
    "{{Fe de erratas:}} los hoodies y los moldes de chaqueta de versiones anteriores no se migraron. Si te quedó alguno viejo, rehacelo desde una remera.",
)

e = entrada(c, "piernas_brazos", "Piernas y brazos", "modamod:pantalon", 2)
e.spot('modamod:pantalon,modamod:socks_solid,modamod:calientabrazos', 'Piernas y brazos', '**Tres prendas, cuatro extremidades y varias opiniones.**', 'Cada lado se corta por su cuenta.', receta=True)
e.txt(
    "**Por cada pierna y cada brazo, una decisión.** Pantalón, medias y calientabrazos se cortan por lado: el izquierdo y el derecho pueden ser distintos. Sí, se puede un pantalón con una botamanga larga y otra corta. Se llama asimetría y en la pasarela le dicen “propuesta”.",
    "**El nombre depende del largo.** Pantalón: shorts, bermudas, 3/4, 7/8 o pantalón (si las dos piernas no coinciden, queda el genérico). Medias con pie: soquetes, medias, medias 3/4 o bucaneras. Sin pie: calzas (cortas si no pasan la rodilla) o calientapiernas. Calientabrazos: guantes si llegan a la mano, guantes largos si pasan el antebrazo, brazalete si es una tira angosta.",
    "**Cómo se corta cada uno.** Pantalón y manga de remera tienen un solo corte por lado: dónde //termina//, medido desde la cintura o el hombro. Medias y calientabrazos tienen dos: el de arriba marca dónde //empieza// la tela y el de abajo dónde //termina//. Así salen desde zoquetes hasta medias al muslo, o un calientabrazos que solo cubre el antebrazo.",
    "**Para no marearte.** En los esquemas de las máquinas, el casillero de la izquierda del dibujo es el lado //derecho// del jugador: se lee de frente, como un espejo. Pasa en todas, así que memorizalo una vez y listo.",
)

e = entrada(c, "pollera_capa", "Pollera y capa", "modamod:pollera", 3)
e.spot("modamod:pollera,modamod:capa", "Pollera y capa",
       "**La pollera no es una caja con ganas: es tela.**",
       "Una malla propia que baja de la cintura y se mueve con vos: choca con tus piernas, se abre al caer, se achica al saltar y se balancea de costado.")
e.txt(
    "**Cinco formas.** //Campana// (lisa, la de siempre), //tableada// (pliegues en V), //tubo// (recta, casi sin vuelo), //globo// (ancha al medio y cerrada en el ruedo) y //circular// (círculo completo: la que más vuela). Siete largos, del ultramicro al tobillo.",
    "**Varias a la vez.** Podés llevar hasta tres polleras: se dibujan en el orden de los lugares y cada una sale un poquito más afuera que la de abajo. Los patrones se ven a resolución completa.",
    "**Twirl.** Apretá **R** con una pollera puesta: das una vuelta entera con los brazos abiertos, la pollera se abre casi horizontal y gira arrastrada. Los demás jugadores lo ven. Utilidad práctica: ninguna. Valor social: incalculable.",
    "**La capa.** Cuelga de los hombros y se mueve como tela: se levanta al correr, rebota con los saltos y se abre al agacharte. Siete largos (del capelet al tobillo), ruedo recto, redondeado o con cola (arrastra por el piso), capucha (**H**) y cuello alto. El forro se tiñe y se estampa aparte del exterior.",
    "**El embozo** es una esclavina que cubre los hombros, con su propio molde en la Modeladora y siete largos (de 2 px hasta el piso). Choca con las piernas y los brazos como la pollera y, desde los 12 px, hace de capa: el paño de atrás deja de dibujarse y los apliques y correas pasan al embozo. Con **J** se abre en el cuello y cae en diagonal por los hombros. Un segundo molde le pone borde, que se tiñe con la zona //Detalles//.",
    "**La capucha de la capa** puede ser de malla o de cajas, según su molde. Va abierta abajo, por fuera del paño o del embozo, y también lleva apliques.",
    "**Reglas de convivencia.** La capa del mod manda sobre la capa vanilla, incluidas las de Optifine y Minecon. Con élitros puestos pasa al revés: se ven los élitros y la capa se esconde. Con un hoodie, la capa cuelga por fuera y no dibuja su capucha ni su cuello alto.",
    "{{Fe de erratas:}} en la pollera, el patrón todavía puede mostrar un corte justo en el centro de la espalda, donde se juntan los extremos de la tela.",
)

e = entrada(c, "delantal", "Delantal", "modamod:delantal", 4)
e.spot('modamod:delantal', 'Delantal', '**Cinco lanas y a cocinar (o a fingir).**', receta=True)
e.txt(
    "**La prenda que dice “estoy cocinando” aunque no sea verdad.** Se craftea con cinco lanas (la grilla está en el Recetario) y va en su propio lugar de la pantalla de Ropa, por encima de la remera, la chaqueta y la pollera, del pecho hacia abajo.",
    "**En la Modeladora** tiene su propia pestaña con casilleros para la //forma// (recto, trapecio, peto, corazón o festón), //desde// y //hasta// (de dónde a dónde cubre), la //cobertura// (envolvente, solo el frente o angosto), los //tirantes// (rectos o cruzados), las //esquinas//, los //volados// (de los costados y de arriba) y el //ruedo//. El ruedo Redondeado redondea las esquinas de abajo.",
    "**Se tiñe en dos zonas,** //peto// y //falda//, en la Estación de Tintes.",
)

e = entrada(c, "calzado", "Borcegos y calzado", "modamod:borcegos", 5)
e.spot("modamod:borcegos", "Borcegos",
       "**Zapatos con carácter, y con cajas.**",
       "Un par de botas de cuero con caña, puntera, suela gruesa y cordones, armadas con cajas: se ven los dos pies. Van en un lugar de calzado propio, junto al cinto en la pantalla de Ropa.")
e.txt(
    "**Tres zonas de color.** //Cuero//, //Suela// y //Cordones//, cada una con su color y su dibujo. De fábrica: cuero marrón, suela casi negra, cordones crema. Se pintan en la Estación de Tintes o en la Estilista, y admiten apliques y correas.",
    "**Cada pie por su cuenta.** El izquierdo y el derecho tienen cada uno su caña, su suela y su botamanga (seis casilleros en la Modeladora, como las mangas). Con la simetría activa, un molde manda a los dos. En la Estilista, el botón //Espejar// repite en el otro pie lo que hagas en uno.",
    "**Los moldes del calzado** vienen en cinco familias: //caña// (baja, alta, bota, tenis, zapato, mocasín, bailarina, pantufla, taco o ninguna), //suela// (chata, plataforma, cuña, goma, taco chico, sandalia o chancla), //punta// (fina, ancha, redonda, cuadrada, alargada, de goma o descubierta), //cierre// (hebilla, velcro, tira en V, tobillera, gladiadora, costura lateral o ninguno) y //detalle// (lengüeta, parche, costura en el empeine).",
    "**La botamanga.** Un casillero define cómo se lleva el pantalón: por dentro de la caña (el pantalón se corta donde empieza la caña y se ven el cuero y los cordones) o por fuera (baja entero y se ensancha sobre la caña).",
)

e = entrada(c, "accesorios", "Sombreros y bandas", "modamod:sombrero_bruja", 6)
e.spot("modamod:sombrero_bruja,modamod:banda", "Sombreros y bandas",
       "**Lo que te ponés cuando ya te pusiste todo.**",
       "El sombrero tiene su lugar propio (aparte del casco, así que se lleva con casco, con capucha y con apliques). El cinto y el collar son la misma prenda, la //banda//, en dos lugares distintos.")
e.txt(
    "**Sombrero.** Tres zonas de color: ala, copa y cinta. Según los moldes que le pongas en la Modeladora sale gorra, boina, galera, sombrero vaquero o charro, tricornio, gorro de cocinero, gorro marinero, vincha, cofia o el clásico sombrero de bruja con la punta recta o doblada, que se mece con el movimiento.",
    "**Banda.** Un aro que rodea la cintura (el //cinto//) o el pecho (el //collar//). Cada zona solo entra en su lugar. Se arma con tres moldes: //ancho// (fino, medio, ancho), //zona// y //herraje// (ninguno, placa, aro o colgantes como campana, hueso, corazón y medalla).",
)

e = entrada(c, "mascaras_barbijo", "Máscaras y barbijo", "modamod:antifaz", 7)
e.spot("modamod:antifaz,modamod:media_mascara,modamod:mascara_completa,modamod:barbijo", "Máscaras y barbijo",
       "**Para esconder la cara con estilo.**",
       "Tres máscaras y un barbijo que se usan juntos o por separado.", receta=True)
e.txt(
    "**Cuatro prendas.** El //antifaz// (una franja sobre los ojos con puntitas a los costados), la //media máscara// (de la frente a la nariz), la //máscara completa// (toda la cara, con ojos y una ranura en la boca) y el //barbijo// (de la nariz al mentón, con pliegues, alambre en la nariz y elásticos a las orejas).",
    "**Dónde van.** Las tres máscaras comparten el lugar //Máscara// de la cabeza. El barbijo tiene su propio lugar, así que se puede llevar encima de una máscara.",
    "**Se hacen con lana e hilo.** Antifaz: hilo, lana, hilo en una fila. Media máscara: tres lanas sobre hilo, lana, hilo. Máscara completa: esa misma grilla con otra fila de tres lanas abajo. Barbijo: hilo, vacío, hilo sobre tres lanas. Las grillas están en el Recetario.",
    "**Salen blancas.** Se tiñen en la Estación de Tintes, en las categorías //Máscara// y //Barbijo//, con tres cuadraditos de prenda entera, y llevan una foto de la Sublimadora en el frente (sin espalda ni capas con máscara).",
)

e = entrada(c, "pantalla_ropa", "Pantalla de Ropa", "minecraft:iron_chestplate", 8)
e.txt(
    "**Un solo lugar para todo lo que te ponés.** Los lugares de ropa del mod ya no están en el inventario de siempre: se abren con el botón //Ropa// del inventario o con **K** (también en creativo, y vuelve a cerrar).",
    "**Qué muestra.** Tu personaje, los lugares de ropa del mod, la **armadura real** (la que da las estadísticas), la **armadura cosmética** (solo se ve; casco, pechera, pantalón y botas) y tu inventario. La pechera cosmética acepta élitros y el casco acepta calabazas y cabezas.",
    "**Dos interruptores por pieza.** //Cosm.// muestra el ítem cosmético en lugar de la armadura real; //Ocultar// no dibuja nada. Si //Cosm.// está prendido y el lugar cosmético está vacío, la pieza se ve oculta. Con los dos apagados, ves la armadura real, como siempre.",
    "Los demás jugadores ven lo mismo que vos, y todo se guarda con el personaje, también al morir. Las estadísticas siempre salen de la armadura real: estar a la moda no te hace más resistente. Todavía.",
)
