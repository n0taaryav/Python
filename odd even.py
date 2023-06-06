import random

def play_game():
    player_choice = input("Choose odd or even: ").lower()
    while player_choice not in ['odd', 'even']:
        print("Invalid choice. Please choose odd or even.")
        player_choice = input("Choose odd or even: ").lower()
    
    player_number = int(input("Choose a number between 1 and 10: "))
    while player_number < 1 or player_number > 10:
        print("Invalid number. Please choose a number between 1 and 10.")
        player_number = int(input("Choose a number between 1 and 10: "))

    computer_number = random.randint(1, 10)
    print(f"Computer chose {computer_number}.")

    total = player_number + computer_number
    if total % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    
    if result == player_choice:
        print("You win!")
    else:
        print("You lose!")

