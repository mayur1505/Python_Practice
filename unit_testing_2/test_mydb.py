#we will write test file here for db.py
# so first test is to verify Jones employee ID and
# the other one is to verify Thoms employee ID 
# so this database is basically a employee database and all we are
# doing is verifying IDs of different employees and we are writing a unit test



# from mydb import MyDB

# def test_johns_id(cur):
#     db = MyDB()  #this will give database object
#     conn = db.connect("server") #connecting to database server
#     curs = conn.cursor() #cursor object
#     id = cur.execute("select id from employee_db where name=John")#cur.execute will be able to execute sql squeries, here it will return id of jhon
#     assert id == 123

# def test_toms_id(cur):
#     db = MyDB()  #this will give database object
#     conn = db.connect("server") #connecting to database server
#     curs = conn.cursor() #cursor object
#     id = cur.execute("select id from employee_db where name=Tom")
#     assert id == 789

#The problem with above approach is 
# 1.we are repeating most of the code
# 2.creating connection with db is costly operation and in above approach 
#we are doing that in every test case and if we have 1000 test cases, then above 
#approach is not feasible

#Two ways to fix above issues,
#1) setup and teardown methods (classic xunit style)
#2) fixtures (recommended)

#1)Setup and teardown method (setup will initialize
#whatever you need for your test cases in the beginning
#and after finishing test cases we will need clean up for that teadown is used)
#this is not so useful so don't learn and don't implement

#2)fixture method
# from mydb import MyDB
# import pytest

# @pytest.fixture()
# def cur():
#     print("setting up")
#     db = MyDB()
#     conn = db.connect("server")
#     curs = conn.cursor()
#     return curs

# #Fixtures leverage a concept of dependancy injection
# #so all the tests have dependency on cursor (cur) and we are injecting that dependency
# #using above fixture by passing cur in test function
# def test_johns_id(cur): 
#     id = cur.execute("select id from employee_db where name=John")
#     assert id == 123

# def test_toms_id(cur):
#     id = cur.execute("select id from employee_db where name=Tom")
#     assert id == 789

#run -> pytest -v --capture=no
#--capture=no for printing the things which we want to print
#no means don't capture the output of print statement somewhere
#else but show it on Stdout

#in o/p we can see "setting up" two time, i.e. at each test case it is creating
#new database object and creating connection with db each time but this is not
#we were expecting, to restrict that we will use scop parameter.
#when scope is equal to module, it will set up only once

from mydb import MyDB
import pytest

@pytest.fixture(scope="module")
def cur():
    print("setting up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close() #for cleaning up resorces after finishing test cases
    conn.close() #for cleaning up resorces after finishing test cases
    print('closing database')
def test_johns_id(cur): 
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789