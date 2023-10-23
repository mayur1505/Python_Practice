import time
#we will calculate how much time a function is taking to their performance

def calc_square(numbers):
    start=time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end=time.time()
    print("Cal_square took " + str((end-start)*1000) +":milliseconds")#multiplying by 1000 to convert into millisecods
    return result


def calc_cube(numbers):
    start=time.time()    
    result = []
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    print("Cal_cube took " + str((end-start)*1000) + ":milliseconds")#multiplying by 1000 to convert into millisecods
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

#suppose we have written very big code
#which has almost 200 functions
#so to measure performance we will check how much time it took to execute
#but in every function writing start=time.time() and end=time.time() is not feasible
#so the better way of doing this is decorators
#Decorators allows us to wrap our function in another function
