import math
nCasos = int(input('Casos de prueba :'))
for i in range(nCasos):
    print('Ingresa numero de losetas...')
    ancho = int(input('Ancho : '))
    alto = int(input('Alto : '))
    losetasTotal = ancho * alto
    losetasClaras = int((losetasTotal / 2)) + (losetasTotal % 2)
    losetasOscuras = int(losetasTotal/2) 
    print(f'Total Losetas = 1 --> Losetas Claras : {losetasClaras} , Losetas Oscuras : {losetasOscuras}')