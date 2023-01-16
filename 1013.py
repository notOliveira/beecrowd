# 1013


# Minha resposta - Errada, pois eu deveria usar a fórmula, porém totalmente funcional

valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if a > b and a > c:
  print(a, "eh o maior")
elif b > a and b > c:
  print(b, "eh o maior")
else:
  print(c, "eh o maior")