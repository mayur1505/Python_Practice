#strings are used to store text data in python
text="ice cream"
print(text)
print(text[0])
#text[0]='g' this will throw error as TypeError: 'str' object does not support item assignment
#because strings are immutable in python

#using index subrange we can access subtext
print(text[0:3])#first index is included "as it is" and "second-1" is the second one
print(text[4:])#start from 4th index and go till the end
print(text[0:3])#start from 0 and got till 2nd index
# " " or ' ' both are fine for strings
#text='let's learn python' #invalid syntax
text="let's learn python" #correct syntax for this case
text='hello "world"'

#how to store multiline string
#use triple quotes
address = '''murgesh paliya
vimanpura, bangalore
'''
print(address)


#concatenate two strings
s1='hello'
s2='world'
print(s1+s2)

#how to join a string with int
s='total states in usa #'
num=25
print(s + str(num))