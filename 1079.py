# 1079

N = int(input())

for i in range(0, N):
  valores = input().split()
  a = float(valores[0])*2
  b = float(valores[1])*3
  c = float(valores[2])*5

  media = (a+b+c)/10
  print("{:.1f}" .format(media))