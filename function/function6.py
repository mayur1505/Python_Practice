#Documentation string
#Way to document a function, when we have complicated function so to explain what that function does 
#like what does it expect as a output and what as a input
#for this we use tripple qoutes


def sum(a,b):
    """
    This function takes 2 arguments which are integer numbers and it will return
    sum of them as oupute
    """

    print("a:",a)
    print("b:",b)
    total=a+b
    return total

n=sum(b=5,a=4)
print("The sum is",n)