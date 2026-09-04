# Chequea cada tick si un jugador ya tiene las 30 advancements de zona de guia_turistica (Vol. I).
# Si las tiene todas y todavía no le dimos el Volumen II, le otorga ggg:vol1_completado
# (su loot_table le entrega el libro patchouli:las_vegas).
#
# IMPORTANTE: si se agrega una zona nueva a guia_turistica con su propio advancement
# (ej. el_escondite_del_neuro, pendiente de coordenadas), hay que sumarla acá abajo.
execute as @a[advancements={ggg:venta_de_peces=true,ggg:maderera_riva=true,ggg:tegridy_farms=true,ggg:tienda_de_exploradores=true,ggg:la_herreria_de_polar=true,ggg:memuebles_2=true,ggg:gachapon=true,ggg:iglesia=true,ggg:mural_comunitario=true,ggg:casa_de_rozsier=true,ggg:joyeria_don_carlos=true,ggg:me=true,ggg:mercadito=true,ggg:tienda_de_artefactos=true,ggg:torre_del_magoldito=true,ggg:carnicero=true,ggg:femboy_hooters=true,ggg:kfc=true,ggg:jose_palmera=true,ggg:manga_cafe=true,ggg:panaderia_el_panochon=true,ggg:taberna=true,ggg:el_otraniano=true,ggg:la_covacha_de_sadako=true,ggg:maus=true,ggg:hotel_galvhiar=true,ggg:oficina_de_empleo=true,ggg:tienda_de_protecciones=true,ggg:portal_del_nether=true,ggg:travis_bickle=true,ggg:vol1_completado=false}] run advancement grant @s only ggg:vol1_completado
