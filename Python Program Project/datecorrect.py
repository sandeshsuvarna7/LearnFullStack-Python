dateinput = input("Enter date in dd/mm/yyyy format: \t")
print(dateinput)
#if len(dateinput) == 10 and dateinput.split('/').count == 3:
#if len(dateinput) == 10:
  #datex = dateinput.split('/')[0]
  #monthx = dateinput.split('/')[1]
  #yearx = dateinput.split('/')[2]
datex = dateinput[0:2]
monthx = dateinput[3:5]
yearx = dateinput[6:10]
print(datex + " " + monthx + " " + yearx)
if len(dateinput) == 10:
  if datex > 31:
    print("Day should be less than 31")
  
  if monthx > 12:
    print("Month should be less than 12")
  
  if len(yearx) == 4 and yearx > 1951 and yearx < 2050:
    print("Year should be between 1951 and 2050")
    if(yearx%)
else:
  print("Date format incorrect")

