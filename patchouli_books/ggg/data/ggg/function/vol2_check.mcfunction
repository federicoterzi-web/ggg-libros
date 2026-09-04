# Chequea cada tick si un jugador ya tiene las 9 advancements de zona de las_vegas (Vol. II).
# Si las tiene todas y todavia no le dimos la copia completa, le otorga ggg:vol2_completado
# (su loot_table le entrega el libro patchouli:las_vegas_completa).
execute as @a[advancements={ggg:casino_lucky_38=true,ggg:casino_gomorra=true,ggg:galeria_del_fan_art=true,ggg:hotel_vault_21=true,ggg:red_rocket=true,ggg:fabrica_abandonada=true,ggg:mercado_negro=true,ggg:biblioteca_abandonada=true,ggg:capilla=true,ggg:vol2_completado=false}] run advancement grant @s only ggg:vol2_completado
