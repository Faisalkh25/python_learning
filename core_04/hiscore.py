import random
# prob 2

def hiscore():
    print("you are playing game.")
    score = random.randint(1,101)
    #    fetch score
      
    with open("c:/python_lect/core_04/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score is {score}")
    if(score>hiscore):
        with open("c:/python_lect/core_04/hiscore.txt", "w") as f:
            f.write(str(score))
    return score



hiscore()