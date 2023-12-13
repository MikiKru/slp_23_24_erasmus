# function
def say_hello():
    print("hello")

# Class - a template for objects -> fields(oth. objects), methods
# Object - an instance of the class

# class definition
class User:
    def __init__(self, name, lastname, status, grades): # constructor -> special method that initialize the objects
        self.name = name                                # for class field named name assign value from the parameter name
        self.lastname = lastname
        self.status = status
        self.grades = grades
    def set_status(self, status):                       # setters -> doesn't return values, has one param
        self.status = status
    def get_name(self):                                 # getters -> return value, has no params
        return self.name
    def set_grades(self, grades):
        self.grades = grades
    def add_grade(self, grade):
        self.grades.append(grade)
    def __del__(self):
        print("Object is kiled!!!")
    def __str__(self):                                  # to string method
        return "Name: " + self.name + "\n"+ "Lastname: " + self.lastname + "\n" + "Status: " + str(self.status) + "\n" + "Grades: " + str(self.grades) + "\n"


# objects -> object name
user1 = User("Michal", "Kru", True, [3, 4, 5])      # object type User -> is using default constructor
user2 = User("X", "Y", False, [])
# function call
# say_hello()
# method (function in the User class)
# print(type(user1))
print(user1.__str__())
print(user2)
user2.set_status(True)
print(user2)
print(user2.get_name())
user2.set_grades([3, 3, 3])
print(user2)
user2.add_grade(5)
print(user2)
# del(user2)                  # delete an object
# print(user2)                # no access to the obj user2





