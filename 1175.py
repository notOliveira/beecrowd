# 1175

lista = [0.0]*20
contador = 0

for contador in range(len(lista)):
  valor = int(input())
  lista[contador] = valor

contador = 0
listaNova = list(reversed(lista))

for contador in range(len(lista)):
  print("N[{}] = {}" .format(contador, listaNova[contador]))