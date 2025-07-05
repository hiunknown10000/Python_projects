'''
logic:
stone=1
paper=2
scissor=3
match: compInput = userInput
'''

import random


print("Lets make a challenge\n\tStone_Paper_Scissor game:\n")
user=input("Enter your choice(Stone/Paper/Scissor): ")
user=user.lower()
if not(user=="stone" or user=="paper" or user=="scissor"):
    print("Opps! wrong choice")
    exit()

# Library
lab={"stone":1, "paper":2, "scissor":3}
revlab={1:"stone", 2:"paper", 3:"scissor"}

# Computer and User input
compInput=random.choice([1,2,3])
userInput=lab[user]

#Output
print(f"You choose:- {user.capitalize()}")
print(f"Computer choose:- {revlab[compInput].capitalize()}")

# Game output
'''
if (compInput==userInput):
    print("Draw!")
else:
    if(compInput==1 and userInput==2):
        print("You are WIN")
    elif(compInput==1 and userInput==3):
        print("You are Lose")
    elif(compInput==2 and userInput==1):
        print("You are Lose")
    elif(compInput==2 and userInput==3):
        print("You are WIN")
    elif(compInput==3 and userInput==2):
        print("You are Lose")
    elif(compInput==3 and userInput==1):
        print("You are WIN")
    else:
        print("Something went wrong :(")
'''

# Using (compInput-userInput) logic
ans= compInput - userInput
if (ans== -1 or ans==2):
    print("You are WIN")
elif(ans==-2 or ans== 1):
    print("You are Lose")
else:
    print("Something went wrong")