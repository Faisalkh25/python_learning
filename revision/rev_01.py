# 1 
'''
def CheckEvenOdd(a):
    if a%2 == 0:
       return f"{a} is a even number"
    else:
       return f"{a} is a odd number"
'''


# print(CheckEvenOdd(6))

# 2 Create a function that accepts a list of numbers and returns the sum.
'''
def sumOfList(numbers):
    total=0
    for i in numbers:
        total += i

    return total
print(sumOfList(numbers = [10,20,30,40,50]))
'''

# Write a function that returns the largest number from a list.
'''
def largestNumber(nums):
    max=nums[0]
    
    for i in nums:
        if i> max:
            max =i

    return max

print(largestNumber(nums=[5,12,3,18,7,45]))
'''

# 4 Count Even Numbers, nums = [2, 5, 8, 11, 14, 17]
'''
def CountEvenNums(nums):
    count=0
    even_nums= []
    for i in nums:
        
        if i % 2 == 0:
            count += 1
            even_nums.append(i)

    return count,even_nums

print(CountEvenNums(nums=[2, 5, 8, 11, 14, 17]))

'''

# 5 Remove Duplicates, nums = [1, 2, 2, 3, 4, 4, 5]

'''
nums = [1, 2, 2, 3, 4, 4, 5]
a = set(nums)
print(a)
'''






        




