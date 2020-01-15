i = range(1999, 3201)
l = list()
for n in i:
  if n%7 == 0 and n%5 != 0:
    l.append(n)

print(l)