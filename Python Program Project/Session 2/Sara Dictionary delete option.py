student_data = {'id1':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id2':
{'name': ['David'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id3':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id4':
{'name': ['Surya'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
}

dictTemp = dict()
name = list()
for key1 in student_data:
  value = str(student_data[key1]['name'])
  cond = any(ele in value for ele in name)
  if not cond:
    name = name + student_data[key1]['name']
    print(str(name))
  else:
    studentname = student_data[key1]['name']
    dictTemp[key1] = student_data[key1]

for key2 in dictTemp:
  del student_data[key2]

print(student_data)

