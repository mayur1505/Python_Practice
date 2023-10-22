#1)what are iterators
#2)Iterator implementation using class

a=["hey","bro","how","are","you"]

for i in a:
    print(i)

print(dir(a))#The dir() function returns all properties and methods of the specified object,
#without the values. This function will return all the properties and methods, 
#even built-in properties which are default for all object.
#after printing print(dir(a)) we can see __iter__ in output

#iternally __iter__  function is used for iterating
itr=iter(a)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


#so "for" loop has an iterator and each time when we iterate, it internally calls next method
