def GenerateMethod(x):
  for i in range(x):
    yield x

g = GenerateMethod(5)
print(g.next)

strVal = 'Value'
strValues = iter(strVal)

print(type(strVal))
print(type(strValues))
print(next(strValues) + " --- " + next(strValues) +" --- " +  next(strValues) + " --- " + next(strValues) + " --- " + next(strValues))
