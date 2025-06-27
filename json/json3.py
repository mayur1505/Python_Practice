#this code will read the text file which we made in json2.py lecture/code

f=open("/home/mayurshimpi/Desktop/book.txt",'r')
s=f.read() #this will read the whole file in to this "s" variable
print(s) #this will print a string
print(type(s))

print()
#Suppose we want to know ram's phone number, then we have to use json module
#we have read this json string and parse it into a json object

import json
book=json.loads(s)#this will convert this "s" string into dictinoary
print(book)
print(type(book))

print(book['ram'])#print ram's address
print(book['ram']['phone'])

print()

for person in book:#print all the records from the dictinoary
    print(book[person])