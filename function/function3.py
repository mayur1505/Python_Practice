# in function2 example, pass b value first and then a
#we have to use named arguments here
def sum(a,b):
    print("a:",a)
    print("b:",b)
    total=a+b
    return total

n=sum(b=5,a=4)
print("The sum is",n)