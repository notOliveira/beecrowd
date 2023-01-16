# 1012

valores = input()
pi = 3.14159
spl = valores.split()


A = float(spl[0])
B = float(spl[1])
C = float(spl[2])

print("TRIANGULO: {:.3f}" .format((A*C)/2))
print("CIRCULO: {:.3f}" .format((C**2)*pi))
print("TRAPEZIO: {:.3f}" .format(((A+B)*C)/2))
print("QUADRADO: {:.3f}" .format(B**2))
print("RETANGULO: {:.3f}" .format(A*B))