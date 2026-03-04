
# variable storage in python
a = 5
b=5
print(id(a))
# 140736463590440
print(id(b))
# 140736463590440 
# so inthis case variable b refers to the box a wich has same value 5 that is why 
# bith address are same because b is referring to the address of a (box)

# now when i change the value of b it will have new address 

b = 9
print(id(b))
# 140736440456360 
# python sees that 9 is not existing so it created new box which has new address
# and its variable name is b 

# b=5 now this is not referring to any box or variable so it is wastage and it will be removed
# withthe help of garbage collection

#All this process is called string interning

# but it wont work with long strings or large numbers
str = "my name is faisal khan and i am a software developer"
str1 = "my name is faisal khan and i am a software developer"


print(id(str))
# 2469761410768
print(id(str1))
# 2197014210256


