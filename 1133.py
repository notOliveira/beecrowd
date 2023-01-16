# 1133

# Minha resposta, correta e funcional, porém não aceita

x = int(input())
y = int(input())

a = min(x,y)
b = max(x,y)

for i in range(a, b):
  if i % 5 == 2 or i % 5 == 3:
    print(i)