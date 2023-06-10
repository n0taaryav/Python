import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number correctly!" + "It was "+ random_number + "!")
            return

        attempts -= 1
        print(f"Attempts left: {attempts}")

    print(f"\nGame over! You ran out of attempts. The number was {random_number}.")


number_guessing_game()
