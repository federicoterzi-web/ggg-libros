from lib import categoria, entrada

# ───────────────────────── 04 EL TALLER ─────────────────────────
c = categoria("04_taller", "El taller", "minecraft:loom", 3,
              "Las reglas de la casa: cómo piensa una máquina, qué se gasta y por qué no conviene meter la mano.")

e = entrada(c, "maquinas", "Cómo trabaja una máquina", "modamod:modelado", 0)
e.spot("modamod:modelado,modamod:tinturas,modamod:sublimadora,modamod:estilista,modamod:telar", "Las cinco hermanas",
       "**Cinco máquinas, un mismo carácter.**",
       "Mismo esqueleto en todas: una entrada grande, una salida grande, un botón de acción en el medio y un visor 3D con vos puesto.",
       "Cada una tiene su metal: Tintes verdín, Modeladora cobre, Sublimadora oro, Estilista lila y Telar granate.")
e.txt(
    "**Configurar, fijar, ejecutar.** Armás el ajuste y lo **fijás** (con la chincheta o un botón). Lo fijado es lo que se aplica; lo demás es borrador y solo vive en la vista previa. Poné la prenda en la **Entrada**, apretá el botón (//Modelar//, //Teñir//, //Prensar//, //Aplicar// o //Tejer//) y sale por la **Salida**.",
    "**Cuánto tardan.** Modelado 15 segundos, Tintes 10, Sublimadora 15, Estilista 13, Telar 12. Mientras trabajan se animan, suenan y se iluminan; al terminar, una campanita. Con redstone, se pausan.",
    "**Qué se gasta.** //Modeladora:// un uso de tijera por prenda. //Tintes:// tinta CMYK. //Sublimadora:// tinta y papel. //Estilista:// hilo (apliques) y cuero (correas). //Telar:// lana e hilo. Los moldes, los patrones y las fotos no se gastan nunca.",
    "**Diseños guardados.** Escribís un nombre y guardás todo lo fijado de esa prenda. Clic carga, clic derecho borra. Cada máquina tiene su propio cajón de diseños, así que el de la Modeladora no pisa al de Tintes.",
    "**Mientras trabajan, no se tocan.** La pantalla se cierra sola y no se puede abrir hasta que termina. Meter la mano en una máquina en marcha lastima: la Modeladora corta, la de Tintes marea con los vapores, la Sublimadora quema, la Estilista te pega con el pórtico y el Telar te engancha. Es un taller, no un spa.",
    "**Al romperlas, se guardan enteras.** Como una shulker: el ítem conserva todo lo de adentro (prendas, moldes, diseños, fotos, tinta y hasta el trabajo a medias) y lo devuelve al colocarla. Vale también para las explosiones.",
    "**Línea: sí / no.** Cada máquina tiene un botón de línea de producción, apagado de fábrica, en la pantalla y en el frente (un botoncito con un LED verde). Apagada, la máquina se usa sola: no empuja la prenda terminada a la siguiente ni saltea las que le llegan por cinta o tolva. Prendida, trabaja en cadena. {{Truco:}} apagarla es el freno para poder abrir la pantalla.",
)

e = entrada(c, "papeleria", "Moldes en blanco", "modamod:molde_en_blanco", 1)
e.spot('modamod:molde_en_blanco,modamod:patron_en_blanco,modamod:mascara_en_blanco,modamod:trama_en_blanco,modamod:plantilla_en_blanco,modamod:diseno_en_blanco', 'Los seis en blanco', '**El papel antes de ser molde.**', 'Cada receta rinde cuatro. Después de esto, todo molde es una variación.', receta=True)
e.txt(
    "**Todo molde nace en blanco.** Cinco papeles en blanco, y cada receta rinde cuatro:\n- **Molde:** papel y carbón alrededor de unas tijeras.\n- **Patrón:** hilo y tinta entre dos filas de papel.\n- **Máscara:** papel y tinta alrededor de unas tijeras.\n- **Trama:** hilo alrededor de un papel.\n- **Plantilla:** papel y cuero alrededor de unas tijeras.",
    "Se suma el //Diseño en blanco// (ocho papeles alrededor de un carbón) para guardar diseños de corte. Las grillas exactas están en el Recetario.",
    "**Del blanco al molde de corte.** Se combina el molde en blanco con tijeras y un ingrediente que decide cuál sale. **Rango:** de 1 a 7 hilos, del Más alto al Más bajo. **Calce:** lana (1 pegado, 2 ajustado, 4 suelto, 5 oversize; el normal es el blanco). **Ruedo:** cuero (1 ajustado, 2 campana, 3 ondulado, 4 festoneado, 5 pico, 6 redondeado, 7 con cola). **Volado:** plumas (1 recto, 2 circular).",
    "{{Fe de erratas:}} el resto de los moldes (cuellos, formas de pollera, calzado, delantal, correas, máscaras de sublimado) tiene su propia receta. Si no la encontrás acá, buscá su nombre en el libro de recetas del inventario.",
)

# ───────────────────────── 05 ALTA COSTURA ─────────────────────────
c = categoria("05_corte", "Alta costura", "modamod:modelado", 4,
              "La Mesa de Modelado: largos, calces, ruedos y tramas. Donde una remera deja de ser una remera.")

e = entrada(c, "modeladora", "La Mesa de Modelado", "modamod:modelado", 0)
e.spot("modamod:modelado", "Mesa de Modelado",
       "**El corte es destino.**",
       "La Modeladora cambia el corte de la prenda: largo, mangas, cuello, calce, ruedo y trama.", receta=True)
e.img("modamod:textures/gui/libro/modeladora_abierta.png", titulo="La Modeladora abierta")
e.txt(
    "**El visor y la tira de zonas.** A la izquierda, tu personaje con la prenda. Debajo, una tira de zonas (Cabeza y cuello, Torso, Brazos, Prenda entera...) con números y flechas. Al cambiar de zona, la cámara se acerca y a la derecha aparecen solo los casilleros de esa zona, cada uno con su nombre y su chincheta. Un puntito verde marca que ya hay algo fijado.",
    "**Paso a paso.**\n1. Elegí la prenda con el botón de arriba a la derecha del visor.\n2. Elegí una zona.\n3. Clic en la fila del casillero que querés cambiar: se abre la lista de moldes que acepta.\n4. Clic en un molde: queda puesto y fijado.",
    "5. Poné la prenda en la Entrada y apretá **Modelar**. Hace falta prenda, algo fijado, tijeras y la Salida libre. Un clic en la chincheta de un casillero fijado lo quita.",
    "**La bolsa de moldes.** Ya no hay almacenes con lugares contados: soltá tus moldes en el casillero //Bolsa de moldes// (o con shift-clic desde el inventario). Elegir un molde no lo gasta: el mismo sirve en todos los casilleros del mismo tipo. Clic derecho sobre uno de la lista saca uno a tu inventario.",
    "**Diseños de corte.** El botón ★ //Último// recarga los cortes de la última prenda de esa categoría. Para guardar el actual, escribí un nombre y apretá **+**: fabrica un ítem //Diseño de corte// (gasta un Diseño en blanco) que podés guardar en un cofre o regalar. Se cargan soltándolos en el casillero //Bolsa//.",
    "**La tijera.** Es el insumo de la Modeladora: tijeras de vanilla, y cada //Modelar// gasta un uso. La pantallita del frente muestra la tijera puesta y su durabilidad en una barra verde. Se cargan con la tijera en la mano sobre el bloque, con shift-clic o por tolva. Agachado y con la mano vacía, la recuperás.",
    "{{Fe de erratas:}} los patrones de color (rayas, corazones, estrellas, lunares...) no van acá: viven en la Estación de Tintes.",
)

e = entrada(c, "rango", "Rango: la regla de siete", "modamod:molde_rango_cero", 1)
e.spot('modamod:molde_rango_cero,modamod:molde_rango_minimo,modamod:molde_rango_corto,modamod:molde_rango_medio,modamod:molde_rango_mediolargo,modamod:molde_rango_largo,modamod:molde_rango_maximo', 'Los siete rangos', '**Siete marcas para medirlo todo.**', 'De la línea más alta a la más baja.', receta=True)
e.txt(
    "**Una regla, siete marcas.** El molde de rango mide una línea desde arriba hacia abajo, en siete niveles: el nivel //k// está a //2k// filas desde el hombro o la cintura. Se llaman Más alto, Muy alto, Alto, Medio, Bajo, Muy bajo y Más bajo. Sirve para todo: mangas, piernas, largo de remera, tiro, largo de pollera, largo de capa y largo de embozo.",
    "Cada prenda traduce el mismo nivel a su propia medida. El nivel 3, por ejemplo, es una manga media, una pantorrilla o una pollera a la rodilla. Y el nivel 0 es la línea más alta: manga sin nada, pierna sin nada, top.",
    "**Largo de remera,** del Más alto al Más bajo: top, crop, corto, normal, cadera alta, cadera y largo. **Tiro del pantalón:** hombros, pecho, bajo el pecho, muy alto, alto, medio y cadera (el último, sin banda).",
    "**Pollera,** px desde la cintura: ultramicro 3, micro 5, mini 7, a la rodilla 9, midi 11, larga 13 y hasta el tobillo 15. **Capa,** px desde los hombros: capelet 6, a la cintura 9, a la cadera 12, clásica 16, a la rodilla 18, larga 21 y hasta el tobillo 24. **Embozo,** px desde los hombros: 2, 5, 8, 12, 16, 20 y hasta el piso.",
    "**Cómo se lee cada corte.** Un solo pin en pantalón y manga de remera: dónde termina. Dos pines en medias y calientabrazos: arriba dice dónde //empieza// la tela y abajo dónde //termina//. Sin pin de arriba, la tela arranca arriba de todo.",
)

e = entrada(c, "calce", "Calce, cuellos y cajones", "modamod:molde_calce_oversize", 2)
e.spot('modamod:molde_calce_pegado,modamod:molde_calce_ajustado,modamod:molde_calce_suelto,modamod:molde_calce_oversize', 'Calces', '**Cuatro moldes, y el quinto es el blanco.**', 'El Normal no se fabrica: es el molde en blanco.', receta=True)
e.txt(
    "**El calce es lo que separa una remera de una carpa.** Cinco niveles:\n- **Pegado:** reemplaza la piel; la tela va justo donde estaba la skin.\n- **Ajustado:** aprieta, medio píxel menos; se nota el escalón donde corta.\n- **Normal:** un cuarto de píxel de aire.",
    "- **Suelto:** más holgado; se abre hacia el ruedo y cuelga un píxel por debajo del corte.\n- **Oversize:** el doble de abierto hacia el ruedo y cuelga dos píxeles.\nEl calce Normal es el molde en blanco: no hace falta fabricarlo.",
    "**Cajones.** Los casilleros que tienen un par llevan un botón ▾: manga con puño, cuello con solapa y, en pantalón, medias y calientabrazos, corte con ruedo. Al abrirlo aparece el segundo casillero, y los dos aceptan cualquiera de los dos moldes. El cajón se abre solo si ya hay un molde puesto.",
)

e = entrada(c, "ruedos", "Ruedos, volados y formas", "modamod:molde_pollera_tubo", 3)
e.spot('modamod:molde_ruedo_ajustado,modamod:molde_ruedo_campana,modamod:molde_ruedo_ondulado,modamod:molde_ruedo_festoneado,modamod:molde_ruedo_pico,modamod:molde_ruedo_redondeado,modamod:molde_ruedo_cola,modamod:molde_ruedo_fruncido', 'Ruedos', '**Cómo termina cada borde.**', 'Cada casillero acepta solo los que le corresponden.', receta=True)
e.txt(
    "**El ruedo es el remate de todo borde libre:** torso, puños, botamangas, bordes de medias y calientabrazos, pollera, capa y delantal. Una sola familia de moldes decide cómo termina cada uno.",
    "**Ajustado:** elástico; la última fila aprieta, la tela no cuelga y se pinta un rib. **En campana:** las últimas filas se abren hacia afuera. **Ondulado, festoneado y con pico:** bordes decorativos, solo en la pollera. **Redondeado:** las esquinas de abajo de la capa y del delantal. **Con cola:** la cola de la capa, diez píxeles más que arrastran por el piso.",
    "**Fruncido:** en medias y calientabrazos, la tela se arma como una malla con pliegues redondeados en las ocho filas cerca del borde. No funciona en torso, puños, botamangas ni pollera.",
    "**Volados.** Dos moldes, //recto// (tira fruncida con muchas ondas chicas y poca apertura) y //circular// (ruedo abierto con pocas ondas grandes). Valen en cualquier casillero de ruedo y en //Toda la pollera//, que pone tres filas parejas de arriba a abajo. Si ponés los dos, el del ruedo manda en la última fila.",
)

e = entrada(c, "tramas", "Tramas y materiales", "modamod:molde_red_encaje", 4)
e.img("modamod:textures/gui/libro/redes.png", titulo="Redes")
e.img("modamod:textures/gui/libro/arneses.png", titulo="Arneses")
e.txt(
    "**Perforar la tela, con estilo.** El molde de red agujerea la tela ya teñida: deja ver la piel por los huecos y refuerza solo los bordes (cuello, puños, dobladillo y el borde del largo elegido) para que la prenda no parezca deshilachada.",
    "- **Red fina:** malla diagonal chica y apretada.\n- **Red gruesa:** malla diagonal grande, bien abierta.\n- **Red hexagonal:** panal de abejas.\n- **Red perforada:** tela sólida con agujeritos redondos, tipo broderie.\n- **Encaje:** rombos grandes con un punto al centro.",
    "- **Rayas caladas:** franjas horizontales abiertas, con puentes alternados.\n- **Escocesa:** cuadrícula recta.\n- **Textura lisa:** quita la red que tuviera la prenda.",
    "**Arneses.** Son lo contrario de una red: todo queda abierto salvo las tiras. Cruzado (tiras en X con un anillo en el cruce), de tirantes (dos tirantes verticales y una banda al medio) y de bandas (bandas horizontales con anillo). Siguen los bordes de corte reales: si acortás la remera a crop, el arnés se acomoda solo. Los anillos son plateados y no se tiñen.",
    "**Materiales.** Tres moldes que dan tela en vez de agujeros: //denim// (sarga diagonal con desgaste a manchones), //cuero// (grano de poros con grietas y un brillo pintado) y //pana// (canaletas verticales, tipo corderoy).",
    "{{Fe de erratas:}} una prenda lleva una trama o un material, no los dos: hay un solo casillero. Elegí con orgullo.",
)

# ───────────────────────── 06 PALETA DE TEMPORADA ─────────────────────────
c = categoria("06_color", "Paleta de temporada", "modamod:tinturas", 5,
              "La Estación de Tintes: tinta CMYK, capas, patrones y tres recetas de color para presumir.")

e = entrada(c, "tintes", "Tinta y color", "modamod:tinturas", 0)
e.spot("modamod:tinturas", "Estación de Tintes",
       "**Cuatro colores y una transparencia.**",
       "La Estación de Tintes trabaja con tinta CMYK: cian, magenta, amarillo y negro, cargados con los tintes de siempre. Clic derecho con el tinte en la mano, o por tolva desde atrás.", receta=True)
e.txt(
    "**Los tanques.** Cada uno guarda hasta 64 dosis. Un teñido gasta una dosis de cada canal que use alguno de los colores fijados. El nivel se ve dentro de cada slider: el fondo se llena con el color de la tinta y a la derecha dice //n/64// (en rojo si está vacío).",
    "**Un color son cinco sliders:** Cyan, Magenta, Yellow, Key (negro) y Transparencia, de 0 a 100 % en pasos de 5.",
    "**Transparencia.** No gasta tinta. Al 100 % hace un agujero en la tela; en el medio, la tela queda translúcida de verdad, como un tul. Va por color: podés calar solo los corazones de un patrón. Las muestras con transparencia se ven sobre fondo a cuadros.",
    "**Muestras de color.** //Envasar// gasta un frasco de vidrio y te da una Muestra de color con la mezcla que estás editando; el tooltip dice el código y los porcentajes. //Usar muestra// copia esa mezcla al color que estás editando. La muestra es solo la receta: no trae tinta ni se gasta. Es el único regalo que no se rompe.",
)

e = entrada(c, "capas", "Cuadraditos y capas", "modamod:tinturas", 1)
e.txt(
    "**Cada cuadradito es una capa.** El dibujo de la prenda tiene un cuadradito por zona, y cada uno es una capa de color con su propia configuración. En la remera: dos de prenda entera, pecho, cuello (solo el borde del escote), manga izquierda, manga derecha, borde de abajo y solapas.",
    "En pantalón: cintura y una botamanga por lado. En medias y calientabrazos: arriba y abajo de cada lado. En la pollera, tres de fila fija. En la capa: exterior, forro, capucha y cuello. En el delantal: peto y falda. El sombrero (ala, copa y cinta), la banda (banda, borde y herraje), el calzado (cuero, suela y cordones, por pie), el maletín tiene las suyas. Las máscaras y el barbijo tienen tres cuadraditos de prenda entera, y el banner tres cuadraditos apilados (un liso de fondo y patrones encima).",
    "**Paso a paso.**\n1. Elegí la prenda con //Categoría//.\n2. Clic en un cuadradito: queda con marco dorado.\n3. Para un patrón, poné un molde de patrón en el cuadradito; sin molde, es un color liso.\n4. Armá el color con los sliders.",
    "5. Apretá la chincheta para fijarlo. Con molde, el molde vuelve al almacén; si ya estaba fijado y no tiene molde, se desfija.\n6. Prenda en la Entrada y **Teñir**.",
    "**Mirar antes de teñir.** La vista previa muestra lo fijado más el cuadradito que estás editando; si ese no está fijado, la línea //Editando// dice //sin fijar// y no va a salir en la prenda. Con el mouse sobre un cuadradito, la vista apaga todo lo que no es su zona.",
    "**Panel de capas.** Abajo a la derecha, la lista de capas: la de arriba tapa a las de abajo. Cada fila tiene un //ojo// (oculta la capa sin borrarla: no se aplica ni gasta tinta), la muestra de colores, el nombre y las flechas ▲▼ para reordenar.",
)

e = entrada(c, "controles", "Controles finos", "modamod:tinturas", 2)
e.txt(
    "**Todo cuadradito tiene opiniones.**\n- **Mezcla:** Normal (tapa lo de abajo), Multiplicar (oscurece: ideal para un patrón sobre otros colores) o Superponer (contraste).\n- **Opacidad:** de 10 a 100 %.\n- **Capa n/N ▲▼:** el orden de pintado.\n- **Tamaño:** de extra chico a extra grande.",
    "- **Ángulo:** gira las rayas de a 15°. En motivos gira toda la grilla, como girar la tela.\n- **Giro:** solo motivos; gira cada motivo en su lugar.\n- **↔ y ↕:** distancia horizontal y vertical entre motivos, de 50 % (pegados) a 300 %.\n- **Espejo:** da vuelta cada motivo, ↔, ↕ o los dos.",
    "- **Alternar:** de por medio, el motivo sale espejado, por filas, columnas o damero. Con //Giro// arma un zigzag tipo tejido.\n- **Simetría:** en el torso, la mitad izquierda es el reflejo de la derecha: las rayas en diagonal quedan en V.\n- **Posición:** corre el patrón.",
    "- **Forma:** rayas (Alternado, Arriba, Abajo, Medio, Tres rayas) o repetición de motivos (Grilla, Ladrillo, Disperso, Único).\n- **Azar:** nueva tirada al azar.\n- **Invertir:** pinta el negativo del patrón.\n- **Fondo:** con patrón, el último color activo pinta liso toda la zona de abajo y el patrón usa los otros. Sirve donde hay un solo cuadradito por zona (capa, sombrero, cinto, maletín, calzado, máscaras).",
    "**Varios colores en una capa.** Sobre la muestra grande hay tres muestras de color: clic en una elige cuál editan los sliders. //Colores 1/2/3// dice cuántos usa la capa. //Contorno// dibuja una línea alrededor de cada motivo con el último color activo (hacen falta al menos dos).",
    "**Variación.** //Fijo:// todo el relleno del Color 1. //Alternar:// cada motivo, raya o cuadro toma el color siguiente. //Aleatorio:// cada uno toma un color al azar (//Azar// vuelve a sortear). //Degradé:// pasa de un color al otro de arriba abajo, también en capas lisas.",
)

e = entrada(c, "patrones", "Patrones y motivos", "modamod:pattern_vichy", 3)
e.img("modamod:textures/gui/libro/motivos.png", titulo="Corazones, de cuatro formas")
e.txt(
    "**Los moldes de patrón son la despensa.** Los rayados (rayas superiores, alternadas, tres rayas), los motivos repetidos (corazones, estrellas, lunares) y el vichy, que hace cuadros de tres tonos con un solo color.",
    "**Animales y clásicos.** Leopardo, cebra, tigre, vaca, jirafa, serpiente y dálmata; tartán, leñador, pata de gallo, argyle, camuflaje, camuflaje digital, zigzag y ventana. Las recetas están en el Recetario. Solo se usan en la Estación de Tintes.",
    "**Repetición de motivos.** //Grilla// (filas parejas), //Ladrillo// (cada fila corrida media posición), //Disperso// (al azar, con huecos) y //Único// (un motivo grande en el frente de cada pieza, tipo logo). Los motivos se reparten para entrar justo alrededor de la pieza: el que cae en la costura sigue del otro lado sin cortarse.",
)

e = entrada(c, "recetas_color", "Cuatro recetas de color", "modamod:pattern_corazones", 4)
e.txt(
    "**Recetas que no necesitan horno.** Cuatro combinaciones para copiar sin vergüenza. Se editan en la Estación de Tintes, cuadradito por cuadradito.",
    "**1. Remera en degradé.** Un cuadradito de prenda entera, sin molde. Dos colores. //Variación: Degradé//. El color pasa de arriba a abajo sin que nadie se lo pida.",
    "**2. Rayas multicolor.** Molde de rayas en el cuadradito. Tres colores. //Variación: Alternar//. Cada raya toma el color siguiente: efecto circo con intención.",
    "**3. Corazones rojos y rosas con contorno negro.** Molde de corazones, tres colores (rojo, rosa y negro al final), //Contorno: sí//, //Variación: Alternar//. Con //Ladrillo// queda más tejido; con //Disperso//, más desordenado.",
    "**4. Corazones calados.** En una capa de corazones, //Transparencia// al 100 % en uno de los colores: la tela queda agujereada con forma de corazón. Es la única vez que un agujero en la ropa es una decisión de diseño.",
)
