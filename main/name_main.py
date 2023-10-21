#https://www.geeksforgeeks.org/__name__-a-special-variable-in-python/

def calculate_area(base,height):
    print("__name__:",__name__)
    return 1/2*(base*height)

#__name__ is by default set to __main__
#it is a entry point to a code in python
#in C main() is the entry point
if __name__== "__main__":
    print("I am in area.py")
    a=calculate_area(10,20)
    print("Area",a)

