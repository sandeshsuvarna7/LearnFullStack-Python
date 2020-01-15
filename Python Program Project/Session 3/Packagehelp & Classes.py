import math
print(dir(math)) #Get all function inside an package

help(math.ceil) #get the assistance of command with help keyword

print(math.ceil(5.1243))

class Person:
    def __init__(self, name, surname, year_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
        
    def setValue(self, name, surname, year_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
    
    def age(self, current_year):
        return current_year - self.year_of_birth
    
    def __str__(self):
        return "%s %s was born in %d." %(self.name, self.surname, self.year_of_birth)


per = Person("Jio", "Kumar", 2012)
print(per)
print(per.age(2020))


class Student(Person):

#Shortcut to pass paramters to parent class
#     def __init__(self, student_id, *args, **kwargs): 
#         super(Student, self).__init__(*args, **kwargs)
#         self.student_id = student_id

      def __init__(self, student_id, sname, ssurname, syear_of_birth):
        super(Student, self).__init__(sname, ssurname, syear_of_birth)
        self.student_id = student_id
    
      def welcome(self):
        print(self.name, self.surname, ", your student ID is", self.student_id, "and date of birth is", self.year_of_birth)

stud = Student(101, 'Ranbir', 'Kapoor', 1985)
print(stud)
print(stud.age(2021))
print(stud.welcome())


class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person1("John", 36)

p1.age = 40

print(p1.age)
print(p1.name)

