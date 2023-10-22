#list comprehension provides a way to transform one list into another
a=[1,2,3,4,5,6,7,8]
#let's say we want a list from above list which will contain only even numbers
#the traditional way of doing this is
# even=[]
# for i in a:
#     if i%2==0:
#         even.append(i)

# print(even)

#but list comprehension gives another way to do this in short
even=[i for i in a if i%2==0]
print(even)
#squre
square=[i*i for i in a]
print(square)