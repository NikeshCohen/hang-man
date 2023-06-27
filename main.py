from game import init_game
from art import logo

print(logo)
start_game = input("\nWelcome to hangman!\nWould you like to start a new game? (y/n): ")

while start_game.lower() != "y" and start_game.lower() != "n":
    print("\nPlease enter a valid input!")
    start_game = input("Would you like to start a new game? (y/n): ")

if start_game.lower() == "y":
    print("\nAwesome lets get started!")
    init_game()
elif start_game.lower() == "n":
    print("\nOkay, goodbye!")
    quit()
