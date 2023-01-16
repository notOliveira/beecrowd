# 1184

O = input().upper() # S = SOMA / M = MEDIA
soma = 0
matrix = [0]*12
qtd = 0
controle = 10

for i in range(len(matrix)):
  matrix[i] = [0]*12
  for j in range(len(matrix[i])):
    matrix[i][j] = float(input())

for i in range((len(matrix)-1), 0, -1):
  for j in range(controle, -1, -1):
    soma = soma + matrix[i][j]
    qtd += 1
  controle -= 1

if O == "S":
  print("{:.1f}" .format(soma))
elif O == "M":
  print("{:.1f}" .format(soma/qtd))