# 1183

O = input().upper() # S = SOMA / M = MEDIA
soma = 0
matrix = [0]*12
controle = 1
qtd = 0

for i in range(len(matrix)):
  matrix[i] = [0]*12
  for j in range(len(matrix[i])):
    matrix[i][j] = float(input())

for k in range(0,len(matrix)):
  for l in range(controle,len(matrix[i])):
    soma = soma + matrix[k][l]
    qtd += 1
  controle += 1

if O == "S":
  print("{:.1f}" .format(soma))
elif O == "M":
  print("{:.1f}" .format(soma/qtd))