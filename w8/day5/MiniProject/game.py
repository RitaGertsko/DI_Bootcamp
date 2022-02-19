# Part I - Game.Py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
#   1. get_user_item(self) – Ask the user to select an item (rock/paper/scissors).
#        Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.
#   2. get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function.
#        Use python’s random.choice() function (read about it online).
#   3. get_game_result(self, user_item, computer_item) – Determine the result of the game.
#         Parameters:
#             *user_item – the user’s chosen item (rock/paper/scissors)
#             *computer_item – the computer’s chosen (random) item (rock/paper/scissors)
#             *Return either win, draw, or loss. Where win means that the user has won,
#                 draw means the user and the computer got the same item, and loss means that the user has lost.
#
#   4. play(self) – the function that will be called from outside the class (i.e. from rock-paper-scissors.py). It will do 3 things:
#       1. Get the user’s item (rock/paper/scissors) and remember it
#       2. Get a random item for the computer (rock/paper/scissors) and remember it
#       3. Determine the results of the game by comparing the user’s item and the computer’s item
#             1. Print the output of the game; something like this: “You selected rock. The computer selected paper.
#             You lose”, “You selected scissors. The computer selected scissors. You drew!”
#             2. Return the results of the game as a string: win;draw;loss;, where win means that the user has won,
#             draw means the user and the computer got the same item, and loss means that the user has lost.

import random

class Game:
    game_options = {
        "r": "Rock",
        "p": "Paper",
        "s": "Scissors",
    }

    game_scenarios = {
        ("PaperRock", "RockScissors", "ScissorsPaper"): "Win",
        ("RockPaper", "PaperScissors", "ScissorsRock"): "Loss",
    }

    def __init__(self):
        self.user_choice = ""
        self.computer_choice = ""
        self.game_result = ""

    def get_user_item(self):
        user_input = input("please pick between:\n r (Rock)\n p (Paper)\n s (Scissors)\n >>>")
        while user_input not in Game.game_options.keys():
            print("Wrong Input")
            user_input = input("please pick between:\n r (Rock)\n p (Paper)\n s (Scissors)\n >>>")
        self.user_choice = Game.game_options[user_input]
        return self.user_choice

    def get_computer_item(self):
        self.computer_choice = random.choice(list(Game.game_options.values()))
        return self.computer_choice

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            self.game_result = "Draw"
        else:
            for tup in Game.game_scenarios.keys():
                if (user_item + computer_item) in tup:
                    self.game_result = Game.game_scenarios[tup]
                    break
        return self.game_result

    def play(self):
        print(f"You selected {self.get_user_item()}\nThe computer selected {self.get_computer_item()}\nIt's a {self.get_game_result(self.user_choice, self.computer_choice)}")
        return self.game_result
