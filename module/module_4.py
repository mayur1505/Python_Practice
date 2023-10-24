import module_3 #to imoprt custom module, just use file name without .py extension(as both the files are in same code directory)

print("Area of square",module_3.calculate_square_area(5))

#another way to import module
import module_3 as f

print("Area of Traingle",f.calculate_traingle_area(3,5))

#to import from  subdirectory
import  module_sub.function as f 

jo_list=[200,500,700]

jo_total=f.calculate_total(jo_list)
print("jo's total",jo_total)

#to import from totally different directory
#we will have to system path for this
import sys
sys.path.append("C:\\Users\\HP\\Desktop\\Preparation\\Python_Practice\\function")
import function1 as f1

mayur_list=[200,500,700]

mayur_list_total=f.calculate_total(mayur_list)
print("Mayur's total expens",mayur_list_total)