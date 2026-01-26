import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock,paper,scissors) : ")

    computer_choice = random.choice(options)

    choices = {"Player": player_choice, "Computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    
    
    if player == computer:
        return "Its a tie"

    elif player.lower() == "rock":
        if computer.lower() == "scissors":
            return "Rock smashes scissors, YOU WIN!"
        elif computer.lower() == "paper":
            return "Paper cover rock, You lose"

    elif player.lower() == "paper":
        if computer.lower() == "scissors":
            return "Scissor cuts paper, You lose"
        elif computer.lower() == "rock":
            return "Paper cover rock, YOU WIN!"
        
    elif player.lower() == "scissors":
        if computer.lower() == "paper":
            return "Scissors cuts paper, YOU WIN!"
        elif computer.lower() == "rock":
            return "Rock smashes scissors, You lose"
    
choices = get_choices()
p_choice = choices["Player"]
c_choice = choices["Computer"]

result = check_win(p_choice,c_choice)

print(result)


        
    
