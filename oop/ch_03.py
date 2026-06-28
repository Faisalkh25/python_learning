# static method
# sometimes we need a funcituon that does use the self parameter. we dont need to give object 

class Employee:

    name = "faisal"
    city = "lucknow"

    @staticmethod
    def greet():
        print("Hello everyone")

e = Employee()
e.greet()