# 1048

salario = float(input())

reajuste = 0

if salario >= 0 and salario <= 400:
  reajuste = 0.15*salario
  print("Novo salario: {:.2f}" .format(reajuste+salario))
  print("Reajuste ganho: {:.2f}" .format(reajuste))
  print("Em percentual: 15 %")
elif salario > 400 and salario <= 800:
  reajuste = 0.12*salario
  print("Novo salario: {:.2f}" .format(reajuste+salario))
  print("Reajuste ganho: {:.2f}" .format(reajuste))
  print("Em percentual: 12 %")
elif salario > 800 and salario <= 1200:
  reajuste = 0.10*salario
  print("Novo salario: {:.2f}" .format(reajuste+salario))
  print("Reajuste ganho: {:.2f}" .format(reajuste))
  print("Em percentual: 10 %")
elif salario > 1200 and salario <= 2000:
  reajuste = 0.07*salario
  print("Novo salario: {:.2f}" .format(reajuste+salario))
  print("Reajuste ganho: {:.2f}" .format(reajuste))
  print("Em percentual: 7 %")
elif salario > 2000:
  reajuste = 0.04*salario
  print("Novo salario: {:.2f}" .format(reajuste+salario))
  print("Reajuste ganho: {:.2f}" .format(reajuste))
  print("Em percentual: 4 %")