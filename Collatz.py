n = int(input('Ingresa n: '))
while n<=0:
   n=int(input('Ingresa n mayor a 0: '))
while n>0:
    print( n , end=' , ')
    if n%2 == 0:
      n //= 2
    else:
       n = n*3 + 1
    if n == 1:
      print('1.')
      break