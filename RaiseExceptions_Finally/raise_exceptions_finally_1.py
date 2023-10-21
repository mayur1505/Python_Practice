#Three topics
#1)how to raise standard exception
#2)how to raise user defined exception
#3)FinallyKeyword

#Let's begin with standard exception

#there are many standard exception in python (google "python builtin exceptions")
#for e.x. MemoryError

try:
    raise MemoryError('memory error') #here we used raise keyword with exception class name "MemoryError", but all of these classes
                                      #are derive from generic class "Exception"
except MemoryError as e:
    print(e)

#Here we use generic class "Exception"
# try:
#     raise Exception('memory error')
# except Exception as e:
#     print(e)