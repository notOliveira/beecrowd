# 1173

lista = [0.0]*10
contador = 0

i = int(input())

for contador in range(len(lista)):
  lista[contador] = i
  print("N[{}] = {}" .format(contador, lista[contador]))
  i *= 2