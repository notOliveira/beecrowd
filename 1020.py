# 1020

idade = int(input()) # idade em dias

ano = idade // 365 # transforma a idade em anos
idade = idade % 365 # tira o valor da idade
mes = idade // 30 # transforma a idade em meses
idade = idade % 30 # tira o valor da idade

print(ano, "ano(s)")
print(mes, "mes(es)")
print(idade, "dia(s)")