# 1049

n1 = input()
n2 = input()
n3 = input()

# VERTEBRADOS

if n1 == "vertebrado":
  # AVES
  if n2 == "ave":
    if n3 == "carnivoro":
      print("aguia")
    elif n3 == "onivoro":
      print("pomba")
    # MAMIFEROS
  elif n2 == "mamifero":
    if n3 == "onivoro":
      print("homem")
    elif n3 == "herbivoro":
      print("vaca")

# INVERTEBRADOS

if n1 == "invertebrado":
  # INSETOS
  if n2 == "inseto":
    if n3 == "hematofago":
      print("pulga")
    elif n3 == "herbivoro":
      print("lagarta")
  # ANELIDEOS
  elif n2 == "anelideo":
    if n3 ==  "hematofago":
      print("sanguessuga")
    elif n3 == "onivoro":
      print("minhoca")