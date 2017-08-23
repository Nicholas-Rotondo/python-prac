import random

def mainGame():
    options = ["rock", "paper", "scissors"]
    userInput = input("please choose rock paper scissor: ")
    userInput.lower()
    AI = random.choice(options)
    if userInput == "rock":
        if AI == "paper":
            print("AI wins")
        else:
            print("User Wins")
    if userInput == "paper":
        if AI == "scissors":
            print("AI wins")
        else:
            print("User Wins")
    if userInput == "scissors":
        if AI == "rock":
            print("AI wins")
        else:
            print("User Wins")




mainGame()
