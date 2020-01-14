
def CheckforPrime(x):
  inc = 2
  while inc < x:
    if x%inc == 0:
       print(str(x) + " is a composite number")
       break;
    else:
      inc = inc + 1
  else:
    print(str(inp) + " is a prime number")

inp = int(input("Enter a number to check for prime or composite: \t"))
if inp == 0 or inp == 1:
  print(str(inp) + " is neither prime or composite number")
else:
  CheckforPrime(inp)
