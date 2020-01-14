dictemp = {'107': 'Sandesh', '102' : 'Aditya', '111': 'Swapnil', '109': 'Sandesh', '105' : 'Salman'}
temp = list()
for key1 in dictemp:
  if dictemp[key1] not in temp:
    temp.append(dictemp[key1])
  else:
    print(temp)