import random
from words import words_list
from art import stages


def init_game():
    random_word = random.choice(words_list)
    word_len = len(random_word)
    lives = 7
    display = []
    guessed_letters = []
    end_game = False

    for letter in random_word:
        display += "_"

    # # TESTING
    # print(f"\nThe word is {random_word}\n")

    print(f"The word contains {word_len} letters:")

    for x in display:
        print(x, end="")

    # Code to run the game
    while not end_game:
        # Ask the user to enter a guess
        while "_" in display:
            guess = input(
                f"\n\n\n\nYou have {lives} lives remaining\nGuess a letter from the word: "
            ).lower()

            while guess in guessed_letters:
                guess = input(
                    f"\n\nYou have already guessed {guess}\nGuess another letter: "
                ).lower()

            guessed_letters += guess

            # Check if the users guess in the word generated
            if guess in random_word:
                print(f"\n{guess} is in the word!")
                print(stages[lives])

                # Enumerate through the letters and replace it with the users guess
                for index, letter in enumerate(random_word):
                    if letter == guess:
                        display[index] = letter

                for x in display:
                    print(x, end="")

            # if the guess in not in the word generated
            else:
                print(f"\n{guess} is not in the word!")
                lives -= 1

                if lives == 0:
                    print(f"You loose! The correct word was {random_word}")
                    print(stages[0])
                    quit()
                else:
                    print(stages[lives])

                    for x in display:
                        print(x, end="")

        print("\n\nWell done! You guessed the word correctly!")
        end_game = True
