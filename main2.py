import random

def select_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "strawberry"]  # Add more words as needed
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        display += " "
    return display

def hangman():
    word = select_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word!")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print(display_word(word, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")
            if attempts == 0:
                print("\nGame Over! The word was:", word)
                break
        else:
            if "_" not in display_word(word, guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break

hangman()
