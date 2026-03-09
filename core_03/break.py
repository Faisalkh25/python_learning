# break statement:
#  it is used tocome out of the loop when encountered. It instruct the program to come out of the loop

for i in range(0,20):
    print(i)
    if i==7:
     break

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7  

# 7 is included because print fucntion is called first before the break

for i in range(30):
   if(i==6):
      break
   print(i)

# 0
# 1
# 2
# 3
# 4
# 5

# continue -> it skips the iteration andthen continues the itereation

for i in range(20):
   if(i==5):
      continue
   print(i)

#  0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19

# pass statement: It is used to do nothing. It is sa null statement

for i in range(20):
   pass


for i in range(5):
   print(i)

