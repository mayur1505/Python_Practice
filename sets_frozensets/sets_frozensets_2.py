x={"a","b","c"}
"a" in x#true
for i in x:
    print(i)#set is iterable

y={"a","h","g"}

#we can find out union, intersection, subsets etc

#union
print(x|y)
#intersection
print(x&y)
#difference
print(x-y)
print(y-x)
#subsets
#if we want to check wheather x is subset of y
print(x<y)