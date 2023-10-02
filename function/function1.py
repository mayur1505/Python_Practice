# function is block of code that performs a specific task
#Problem : if two list of numbers are given, then find total of each of these list


def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total


tom_list=[2100,3400,3500]
joe_list=[200,500,700]

toms_total=calculate_total(tom_list)
joes_total=calculate_total(joe_list)

print("Tom's expenses total is ",toms_total)
print("Joe's expenses total is ",joes_total)