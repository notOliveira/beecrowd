# 1099

# Minha resposta, funcional

testes = int(input())
soma = 0

for i in range(1,testes+1):
  valores = input().split()
  x = int(min(valores))
  y = int(max(valores))
  for w in range(x+1,y):
    if w % 2 != 0:
      soma = soma + w
  print(soma)
  soma = 0