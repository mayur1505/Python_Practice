#Default arguments

def sum(a,b=0): #dafault arg for b is 0, if we don't pass anything it will consider as 0
    print("a:",a)
    print("b:",b)
    total=a+b
    return total

n=sum(3)
print("The sum is",n)