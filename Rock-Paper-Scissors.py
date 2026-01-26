import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock,paper,scissors) : ")

    computer_choice = random.choice(options)

    choices = {"Player": player_choice, "Computer": computer_choice}
    print(choices)

    if player_choice.lower() == computer_choice.lower():
        return "Draw"

    elif player_choice.lower() == "rock" and computer_choice.lower() == "paper" or player_choice.lower() == "paper" and computer_choice.lower() == "scissors" or player_choice.lower(    ) == "scissors" and computer_choice.lower() == "rock":
        return "Computer wins"

    elif player_choice.lower() == "paper" and computer_choice.lower() == "rock" or player_choice.lower() == "rock" and computer_choice.lower() == "scissors" or player_choice.lower() == "scissors" and computer_choice.lower() == "paper":
        return "Player wins"


while True:
    ch = input("Do you want to play more ? (Y/N): ")
    if ch.upper() == "Y":
        choices = get_choices()
        print(choices)
    elif ch.upper() == "N":
        print("Thanks for playing...")
        break
    else:
        print("Please choose a valid choice")
