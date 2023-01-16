# 1113
valores = []*2

while True:
  valores = input().split()
  x = int(valores[0])
  y = int(valores[1])
  if x == y:
    break
  if x < y:
    print("Crescente")
  else:
    print("Decrescente")