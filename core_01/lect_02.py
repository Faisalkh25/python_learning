
# string

text = 'faisal'
text[0]
print(text[0])

# ais
print(text[1:4])
# isal
print(text[2:])
print(len(text))  #len() funciton is used to get the length of a string 

# string slicing
name = 'faisal'
# as
# name[1:4:1]
# print(name[1:4:2])
#functions of strings len(), endswith(), startswith(), capitalize(), find(), replace()

a="hello faisal"
print(a)
print(a.capitalize())
print(a.endswith('ala'))
print(a.find('faisal'))
print(a.replace('faisal', 'drishti'))
# print(a) string is immutable

# practise set
# name = input("Enter name: ") + " good afternoon"
# print(name)

letter = '''
      Dear Faisal Khan,
      You are selected!
      28/02/2026
'''
print(letter)

n = input("enter the name: ")
print(f"good afternoon, {n}")

