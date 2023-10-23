#here we will see how to use decorators

#(note:functions are first class objects in python. what it means is that they can be treated just like any
#other variable and you can pass them as argument to another function or even return them as a return value)

#first we need to define wrapper function, that function will take function as an argument
#python allows nested functions
#*args:positional argument and **kwargs:keyword arguments

import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result1 = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")#__name__ will return name of that function
        return result1
    return wrapper

@time_it#this is decorator (now the code is readable and the time code is restricte to one fuction)
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,10)
#when we call calc_square or calc_cube function, python will wrap it in the timer function for us
out_square = calc_square(array)
out_cube = calc_cube(array)