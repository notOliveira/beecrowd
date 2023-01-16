# 3174

qtd = int(input())

horaDes = 0
horaArq = 0
horaBon = 0
horaMus = 0

for i in range(0,qtd):
  elf = input().split()
  tipo = elf[1].lower()
  horas = int(elf[2])

  if tipo == "desenhistas":
    horaDes += horas
  elif tipo == "musicos":
    horaMus += horas
  elif tipo == "arquitetos":
    horaArq += horas
  elif tipo == "bonecos":
    horaBon += horas

qtdDes = horaDes // 12
qtdArq = horaArq // 4
qtdBon = horaBon // 8
qtdMus  = horaMus // 6

soma = qtdDes + qtdArq + qtdBon + qtdMus

print(soma)