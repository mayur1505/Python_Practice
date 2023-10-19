#reading and writing to files
#1) create a new file and write to it
#2) Reading file line by line
#3) file open modes
#4) with statement

#start with creating new file and writing content to it
f=open("/home/mayurshimpi/Desktop/python_practice/Python_Practice/filemode/funny.txt",'w')# w is 
                                                                                          # write mode
f.write("I love Python")
f.close()#closing file will free up all the resources operating system will allocate for this file

#when we are using "w" as mode, it will overwrite the previous content
#for appending new content to old content we have to use "a" mode
f1=open("/home/mayurshimpi/Desktop/python_practice/Python_Practice/filemode/funny.txt",'a')
f1.write("\nI have again started preparation")
f1.close()