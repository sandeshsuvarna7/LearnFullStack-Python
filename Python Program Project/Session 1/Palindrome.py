 fname = input("Enter Value to check Palindrome condition: \t")
 print("Your value: " +fname)
 #revname = Reverse(fname)
 revname = ""
 i = 1
 i = int(i)
 print(len(fname))
 while i <= len(fname):
   revname = revname + fname[len(fname) - i]
   print (revname)
   i = i + 1
 if revname==fname:
   print(revname + " is a palindrome " + fname)
 else:
     print(fname + " is not a palindrome " + revname)

print(revname.lower() is fname.lower())
print(revname.lower() +" - " + fname.lower())