#reading the file line by line
#start with creating new file and writing content to it
f=open("/home/mayurshimpi/Desktop/python_practice/Python_Practice/filemode/reading.txt",'r')# r is 
                                                                                          # read mode
#first we will open in 'w' mode, we will write below content in that file
# and then we will open in read mode 
                                                                                          
# f.write("""John: Hi Henry

# Henry: Hi John, after a long time.

# John: Yeah dude, where do you live now?

# Henry: With my parents

# John: Where do your parents live?

# Henry: With me

# John: Where do you all live?

# Henry: Together

# John: Dude don't joke

# Henry: I'm not joking dude

# John: Ok, now tell me, where is your house?

# Henry: Next to my neighbor's house

# John: Where is your neighbor's house?

# Henry: Next to my house

# John: Grrrrrrr""")

# print(f.read())#if we use mode as 'r', then we can read that file content like this
#f.close()#closing file will free up all the resources operating system will allocate for this file

#for each line we want to count number of words and append towards end
# words are separeated by spaces, if we can figure out spaces we can count number of words
#we will use split function here
#The split() method splits a string into a list(array of words) and the default separator is white space
#https://www.w3schools.com/python/ref_string_split.asp

f_out=open("/home/mayurshimpi/Desktop/python_practice/Python_Practice/filemode/reading_wordcount.txt",'w')

for line in f:
    tokens=line.split()
    #print(line)
    #print((tokens))
    #print(len(tokens))
    f_out.write(" wordcount:"+str(len(tokens))+ line)#token number will be converted to str and will be added to line


f.close()#closing file will free up all the resources operating system will allocate for this file
f_out.close()


#python file opening modes
#https://www.geeksforgeeks.org/reading-writing-text-files-python/


#with statement
#In above code we have to explicitely open and close the file
#Sometimes in bigger program we may forget this and that's not good

#So if we don't need to do f.close() and we want file to automatically close then we have to use with statement

with open("/home/mayurshimpi/Desktop/python_practice/Python_Practice/filemode/reading_wordcount.txt",'r') as f:
    print(f.read())


print(f.closed) #f.closed flag tells that if the file the closed or still open