 fname = input("First name: \t")
  lname = input("Last name: \t")
   
  print("Your name: " +lname + " " + fname)

  fname = Reverse(fname)
  lname = Reverse(lname)

  print("Your name in reverse: " +fname + " " + lname)


name = input("Your name: \t")
print(name.split(' ')[1] + " " +name.split(' ')[0])


def Reverse(name):
  su = ""
  i = 1
  i = int(i)
  while i <= len(name):
    su = su + name[len(name) - i]
    i = i + 1

  return su