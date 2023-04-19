nCasos = int(input('Ingrese n casos : '))
for i in range(nCasos):
    inicio = int(input('Inicio : '))
    final = int(input('Final :'))
    dif = final - inicio
    if dif < 0:
      dif += 360
    if dif == 180 or dif == 0:
      mensaje = 'DA IGUAL'
    elif 180 > dif and dif > 0:
      mensaje = 'ASCENDENTE'
    else:
      mensaje = 'DESCENDENTE'
    print(f'CASO {i + 1} : {inicio} a {final} grados --> {mensaje}')