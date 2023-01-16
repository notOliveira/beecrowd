# 1154

qtd = 1
idade = 1
soma = 0
while idade > 0:
    idade = int(input())
    if idade < 0:
        break
    else:
        soma = soma + idade
        qtd +=1
print(soma/qtd)
print(qtd)