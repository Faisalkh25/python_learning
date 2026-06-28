class Employee:
    language = ["java", 'python', "javascript"]
    salary = 1200000

    # functions inside class
    def getSalary(self):
        print(f"the salary of the employee is: {self.salary}")

faisal = Employee()
# print(faisal.language, faisal.salary)
faisal.getSalary()
# Employee.getSalary(faisal)