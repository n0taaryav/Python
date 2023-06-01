#rock papper scissors
import random

choices = ["rock", "paper", "scissors"]

player_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print(f"Player chose {player_choice}.")
print(f"Computer chose {computer_choice}.")

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("Player wins!")
elif player_choice == "paper" and computer_choice == "rock":
    print("Player wins!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("Player wins!")
else:
    print("Computer wins!")
