import random
'''
 1 for snake
 2 for gun
 3 for water
'''

computer = random.choice([1,2,3])
userInput = int(input("enter your choice: "))
userDict = {1: 'snake', 2: 'gun', 3: 'water'}

user = userInput

print(f"computer chose: {userDict[computer]}")
print(f"you chose: {userDict[userInput]}")

if(computer == user):
    print("its a draw")

else:
    if(computer == 1 and user == 2):
        print("you win")

    elif(computer == 1 and user == 3):
        print("comnputer wins")

    elif(computer == 2 and user == 1):
        print("computer wins")

    elif(computer == 2 and user == 3):
        print("you win")

    elif(computer == 3 and user == 1):
        print("you win")

    elif(computer == 3 and user == 2):
        print("computer wins")

    else:
        print("somwthing went wrong")

