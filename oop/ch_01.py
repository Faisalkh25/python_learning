
class Employee:
    language = "python"  #class attribute - it belongs to the class itself
    salary = 1200000

aman = Employee()
aman.language = "java" #instance attribute - it belongs to the object rather than class
# instance attribute get the preference before class attribute

print(aman.language, aman.salary)