# 1060

v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())

pos = 0

if v1 >= 0:
  pos += 1
if v2 >= 0:
  pos += 1
if v3 >= 0:
  pos += 1
if v4 >= 0:
  pos += 1
if v5 >= 0:
  pos += 1
if v6 >= 0:
  pos += 1

print(pos, "valores positivos")