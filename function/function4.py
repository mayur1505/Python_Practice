#Global vs local variables
total=0   #global variable
def sum(a,b):
    print("a:",a)
    print("b:",b)
    total=a+b
    print("total inside function is:",total)
    return total    #local variable

n=sum(b=5,a=4)
print("The sum is",total)