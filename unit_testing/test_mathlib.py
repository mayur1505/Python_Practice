#2nd Lecture
#this is a unit test file for test_mathlib.py
# import mathlib #importing file which need to be tested

#pytest use some discovery rules to find out test cases
#so one of the discovery rule is to look for prefix which has "test_"
#so that's why give "test_" as prefix to every function which need to be tested
#and give prefix as "test_" to the unit test file name also
#if we don't use this prefix then commands for running test file won't work

#code
# def test_calc_total():#test_ prefix in front of function name
#     total=mathlib.calc_totol(4,5)#function from mathlib.py
#     assert total == 9  #to verify we will use assert statement (9 is the expected o/p)

# def test_calc_multiply():
#     result = mathlib.calc_multiply(10,3)
#     assert result == 30 # expected output


#one way of running this file is:
#to run this go "unit_testing" directory in terminal
#run "python -m pytest"
# it will recursively go into all the files and subdirectories and it is gonna look for any file which
# has test_ prefix and in that file it is going to execute all the tests which has test_ prefix
# in front of the the name of that method
#so output after running "python -m pytest"


# PS C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing> python -m pytest
# ============================================================== test session starts ==============================================================
# platform win32 -- Python 3.9.2, pytest-7.4.3, pluggy-1.3.0
# rootdir: C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing
# collected 2 items                                                                                                                                 

# test_mathlib.py ..                                                                                                                         [100%]

# =============================================================== 2 passed in 0.03s =============================================================== 

#the other way of running this file is
#run "py.test"

# PS C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing> py.test
# ============================================================== test session starts ==============================================================
# platform win32 -- Python 3.9.2, pytest-7.4.3, pluggy-1.3.0
# rootdir: C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing
# collected 2 items                                                                                                                                 

# test_mathlib.py ..                                                                                                                         [100%] 

# =============================================================== 2 passed in 0.02s ===============================================================

#to see detailed o/p use "py.test -v"

# PS C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing> py.test -v
# ============================================================== test session starts ==============================================================
# platform win32 -- Python 3.9.2, pytest-7.4.3, pluggy-1.3.0 -- c:\users\hp\appdata\local\programs\python\python39\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing
# collected 2 items                                                                                                                                 

# test_mathlib.py::test_calc_total PASSED                                                                                                    [ 50%]
# test_mathlib.py::test_calc_multiply PASSED                                                                                                 [100%] 

# =============================================================== 2 passed in 0.01s ===============================================================


#if testing fails, then we can debug with the o/p and change in the code
#there is not only "test_" prefix rule for searching test file, but also others. we need to google for that.







#new lecture
#3rd Lecture
#Pytest: Skip/Run Tests selectively
#Topics : 1) skip tests 2) selectively run tests using their name 3) custom markers
#suppose in test_mathlib, want to skip testing of one of the methods
#for that import pytest and then use decorator pytest.mark.skip()

# import mathlib #importing file which need to be tested
# import pytest

# @pytest.mark.skip(reason="I dont want to run this test at the moment")
# def test_calc_total():#test_ prefix in front of function name
#     total=mathlib.calc_totol(4,5)#function from mathlib.py
#     assert total == 9  #to verify we will use assert statement (9 is the expected o/p)

# def test_calc_multiply():
#     result = mathlib.calc_multiply(10,3)
#     assert result == 30

#output of above code
# PS C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing> py.test -v 
# =============================================================================================================== test session starts ===============================================================================================================
# platform win32 -- Python 3.9.2, pytest-7.4.3, pluggy-1.3.0 -- c:\users\hp\appdata\local\programs\python\python39\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing
# collected 2 items

# test_mathlib.py::test_calc_total SKIPPED (I dont want to run this test at the moment)                                                                                                                                                        [ 50%]
# test_mathlib.py::test_calc_multiply PASSED                                                                                                                                                                                                   [100%]

# ========================================================================================================== 1 passed, 1 skipped in 0.02s ===========================================================================================================






#sometimes we want to skip some tests if it meet certain condition
#in that case we will use "skipif"

# import mathlib 
# import pytest
# import sys
# #for e.x. we would like to skip test, if it meets specific python version

# @pytest.mark.skipif(sys.version_info > (3,5),reason="Python version is greater than 3.5")#skip if python version is > 3.5
# def test_calc_total():#test_ prefix in front of function name
#     total=mathlib.calc_totol(4,5)#function from mathlib.py
#     assert total == 9  #to verify we will use assert statement (9 is the expected o/p)

# def test_calc_multiply():
#     result = mathlib.calc_multiply(10,3)
#     assert result == 30

#output
# PS C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing> py.test -v
# ================================================================================= test session starts =================================================================================
# platform win32 -- Python 3.9.2, pytest-7.4.3, pluggy-1.3.0 -- c:\users\hp\appdata\local\programs\python\python39\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\HP\Desktop\Preparation\Python_Practice\unit_testing
# collected 2 items

# test_mathlib.py::test_calc_total SKIPPED (Python version is greater than 3.5)                                                                                                    [ 50%] 
# test_mathlib.py::test_calc_multiply PASSED                                                                                                                                       [100%] 

# ============================================================================ 1 passed, 1 skipped in 0.02s ============================================================================= 







#suppose we want to run the test, base on the name
#for ex. we want to run those tests which has "multiply" in their name
