#Problem:Store monthly expenses in a list and find out total expenses for all months
exp = [2340, 2500, 3200, 5309, 3233]

#total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]

#print("The total expenses in all January to may is",total)
total=0
# for exp in exp:
#     total=exp+total
# print("The total expense is",total)

# print month number and expense and then in the end print total expense
for i in range(len(exp)):
    print("Month",(i+1),"Expense",exp[i])
    total=exp[i]+total
print("The total expesne is",total)
