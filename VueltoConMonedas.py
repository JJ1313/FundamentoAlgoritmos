from math import floor
nCasos = int(input('Ingrese n casos : '))
for i in range(nCasos):
    pagado = int(input('Pagado x cliente : '))
    compra = int(input('Valor compra : '))
    dif = pagado - compra
    if(dif == 0):
      print(f'CASO {i+1} : PAGO EXACTO !!')
    elif(dif < 0):
      print(f'CASO {i+1} : DEBE $ {-dif}')
    else:
      vuelto = dif
      m500 = floor(dif/500)
      dif %= 500
      m100 = floor(dif/100)
      dif %= 100
      m50 = floor(dif/50)
      dif %= 50
      m10 = floor(dif/10)
      dif %= 10
      m5 = floor(dif/5)
      dif %= 5
      m1 = dif
      print(f'CASO {i+1} : VUELTO = $ {vuelto} pesos chilenos --> {m500} {m100} {m50} {m10} {m5} {m1}')