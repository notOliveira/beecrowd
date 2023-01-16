# 1072 

qtd = int(input())
dentro = 0
fora = 0

for i in range(1,qtd+1):
  X = int(input())
  if X >= 10 and X <= 20:
    dentro += 1
  else:
    fora += 1
print(dentro, "in")
print(fora, "out")