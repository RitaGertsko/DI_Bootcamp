# Daily Challenge: OOP Quizz
# Part 1 : Quizz :
# Answer the following questions
#
# What is a class?
#       class it's a blueprint for creating instances, an idea for how something should be defined.
# What is an instance?
#       instance is a copy of a class with actual values. an object belonging to a specific class.
# What is encapsulation?
#       Encapsulation is the packing of data and functions that work on that data within a single object.
#       By doing so, you can hide the internal state of the object from the outside. This is known as information hiding. A class is an example of encapsulation.
# What is abstraction?
#       Abstraction is used to hide the internal functionality of the function from the users.
#       another idea behind this is to abstract the code to create very general and abstract objects/classes that can address general and abstract instances.
# What is inheritance?
#       As the name suggests, Inheritance is a concept where classes can inherit (or be modified by inheriting) methods and properties from another classes (base class and derived class).
# What is multiple inheritance?
#       It's a big no-no and a bad practice.
#       When a class is derived from more than one base class.
# What is polymorphism?
#       Poly means a lot and Morphism means shapes. essentially it's the ability to having many forms,
#       (i.e. the same class being used for different instances)
# What is method resolution order or MRO?
#       The Method Resolution Order (MRO) defines the class search path used by Python to search for the right method to use in classes having multi-inheritance.


# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.
#
# The requirements are as follows:
#       The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
#       The Deck class :
#               should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
#               should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", '5', "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.suit + ": " + self.value

# Deck will hold "in composition" a list of cards
class Deck:
    def __init__(self):
        self.deck = []

    def shuffle(self):
        self.deck = []
        for suit in Card.suits:
            for value in Card.values:
                self.deck.append(Card(suit, value))
        #          used ans to concat all cards into a string to print
        # ans = ""
        # for card in self.deck:
        #     ans = ans + card.__str__() + ", "
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


deck = Deck()
deck.shuffle()
print(deck.deal())
