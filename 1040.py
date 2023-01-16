# 1040

valores = input().split()

n1 = float(valores[0])*2
n2 = float(valores[1])*3
n3 = float(valores[2])*4
n4 = float(valores[3])*1

media = float((n1+n2+n3+n4)/10)A,B,C = map(float,input().split())
if (A+B)>C and (A+C)>B and (B+C)>A:
    perimeter = (A+B+C)
    print(f"Perimetro = {perimeter:0.1f}")
else:
    area = 0.5*(A+B)*C
    print(f"Area = {area:0.1f}")

print("Media: {:.1f}" .format(media))

if media >= 7.0:
  print("Aluno aprovado.")
elif media < 5.0:
  print("Aluno reprovado.")
else: # media >= 5.0 and media < 6.9
  print("Aluno em exame.")
  x = float(input())
  print(f'Nota do exame: {x:.1f}')
  mediaf = (media+x)/2
  if mediaf > 5:
    print("Aluno aprovado.")
    print("Media final: {:.1f}" .format(mediaf))
  else:
    print("Aluno reprovado.")
    print("Media final: {:.1f}" .format(mediaf))