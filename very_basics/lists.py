i1='bread'
i2='pasta'
i3='fruits'
#but if we have 100s of items, then we can't make 100s of variables
#the better way is to make list of this
items=['bread','pasta','fruits']#list got stored in item variable

print(items)
print(items[0])#to access particular location item in the list
#to change any item in the list
items[0]='chips'
print(items)

#to access range of elements
print(items[0:3])
print(items[-1])#to access last element

#to append
items.append('butter')#it will insert at last location
print(items)

#to insert at particular location
items.insert(2,'chicken')
print(items)

#how to add 2 lists
mitems=['guuter','sutter','mutter']

gitems=items+mitems
print(gitems)

#items+'soda' will throw error as TypeError: can only concatenate list(not 'str') to list

#len of list
print(len(items))

#to check if 'chicken' is their in items
print('chicken' in items)#true