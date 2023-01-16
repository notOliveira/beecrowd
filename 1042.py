# 1042

# Minha resposta - Funcional, porém mal otimizada e muito grande

valores = input().split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if a < b < c:
  print(a, b, c, sep = "\n")
elif a < c < b:
  print(a, c, b, sep = "\n")
elif b < a < c:
  print(b, a, c, sep = "\n")
elif b < c < a:
  print(b, c, a, sep = "\n")
elif c < a < b:
  print(c, a, b, sep = "\n")
else:
  print(c, b, a, sep = "\n")

print("\n", a, b, c, sep = "\n")