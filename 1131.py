# 1131
opcao = 0
winInt = 0
winGre = 0
empate = 0
grenais = 0

while True:
  grenais += 1
  IXG = input().split()
  inter = int(IXG[0])
  gremio = int(IXG[1])

  if inter > gremio:
    winInt += 1
  elif gremio > inter:
    winGre += 1
  elif gremio == inter:
    empate += 1
  print("Novo grenal (1-sim 2-nao)")
  opcao = int(input())
  if opcao == 2:
    break

print("{} grenais" .format(grenais))
print("Inter:{}" .format(winInt))
print("Gremio:{}" .format(winGre))
print("Empates:{}" .format(empate))

if winInt > winGre:
  print("Inter venceu mais")
elif winGre > winInt:
  print("Gremio venceu mais")
else:
  print("Nao houve vencedor")