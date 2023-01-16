# 3358

exec = int(input())
cons = 0

for x in range(0, exec):
  nome = input()
  for i in range(len(nome)):
    if cons == 3:
      break
    if nome[i].upper() in 'AEIOU':
      cons = 0
    else:
      cons += 1
  if cons >= 3:
    print(nome, "nao eh facil")
  else:
    print(nome, "eh facil")
  cons = 0