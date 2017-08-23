import random

def mainGame():
    options = ["rock", "paper", "scissor"]
    userInput = input("please choose rock paper scissor: ").lower()
    AI = random.choice(options)
    if userInput == "rock" or userInput == "paper" or userInput ==  "scissor":
        if userInput == AI:
            print("Tie")
            replay()
        if userInput == "rock":
            if AI == "paper":
                print("AI wins")
                replay()
        if userInput == "paper":
            if AI == "scissor":
                print("AI wins")
                replay()
        if userInput == "scissor":
            if AI == "rock":
                print("AI wins")
                replay()
    else:
        print("not a valid option")

def replay():
    newgame = input("Would you like to play again(y/n): ").lower()
    if newgame == "y":
        mainGame()
    elif newgame == "n":
        print("Bye")
    else:
        print("Not a valid option")
        replay()


mainGame()
