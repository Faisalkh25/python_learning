# p1
# multiplication of 6

# n = int(input("enter the number: "))

# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")

#greet all member in the list l and which starts with s

# l = ['faisal', 'drishti', 'shubham', 'shrishti', 'soha']

# for s in l:
#     if(s.startswith('s')):
#      print(f"Hello {s}")

# wap to find the prime no or not

# n = int(input("enter a number: "))
# for i in range(2, n):
#     if(n%i==0):
#         print(i)
#         print("no is not prime.")
#         break
# else:
#     print("no is prime")    

# num = int(input("enter the number: "))

# for i in range(2, num+1):
#     isPrime = True

#     for n in range(2, i):
#         if i%n==0:
#             isPrime = False
#             break
#     if isPrime:
#         print(i)    

# prob 3
# sum of n natural number

# nu = int(input("enter the number: "))

# i=1
# sum=0

# while(i<=nu):
#     sum += i
#     i += 1

# print(sum)    

# factorial of a number
# 5! = 5*4*3*2*1

# num = int(input("enter the factorial of a number: "))

# fact = 1
# for i in range(1, num+1):
#     fact *= i
   
# print(f"the factorial of a number is: {fact}")   

# prob 4

'''
  *
 ***
*****

'''

# n = int(input('enter the number: '))

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("")

# prob 5

'''
*
**
***
'''

# n = int(input("enter the number: "))

# for i in range(1, n+1):
   
#     print("*" * i, end="")
#     print("")

# prob 6:

'''
***
* *
***
'''
# n = int(input("enter the number: "))

# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*", end="")
#         print(" " * (n-2), end="")
#         print("*", end="")  
#     print("")      
    
# function

def add(a,b):
    x=a
    y=b
    r=a+b
    print(r)

add(5,6)    
add(6,6)  
add(20,20)  
add(150,150)  
add(30,30)