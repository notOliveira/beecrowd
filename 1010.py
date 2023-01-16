# 1010

p1 = input()
p2 = input()

spl1 = (p1.split(" "))
spl2 = (p2.split(" ")) 

#Conversões
p1v0 = int(spl1[0])
p1v1 = int(spl1[1])
p1v2 = float(spl1[2])
p2v0 = int(spl2[0])
p2v1 = int(spl2[1])
p2v2 = float(spl2[2])

print("VALOR A PAGAR: R$ {:.2f}" .format((p1v1*p1v2)+(p2v1*p2v2)))