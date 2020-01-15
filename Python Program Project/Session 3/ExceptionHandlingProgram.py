def Division(x, y):
    return x / y
    
try:
    x = int(input("Enter an Divisor value: \t"))
    y = int(input("Enter an Dividend value: \t"))
    print("Quotient: " +str(Division(x, y)))
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
except ValueError as err:
    print("Please enter only integer value..." + err)
finally:
    print("Finally executed...")