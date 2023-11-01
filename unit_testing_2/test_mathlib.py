# import mathlib

#supply multiple inputs and you check if those inputs are producing the expected output or no

# def test_calc_square_1():
#     result=mathlib.calc_square(5)
#     assert result==25

# def test_calc_square_2():
#     result=mathlib.calc_square(9)
#     assert result==81

# def test_calc_square_3():
#     result=mathlib.calc_square(10)
#     assert result==100


#the problem with above appraoch is that there is repetition/duplication of code
#below is better way
import mathlib
import pytest
@pytest.mark.parametrize("test_input, expected_output",[
    (5, 25),
    (9, 81),
    (10, 100) 
])#pytest decorator that you need to use whenever you want to parameterize your test cases. Inside we have passed tuples
def test_calc_square(test_input, expected_output):
    result=mathlib.calc_square(test_input)
    assert result == expected_output

#for running -> pytest -v
#we should use this method when we see similarity between test cases
