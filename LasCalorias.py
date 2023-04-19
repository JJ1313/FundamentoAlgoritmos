from math import ceil 
e = -1
nCaso = 1
while e != 0:
  e = int(input('Ingresa calorias consumidas x entrenamiento : '))
  if(e > 0):
    nComilonas = int(input('Ingresa n comilonas :'))
    totalConsumidas = 0
    for i in range(nComilonas):
      totalConsumidas += int(input(f'Ingrese calorias en comilona {i+1} : '))
    # ------ Calcular la cantidad de entrenamientos ------
    # Si el resultado no es exacto hay q encontrar el entero superior mas cercano

    entrenamientosFloat = totalConsumidas / e # Resultado en float
    nEntrenamientos = int(entrenamientosFloat) # Parte entera del resultado
    if(entrenamientosFloat > nEntrenamientos): # Caso en que el resultado en float no es exacto
      nEntrenamientos += 1  # Se le suma 1 al entero para compensar la fraccion faltante
    # --- Misma funcion pero usando math.ceil()
    #nEntrenamientos = ceil(totalConsumidas / e)
    print(f'''CASO {nCaso} :
Fitnesstencio consume {e} calorias cada entrenamiento.
Fitnesstencio consumio {totalConsumidas} calorias en sus {nComilonas} comilonas.
Fitnesstencio debe realizar {nEntrenamientos} entrenamientos(s).
''')
  nCaso += 1