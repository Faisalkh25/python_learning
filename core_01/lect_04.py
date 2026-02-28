# tuple
# tuple are similar like list but it is immutable and syntax is different as from list

tup = [24,53,96,42,15]
print(type(tup))
# <class 'list'>

# to declare tup we do not need [] sqaure brackets,instead we need no brackets or () 

tupA = 1,5,6,8
print(type(tupA)) 
# <class 'tuple'> 

tupB = (2,5,8,6,4)
print(type(tupB))
# <class 'tuple'>

tupMix = (29, 'faisal', 23.6)
tupMix.count(29)
print(tupMix.count(29))
# 1



# you can also store the list inside the tuple eg =
tupC = (29, 'faisal', 26.5, [2,5,9,4,3])
print(tupC)
# (29, 'faisal', 26.5, [2, 5, 9, 4, 3])
# now in this you can change the value or particular element in the list with other value

# change 5 to 7
tupC[3][1] = 7
print(tupC)
# (29, 'faisal', 26.5, [2, 7, 9, 4, 3])

# now if you try to change the another value except list's value you will get error
# tupC[0] = 15
# print(tupC)
#  Traceback (most recent call last):
#   File "c:\python_lect\core_01\lect_04.py", line 38, in <module>
#     tupC[0] = 15
#     ~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# practise set

fruits = []
f1 = input('enter the fruits: ')
fruits.append(f1)

f2 = input('enter the fruits: ')
fruits.append(f2)

f3 = input('enter the fruits: ')
fruits.append(f3)

f4 = input('enter the fruits: ')
fruits.append(f4)

f5 = input('enter the fruits: ')
fruits.append(f5)

f6 = input('enter the fruits: ')
fruits.append(f6)

print(fruits)

# problem 2





