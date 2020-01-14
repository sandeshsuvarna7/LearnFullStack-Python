myList = ['Go', 'Learn', 'Python list']
myList.append([1,2,3, 'Sandesh', 'AcadGild']) # ['Go', 'Learn', 'Python list', [1, 2, 3, 'Sandesh', 'AcadGild']]

myList + ['Test without initialization']; 
myList1 = myList + ['Test initialization']; #['Go', 'Learn', 'Python list', [1, 2, 3, 'Sandesh', 'AcadGild'], 'Test initialization']

print(myList)

print(myList1 * 3)

print(myList + myList1)

print(myList[3][3])

star = ['*']
counter = int(input("Maximum Star design required: \t"))
i = int(1)
while i <= counter:  
  star1 = star * i
  print(star1)
  i = i + 1

while counter:  
  counter = counter - 1
  star1 = star * counter
  if counter != 0:
    print(star1)

