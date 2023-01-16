# 1038

valor = input().split()

cod = int(valor[0])
qt = int(valor[1])
lanche = (4.00, 4.50, 5.00, 2.00, 1.50)

total = lanche[cod-1] * qt

print("Total: R$ {:.2f}" .format(total))