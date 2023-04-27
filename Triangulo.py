

while (True):
  n =  int(input("Alto triangulo: "))
  if(n>=1):
    break


for i in range(1, n+1):
    for j in range(1, i+1):    
      print(j, end=" ")
    for k in range(j-1, 0, -1):
      print(k, end=" ")
    print()

for i in range(1, n+1):
  sumar = True
  j=1
  while(True):
      if(j==0):
         break
      print(j, end=" ")
      if j == i:
        sumar= False
      if(sumar):
         j+=1
      else:
         j-=1
  print()