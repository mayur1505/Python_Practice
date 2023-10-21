#here we will see how to handle multiple exceptions
# z= x / int(y) when we enter from terminal as input it is default string, 
# like here x will be string if enter from terminal 
#so here error will be TypeError: unsupported operandtype(s) for /: 'str' and 'int'

x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=(x)/int(y)
    print("Division is:",z)
except ZeroDivisionError as e:   #this is specific way of handling exception not generic
    print("Division by zero exception")  
except Exception as e:
    print("The other exception type is ",type(e).__name__)