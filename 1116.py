# 1116

N = int(input())

for i in range(0, N):
  valores = input().split()
  x = int(valores[0])
  y = int(valores[1])
  if y == 0:
    print("divisao impossivel")
  else:
    print("{:.1f}" .format(x/y))