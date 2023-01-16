# 1080

numeros = []
for i in range(0,3):
  num = int(input())
  numeros.append(num)
maior = max(numeros, key=int)
print(maior)
print(numeros.index(maior)+1)