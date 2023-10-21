x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=int(x)/int(y)
    print("Division is:",z)
except ZeroDivisionError as e:   #this is specific way of handling exception not generic
    print("Division by zero exception")  