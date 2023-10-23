#set is an unordered collection of unique elements
basket={"orange","apple","mango","apple","orange"}#one of the ways of initializing sets
print(type(basket))#basket is set class
print(basket)#duplicates will be removed

a=set()#another way of initializing sets
a.add(1)
a.add(2)
a.add(3)
print(a)

#if we initialize as a={} 
#then it will be type "dict" because we initialized empty
#but if a={"mayur"}
#then it will be type "set"


#set is unordered
#means we cannot access them using indexing
#for ex. print(basket[2]) will throw error as 'set' object does not support indexing
#but "list" allows indexing and it allows duplicates also


#so if we want to remove duplicates from the list we can use set
#for ex.
numbers=[1,2,3,4,2,1,3,6,7]
unique=set(numbers)#set supports taking list as input in the constructor
print(unique)
#here we can change the content of our set
unique.add(9)
print(unique)

#but we often want our set to be frozen
#means we should not be able to change the content of our set
#in that case we have to use frozensets
fs=frozenset({1,2,3,4})#frozenset and set are same as they are unordered and store only uniques
#but frozenset does not allow to add new elements i.e.we can't change anything in fs
