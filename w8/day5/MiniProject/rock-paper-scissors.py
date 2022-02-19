# Part II - Rock-Paper-Scissors.Py
# rock-paper-scissors.py : create 3 functions
# get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
# The possibles choices are : Play a new game or Show scores or Quit
#
# print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.
#
#
# Note: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.
#
# main() - the main function. It should take care of 3 things:
# Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)
#
# When the user chooses to play a game:
# Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
# Remember the results of every game that is played.
#
# When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.

from game import Game


def get_user_menu_choice():
    print(
        """menu:
    (p) Play a new game
    (s) Show scores
    (q) Quit"""
    )
    return validate_user_choice()


def validate_user_choice():
    user_choice = input(">>>")
    while user_choice not in ["p", "s", "q"]:
        user_choice = input("Wrong input, try again please:\n>>>")

    return user_choice


# results = { Win: 2, Loss: 4, Draw: 3}

def print_results(results):
    print(
        f"""Game results:
    You won {results["Win"]} times
    You lost {results["Loss"]} times
    You drew {results["Draw"]} times
    
Thank you for playing!""")


def main():
    user_menu_choice = get_user_menu_choice()
    game_result = {"Win": 0, "Loss": 0, "Draw": 0}
    game = Game()
    while user_menu_choice != "q":
        if user_menu_choice == "s":
            print_results(game_result)
        else:
            current_round_result = game.play()
            game_result[current_round_result] += 1
        user_menu_choice = get_user_menu_choice()

    print_results(game_result)


main()
