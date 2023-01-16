# 2867

C = int(input())

for i in range(0, C):
  valores = input().split()
  n = int(valores[0])
  m = int(valores[1])
  qtd = n**m
  print(len(str(qtd)))