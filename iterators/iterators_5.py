#the importance of iterator
#when we use list a=[1,2,3,4,5]
#list is iterable
#here all the elements of the list will consume memeory
#but when we convert then into iterator
#itr=iter(a)
#now here only when we call next function that time that element will take memory
#ex. next(itr): now 1 will take memory
#this will help when we have millions of data and we don't want to initialize at once to save memory
#there we use iterator so that only those elements will take memory whom are called by next or by any loop
#in for or any other loop, "stop iteration" exception is handled by default 
#that's why it does not give that error
