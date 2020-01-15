def GenerateFibonaci(x):
  a  = 1
  b = 1
  for i in range(x):
    yield a
    a, b = b, a+b

inp = int(input("Enter a number to generate fibonaci series upto: \t"))
for nu in GenerateFibonaci(inp):
  print(nu)