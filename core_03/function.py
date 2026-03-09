# function is used to perform a similar task or repeated task with the help of fucniton
# It is a block of code that runs when called

# def avg():
#     a = int(input("enter the number: "))
#     b = int(input("enter the number2: "))
#     r = (a+b)/2
#     print(r)

# avg()
# avg()

# function with argument

def goodDayUser(name):
    s = name
    print("good morning, " + s)

goodDayUser("drishti")

# recursion - > A funciton that calls itself is called a recursion.

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("enter the number: "))
# print(f"The factorial of a number is: {factorial(n)}")      

# problems
# p1 wap using functions to find the greatest of three numbers

# def greatestNumbers(a,b,c):
#     if(a>=b and a>=c):
#         return a
#     elif(b>=a and b>=c):
#         return b
#     elif(c>=a and c>=b):
#         return c
    
# print(greatestNumbers(15,15,7))

# p2 wap to print forst n natural numbers using recursion function

def rec_natural(n):
    if(n<=0):
        return 0
    return n + rec_natural(n - 1)

print(rec_natural(5))
