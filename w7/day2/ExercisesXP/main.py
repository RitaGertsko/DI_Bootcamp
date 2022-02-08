# Exercises XP
# Exercise 1 : What Are You Learning ?
# 1. Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# 2. Call the function, and make sure the message displays correctly.
def display_message():
    print("Hi! Im learning Full-Stack!")


display_message()


# Exercise 2: What’s Your Favorite Book ?
# 1. Write a function called favorite_book() that accepts one parameter called title.
# 2. The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# 3. Call the function, make sure to include a book title as an argument when calling the function.
def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("Lord of the rings")


# Exercise 3 : Some Geography
# 1. Write a function called describe_city() that accepts the name of a city and its country as parameters.
# 2. The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# 3. Give the country parameter a default value.
# 4. Call your function.
def describe_city(city, country="Israel"):
    print(f"{city} is in {country}")


describe_city("Yoqneam illit", "Israel")

# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random


def randomNumberGenerator():
    userNumber = int(input("please give me a number between 1 to 100:"))
    computerNumber = random.randint(1, 100)

    while userNumber < 1 or userNumber > 100:
        userNumber = int(input("it's not a valid number, please try again:"))

    if userNumber == computerNumber:
        print("Success!, the number you gave and the number the computer gave are the same number!")
    else:
        print("No luck...the number you gave and the number the computer gave do not match")

    print(f"your number: {userNumber}, the computer number: {computerNumber}")


randomNumberGenerator()


# Exercise 5 : Let’s Create Some Personalized Shirts !
# 1. Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# 2. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# 3. Call the function make_shirt() using positional arguments to make a shirt.
# 4. Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# 5. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


def make_shirt(size, message):
    print(
        f'The size of the shirt you choose is {size.upper()}, and the massage you`ve writen is: "{message.capitalize()}".')


make_shirt("l", "message")


def make_shirt(size="L", message="I love Python"):
    print(
        f'The size of the shirt you choose is {size.upper()}, and the massage you`ve writen is: "{message.capitalize()}".')


make_shirt()
make_shirt("l", "message")
make_shirt("m", "im not so sure of that")


def make_shirt(size, message):
    print(
        f'The size of the shirt you choose is {size.upper()}, and the massage you`ve writen is: "{message.capitalize()}".')


make_shirt(message="I love Python", size="L")

# Exercise 6 : Magicians
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.
magicians_names = ["Gandalf", "Saroman", "Galadriel", "Wanda", "Dumbledore", "Harry Potter", "Dr.Strange"]


def show_magicians(li):
    for element in li:
        print(element)


show_magicians(magicians_names)


def make_great(li):
    for i in range(len(li)):
        li[i] = "the great " + li[i]
        print(li[i])


make_great(magicians_names)
show_magicians(magicians_names)
