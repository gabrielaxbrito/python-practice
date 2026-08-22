segs = int(input("Digite um valor em segundos"))

#o resto da divisao por minutos me da os segundos
mod_segundos = segs % 60
minutos = segs // 60

#o resto da divisao por horas me da os minutos
mod_minutos = minutos % 60
hora = minutos // 60

print(f"{hora} hora(s), {mod_minutos} minuto(s) e {mod_segundos} segundo(s)")
