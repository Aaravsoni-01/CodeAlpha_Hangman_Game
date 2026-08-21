"""
Hangman Game
------------
A simple text-based Hangman game.
Key Concepts used: Random, while loop, if-else, Strings, Lists
"""

import random
# Predefined list of 30 words (4 to 10 letters)
WORD_LIST = [
    "code", "game", "list", "word",          # 4 letters
    "apple", "chair", "plane", "brain",      # 5 letters
    "python", "guitar", "monkey", "orange",  # 6 letters
    "diamond", "penguin", "rainbow", "reading",   # 7 letters
    "keyboard", "elephant", "mountain", "sunshine",  # 8 letters
    "astronaut", "butterfly", "chocolate", "dangerous",  # 9 letters
    "basketball", "playground", "understand", "helicopter", "watermelon"  # 10 letters
]

MAX_INCORRECT_GUESSES = 6


def choose_word():
    """Randomly select a word from the word list."""
    return random.choice(WORD_LIST)


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def display_hangman(incorrect_guesses):
    """Return an ASCII hangman drawing based on number of wrong guesses."""
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    return stages[incorrect_guesses]


def play_hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 40)
    print("       WELCOME TO HANGMAN!")
    print("=" * 40)
    print(f"The word has {len(word)} letters. Try to guess it!")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(display_hangman(incorrect_guesses))
        print("Word: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        print("Guessed letters: " + ", ".join(guessed_letters) if guessed_letters else "Guessed letters: None")

        guess = input("\nGuess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid input. Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"\nYou already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"\nGood guess! '{guess}' is in the word.\n")
            # Check if player has won
            if all(letter in guessed_letters for letter in word):
                print(display_hangman(incorrect_guesses))
                print("Word: " + display_word(word, guessed_letters))
                print(f"\nCongratulations! You guessed the word: '{word}'")
                print("You win!")
                break
        else:
            incorrect_guesses += 1
            print(f"\nSorry, '{guess}' is not in the word.\n")
    else:
        # This runs if the while loop exits because incorrect_guesses == MAX_INCORRECT_GUESSES
        print(display_hangman(incorrect_guesses))
        print(f"\nGame Over! You've run out of guesses.")
        print(f"The word was: '{word}'")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        print()

    print("Thanks for playing Hangman! Goodbye.")


if __name__ == "__main__":
    main()