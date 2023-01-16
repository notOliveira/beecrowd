# 1019

N = int(input())

horas = N // 3600
horas = horas % 3600
minutos = N // 60
minutos = minutos % 60
N = N % 60

print("{}:{}:{}" .format(horas, minutos, N))