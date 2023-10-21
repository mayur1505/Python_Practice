#Exception are errors detected at the time of program execution
#when we divide anything by zero we get exception as ZeroDivisonError: division by zero
#when we do "abc"+123, we ge TypeError: Can't convert  'int' object to str implicitly

#now we will see how to handle exception in generic way
x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=int(x)/int(y)
    print("Division is:",z)
except Exception as e:   #this is generic way of handling exception
    print("Exception Occured: ",e)   
