# 1064

v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())

pos = 0
somas = 0

if v1 >= 0:
  pos += 1
  somas = somas + v1

if v2 >= 0:
  pos += 1
  somas = somas + v2

if v3 >= 0:
  pos += 1
  somas = somas + v3

if v4 >= 0:
  pos += 1
  somas = somas + v4

if v5 >= 0:
  pos += 1
  somas = somas + v5

if v6 >= 0:
  pos += 1
  somas = somas + v6

print(pos, "valores positivos")
print("{:.1f}" .format(somas/pos))