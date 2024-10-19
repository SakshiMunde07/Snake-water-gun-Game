import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr =  input("Enter your choice: ")
youDict = {"s": 1, "w":-1, "g":0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

#By now we have 2 numbers(variables), you and computer

print(f"You chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if(computer== you):
    print("Its a draw")
else:
    if (computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    else:
        print("Something is wrong!")

