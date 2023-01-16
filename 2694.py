# 2694

N = int(input())

for i in range(0,N):
  valor = input()
  n1 = int(valor[2])*10
  n2 = int(valor[3])*1
  num1 = n1+n2

  n3 = int(valor[5])*100
  n4 = int(valor[6])*10
  n5 = int(valor[7])*1
  num2 = n3+n4+n5

  n6 = int(valor[11])*10
  n7 = int(valor[12])*1
  num3 = n6+n7
  print(num1+num2+num3)