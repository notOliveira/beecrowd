# 3209

testes = int(input())
somaTom = 0

for i in range(0,testes):
  tomadas = input().split()
  for x in range(len(tomadas)):
    somaTom = somaTom + int(tomadas[x])
  somaTom = somaTom - (len(tomadas)-2)
  print(somaTom-(int(tomadas[0])))
  somaTom = 0