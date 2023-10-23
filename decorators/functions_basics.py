# In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.

# The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.


# Prerequisites for learning decorators
# Before we learn about decorators, we need to understand a few important concepts related to Python functions. Also, 
# remember that everything in Python is an object, even functions are objects.

#Nested Function
def outer(x):
    def inner(y):
        print("I am in inner function")
        return x + y
    print("I am in outer function")
    return inner

add_five = outer(5)
result = add_five(6)
print(result)

#pass function as argument
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10

#Return a Function as a Value
def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"

# Output: Hello, Atlantis!

#new learning
def compose(f,g,x):#f and g are function and x is a varaible
    return f(g(x))

compose(print,len, "Hello, world")#len of string is 12