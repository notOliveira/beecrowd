# 1214

testes = int(input())
total = 0

for i in range(1,testes+1):
  total = 0
  acimaMedia = 0
  valores = input().split()
  qtdeValores = int(valores[0])

  for j in range(1,qtdeValores+1):
    total = total + int(valores[j])
  media = total/int(valores[0])
  for k in range(1,qtdeValores+1):
    if int(valores[k]) > media:
      acimaMedia += 1
  result = float((acimaMedia*100)/int(valores[0]))
  print('{:.3f}%' .format(result))