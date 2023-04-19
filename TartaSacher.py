import math
nPruebas = int(input('Ingrese cantidad de pruebas: '))
for i in range(nPruebas):
    ancho = int(input('Ingrese ancho chocolate: '))
    alto = int(input('Ingrese alto chocolate: '))
    r = int(input('Ingrese cantidad de cuadritos para la receta: '))
    nCuadritos = ancho * alto
    nTabletas = math.ceil(r / nCuadritos)
    print(f"""CASO {i+1} :
Una tableta de chocolate tiene {ancho} x {alto} = {nCuadritos}.
Necesitas {r} cuadrados para la tarta Sacher.
Debes comprar como minimo {nTabletas} tableta(s) de chocolate.
    """)
