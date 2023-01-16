# 1074

N = int(input())

for i in range(0,N):
  num = int(input())
  if num > 0: # positivo
    if num % 2 == 0: # par
      print("EVEN POSITIVE")
    else:
      print("ODD POSITIVE")
  elif num == 0: # nulo
    print("NULL")
  else:
    if num % 2 == 0: # par
      print("EVEN NEGATIVE")
    else:
      print("ODD NEGATIVE")