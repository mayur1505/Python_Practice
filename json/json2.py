#we will write two programs
#1) to create address book and write some records into it
#2) read this address book

#There is no object called JSON in python.
#Pythn's native objects are numbers, strings, dictinoaries etc.
#JSON is just a concept and format, which is implemented by different languages. So all languages
#like c++, javascript, python supports it and it is a very generic concept
#Whereas dictinoary is only specific to python


#so we will make a dictinoary first
book={} #book is a dictinoary
book['ram']={
    'name':'ram',
    'address':'murgesh paliya, sector 1',
    'phone':8388438438
}
book['sham']={
    'name':'sham',
    'address':'whitefield, sector 3',
    'phone':62628438438
}


import json

s=json.dumps(book) #it is taking dictionary object book as an input and it is dumping it as a string
                #that's why we have 's' after dump
                #when this converts dic object to string , it will be converted to json format

with open("/home/mayurshimpi/Desktop/book.txt","w") as f:
    f.write(s)
#above two lines will create a text document and that will contain the book dictinoary 
#Now we can read this JSON data using any language that supports JSON such as javascript , c++ etc
#Hence this is called as data exchange format (i.e. exchanging data from python program to javascript program)
