#we will learn powerfull feature "fixtures" of pytest fixtures

#we will create a mock(fake) database for demo purpose of fixtures
# but if you are using any real Python module for let's say Oracle or SQL database it will have
# all these basic functionality it will have your database object will have your
# connection and then the third thing will be cursor so cursor will have an ability
# to execute your database queries
class MyDB:
    def __init__(self):
        self.connection = Connection()

    def connect(self, connection_string):
        return self.connection

class Connection:
    def __init__(self):
        self.cur = Cursor()

    def cursor(self):
        return self.cur

    def close(self):
        pass

class Cursor():
    def execute(self, query):
        if query == "select id from employee_db where name=John":#here we have some put some fixed database queries 
            return 123 #returning some fixed values
        elif query == "select id from employee_db where name=Tom":
            return 789
        else:
            return -1

    def close(self):
        pass

#in test_db.py 
#we will write two unit tests
#1) To verify John's employee id
#2) To verify Tom's employee id
