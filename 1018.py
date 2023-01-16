# 1018

valor = int(input())
valor1 = valor

q100 = valor // 100
valor = valor % 100
q50 = valor // 50 
valor = valor % 50
q20 = valor // 20
valor = valor % 20
q10 = valor // 10
valor = valor % 10
q5 = valor // 5
valor = valor % 5
q2 = valor // 2
valor = valor % 2

print(valor1)
print(q100, "nota(s) de R$ 100,00")
print(q50, "nota(s) de R$ 50,00")
print(q20, "nota(s) de R$ 20,00")
print(q10, "nota(s) de R$ 10,00")
print(q5, "nota(s) de R$ 5,00")
print(q2, "nota(s) de R$ 2,00")
print(valor, "nota(s) de R$ 1,00")