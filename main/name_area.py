#Let's see when does the __name__ value if different than __main__
#suppose we want to import area module from name_main.py file

import name_main
    

print("I am in name_area.py")
name_main.calculate_area(4,12)

