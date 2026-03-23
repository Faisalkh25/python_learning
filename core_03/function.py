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

#p3 
'''
***
**
*
'''

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(5)       

# p4 convert inches to cms
# cm = inches * 2.54

# def i_to_cms(n):
#     cm = float(n * 2.54)
#     print(cm)

# n = int(input("enter the inches number: "))
# i_to_cms(n)

# p6
# wa python fucntion to remove a given word from a list and and stip it at the same time

# def rem(l, word):
#     n=[]
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n


# l = ['shubham', 'faisal', 'rohan', 'ahaan', 'waghan', 'an']
# print(rem(l, "an"))


# print prime number using function

# def prime(n):
#     if(n<=1):
#         print("number is not a prime number")
#         return
#     for i in range(2, n):
#         if(n%i == 0):
#             print(f"the {n} is not a prime number")
#             return
#     print(f"the {n} is a prime number")

# n = int(input("enter the number: "))
# prime(n)

# fibonacci series

# def febonacci(n):
#     if(n<=0):
#         return 0
#     f = 0
#     s = 1
#     for i in range(n):
#         print(f, end="")                            
#         fib = f+s
#         f=s
#         s=fib
    

# n = int(input("enter the number: "))
# febonacci(n)



