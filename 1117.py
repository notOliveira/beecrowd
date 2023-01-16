# 1117

nota1 = float
nota2 = float

while nota1 == float or nota2 == float:
  nota = float(input())
  if nota >= 0 and nota <= 10:
    if nota1 != float:
      nota2 = nota
    else:
      nota1 = nota
  else:
    print("nota invalida")

media = (nota1+nota2)/2
print("media = {:.2f}" .format(media))