# 1094

N = int(input())
coelhos = 0
ratos = 0
sapos = 0
qtdCob = 0

for i in range(0, N):
  exp = input().split()
  qtdExp = int(exp[0])
  animal = str(exp[1]).upper()
  qtdCob = qtdCob + qtdExp
  if animal == "C":
    coelhos = coelhos + qtdExp
  elif animal == "R":
    ratos = ratos + qtdExp
  elif animal == "S":
    sapos = sapos + qtdExp

perCoelhos = coelhos / (coelhos + ratos + sapos)*100
perRatos = ratos / (coelhos + ratos + sapos)*100
perSapos = sapos / (coelhos + ratos + sapos)*100

print("Total: {} cobaias" .format(qtdCob))
print("Total de coelhos: {}" .format(coelhos))
print("Total de ratos: {}" .format(ratos))
print("Total de sapos: {}" .format(sapos))
print("Percentual de coelhos: {:.2f} %" .format(perCoelhos))
print("Percentual de ratos: {:.2f} %" .format(perRatos))
print("Percentual de sapos: {:.2f} %" .format(perSapos))