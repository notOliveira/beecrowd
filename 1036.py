# 1036

valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

delta = (B**2)-(4*A*C)

if delta <= 0 or A <= 0 or 2*A == 0:
  print("Impossivel calcular")
else:
  X1 = (-B+(delta**0.5))/(2*A)
  X2 = (-B-(delta**0.5))/(2*A)
  print("R1 = {:.5f}" .format(X1))
  print("R2 = {:.5f}" .format(X2))