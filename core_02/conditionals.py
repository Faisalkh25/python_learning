
# if else

# a = int(input("enter your age: "))

# if(a>=18):
#     print("you are eligible to drive a vehicle")

# else:
#     print("you are not eligible")    

# print("end of program")    

# if elif
# a = int(input("enter your age: "))

# if(a%2==0):
#     print("age is even")

# if(a>=18):
#     print("you are eligible to drive a vehicle")

# elif(a <=0 or a>105):
#     print("please enter valid age")    

# else:
#     print("you are not eligible")    

# print("end of program")  


# problem 1
# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# c = int(input("enter the third number: "))
# d = int(input("enter the fourth number: "))

# if(a>b and a>c and a>d):
#     print("greatest numebr is: ", a)

# elif(b>a and b>c and b>d):
#     print("greatest numebr is: ",  b)

# elif(c>a and c>b and c>d):
#     print("greatest numebr is: ",  c)

# else:
#     print("greatest numebr is: ",  d)  

# print("end of the program")      

# problem 2

# maths = int(input("enter the marks: "))
# computer = int(input("enter the marks: "))
# physics = int(input("enter the marks: "))

# total_percent = (100*(maths + computer + physics))/300


# if(total_percent >=40 and  maths >= 33 and physics >= 33 and computer >= 33):
#     print("passed")

# else:
#     print("faileed")        


# problem 3

# a = "Subscribe now"
# b= "make money"
# c = "click this"
# d = "buy this"

# inp = input("enter the comment")

# if(a in inp or b in inp or c in inp or d in inp):
#     print("this comment is a scam")

# else:
#     print("it is not a scam")    

# problem 4

# l = ["faisal", "ashu", "abhinav", "drishti"]

# i = input("enter the name: ")

# if(i in l):
#     print("your name is in the list.")

# else:
#     print("your name is not in the list") 

# problem 5
# check if there is 'faisal' in the sentence 

a = input("enter the string: ")   

if('faisal'.lower() in a.lower()):
    print("faisal is in the sentence.")

else:
    print("faisal is not in the sentence")    