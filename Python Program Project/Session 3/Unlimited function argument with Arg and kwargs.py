def AddFunctionArgUnlimited(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)

AddFunctionArgUnlimited(1)
AddFunctionArgUnlimited(1,2)
AddFunctionArgUnlimited(1,2,3)
AddFunctionArgUnlimited(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)

def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
intro(s1=1, s2=2, s3=3, s4=4, s5=5)