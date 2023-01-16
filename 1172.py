# 1172

lista = [0.0]*10
contador = 0

for contador in range(len(lista)):
  valor = int(input())
  if valor > 0:
    lista[contador] = valor
  else:
    lista[contador] = 1
  print("X[{}] = {}" .format(contador, lista[contador]))
  contador += 1