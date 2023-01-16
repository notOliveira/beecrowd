# 1182

c = int(input())
t = input().upper() # S = SOMA / M = MEDIA
soma = 0
matrix = [0]*12

for i in range(len(matrix)):
  matrix[i] = [0]*12
  for j in range(len(matrix[i])):
    matrix[i][j] = float(input())

for k in range(0,len(matrix)):
  soma = soma + matrix[k][c]

if t == "S":
  print("{:.1f}" .format(soma))
elif t == "M":
  print("{:.1f}" .format(soma/(len(matrix))))