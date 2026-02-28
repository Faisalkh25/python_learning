
# Set => a set is used to store elements with unique values and it is unordered.
# set is not indexed which means you cannot get value from the set like list s[2]

s = {5,8,3,1,45}
print(type(s))
# <class 'set'>

print(s) 

set1 = {}
print(type(set1))
# <class 'dict'>  so when you try to declare an empty set you will get dictionary type insetead of set

# to declare the set we need to use fuvntion set()

set2 = set()
print(type(set2))
# <class 'set'>

set1 = set('a,f,j,t,h,o,n')
set2 = set('a,e,i,o,u,p,z')

print(set1 - set2)
# {'n', 't', 'j', 'h', 'f'} 
# now here characters from set1 is removed if the characters of set1 is present in set2

print(set2 - set1)
# {'e', 'z', 'p', 'i', 'u'}

print(set1 | set2)
# {'h', 'i', ',', 'e', 'j', 't', 'z', 'u', 'p', 'n', 'o', 'a', 'f'}

print(set1 & set2)
# {'a', 'o', ','} you will get the common values

# union and intersection methods in set
s1 = {1,5,8,3}
s2 = {6,7,9,3}
print(s1.union(s2))
# {1, 3, 5, 6, 7, 8, 9}

print(s1.intersection(s2))
# {3}  prints only common value from both sets

# Dictionary

# dict is a key value pair. keys are the set and values can be list,set,tuple and dict

dic = {'faisal': 86, 'drishti': 68, 'abhinav': 78}
print(dic)
# {'faisal': 86, 'drishti': 68, 'abhinav': 78}

print(dic['faisal'])
# 86

# print(dic['fais'])

#  Traceback (most recent call last):
#   File "c:\python_lect\core_01\lect_05.py", line 47, in <module>
#     print(dic['fais'])
#           ~~~^^^^^^^^
# KeyError: 'fais'

# we can also get the values from the dict using in built function get()
print(dic.get('faisal'))
# 86

# we can also give message if we do not know the value is present or not in the dict

print(dic.get('fais'))
# None

# it will not give error but it prints none. we ccan change the message

print(dic.get('fais', 'not found'))
# not found

dic1 = {'faisal' : 'java',
        'core-java' : ['oops', 'collection', 'exception'],
        'course': {'frontend': 'React', 'backend': 'SpringBoot'}}

print(dic1)
# {'faisal': 'java', 'core-java': ['oops', 'collection', 'exception'], 'course': {'frontend': 'React', 'backend': 'SpringBoot'}}

print(dic1['core-java'])
# ['oops', 'collection', 'exception']

print(dic1['core-java'][1])
# collection

print(dic1['course']['backend'])
# SpringBoot

# It is mutable, unordered and can have only unique keys example-

marks = {'faisal' : 100, 'kashish': 70, 'shubham': 70, "faisal": 85}
print(marks)
# {'faisal': 85, 'kashish': 70, 'shubham': 70}

marks = {5 : 100, 1: 70, 2: 70, 3 : 85}
print(marks)


print(marks.pop(5))
# 100

print(marks)
# {1: 70, 2: 70, 3: 85}

#problems

words = {'paisa' : 'money', 'madad' : 'help', 'kursi' : 'chair'}

# word = input("enter the word: ")
# print(words[word])

numbers = set()
# n1 = int(input("enter the number: "))
# n2 = int(input("enter the number: "))
# n3 = int(input("enter the number: "))
# n4 = int(input("enter the number: "))
# n5 = int(input("enter the number: "))
# n6 = int(input("enter the number: "))
# n7 = int(input("enter the number: "))
# numbers.add(n1)
# numbers.add(n2)
# numbers.add(n3)
# numbers.add(n4)
# numbers.add(n5)
# numbers.add(n6)
# numbers.add(n7)

print(numbers)

# problem 3
se = set()
se.add(15)
se.add(15.0)
se.add("15")

print(se)
print(len(se))

# problem 4

# dict = {}

# n1 = input("enter the name: ")
# f1 = input("enter the language: ")
# dict.update({n1:f1})

# n2 = input("enter the name: ")
# f2 = input("enter the language: ")
# dict.update({n2:f2})

# n3 = input("enter the name: ")
# f3 = input("enter the language: ")
# dict.update({n3:f3})

# n4 = input("enter the name: ")
# f4 = input("enter the language: ")
# dict.update({n4:f4})

# print(dict)


# s = {8,7,12,"Faisal", [1,2]}
# can you change the values inside a list which is contained in set s
# No..because in set we cannot include list and set is not indexed
# Traceback (most recent call last):
#   File "c:\python_lect\core_01\lect_05.py", line 167, in <module>
#     s = {8,7,12,"Faisal", [1,2]}
#         ^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'

lis = [1,5,3,6]
print(lis[2])






 

