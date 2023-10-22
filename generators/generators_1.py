#generator is simple way of creating an iterator
#(when to use yeild instead of return: https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/)
def remote_control_next():
    yield "cnn"
    yield "espn"
    yield "abpmazalive"
    yield "hotstar"

itr=remote_control_next()

print(itr)#it will print generator object  remote_control_next at 0x00000155D9D66B30

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))#automatically stop iteration exception will be generated as it is a generated

# for c in remote_control_next():
#     print(c)


#Benefits of using generators over class based iterator, 
#1)You don't need to define iter() and next() methods
#2)You don't need to raise StopIteration exception