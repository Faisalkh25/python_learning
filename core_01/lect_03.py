
# list

nums = [15,52,7,63,99]
print(nums)


# print(nums[2])  #7
# list is mutable 

names = ['faisal', 'drishti', 'abhinav']
print(names)

names.append('shrishti')
print(names)

# mixing fo two lists
mix = [nums, names]
print(mix)
# [[15, 52, 7, 63, 99], ['faisal', 'drishti', 'abhinav', 'shrishti']]
# to get particular value from the list

# mix[0]
# print(mix[0])
# [15, 52, 7, 63, 99]

print(mix[0][1]) 
print(mix[1][2])

# we want all values in one list 
mix = nums + names
print(mix)

# list functions
print(nums)
# [15, 52, 7, 63, 99]

nums.count(7)
# print(nums.count(7))  #count of value 7 is 1

nums.insert(2,77)
print(nums.insert(2,77))
print(nums)
# [15, 52, 77, 77, 7, 63, 99]
nums.insert(1,63)
print(nums)
# [15, 63, 52, 77, 77, 7, 63, 99]
nums.insert(7,100)
print(nums)
# [15, 63, 52, 77, 77, 7, 63, 100, 99]

nums.reverse()
print(nums)

nums.remove(77)
print(nums)
# [99, 100, 63, 7, 77, 52, 63, 15]

 # to check and remove a value (first in last out)
# nums.pop() 

print(nums)
# [99, 100, 63, 7, 77, 52, 63]

print(nums.pop(5))
# 52
print(nums)
# [99, 100, 63, 7, 77, 63, 15] 52 removed

# python built in funcitons
# max, min

print(max(nums))
# 100

# similarly on string
print(min(names))
# abhinav