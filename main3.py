import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "melon"]
    return random.choice(words)

def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("The word contains", len(word), "letters.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", guessed_letters)

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You guessed the word correctly!")
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        else:
            guessed_letters.append(guess)
            if guess not in word:
                attempts -= 1
