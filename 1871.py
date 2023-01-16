# 1871

valores = 0
characters = "0"
x = 1
y = 1

while True:
  valores = input().split()
  x = int(valores[0])
  y = int(valores[1])
  if x == 0 and y == 0:
     break
  valor = x + y
  stValor = str(valor)
  for x in range(len(characters)):
    stValor = stValor.replace(characters[x],"")
  print(stValor)