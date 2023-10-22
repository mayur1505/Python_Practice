#set is a unordered collection of unique items (it doesn't allow duplicates), but in Lists duplicates are allowed
#and this is the major difference between list and set
s=set([1,2,3,4,35,3,4,34,22,67,87,89,12,14,15])
print(s)#set will cleanout duplicates
#in set we have to curly brackets for comprehension
even={i for i in s if i%2==0}
print(even)