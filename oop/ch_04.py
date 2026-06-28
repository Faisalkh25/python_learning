# _init_ contructor
'''
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

'''
class Employee:

    city = "lucknow"

    def __init__(self, name, city, language):
        self.name = name
        self.city = city
        self.language = language
        print("this is init method")

    @staticmethod
    def greet():
        print("Hello Everyone")

e = Employee("faisal", "delhi", "java")
# e.name = "faisal"
# e.language ="java"
e.greet()
print(e.name, e.city, e.language )