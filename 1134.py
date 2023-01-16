# 1134

comb = 0
alc = 0
gas = 0
die = 0

while comb != 4:
  comb = int(input())
  if comb == 1:
    alc += 1
  elif comb == 2:
    gas += 1
  elif comb == 3:
    die += 1
  elif comb == 4:
    break
  else:
    continue

print("MUITO OBRIGADO")
print("Alcool: {}" .format(alc))
print("Gasolina: {}" .format(gas))
print("Diesel: {}" .format(die))