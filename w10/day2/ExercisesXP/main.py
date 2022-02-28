# Exercises XP
# Exercise 1

# import my_function
# from my_function import add_person
# from my_function import add_person as add
# import my_function as fun

# Exercise 2
import random

def random_one_to_hundred():
    while True:
        user_num = int(input("Please insert a number between 1 to 100:\n>>>"))
        if 1 <= user_num <= 100:
            print(f"your number: {user_num}")
            comp_num = random.randint(1, 100)
            print(f"computer number is:{comp_num}")
            if user_num == comp_num:
                print("Success!, your number and the computer number are matching")
            else:
                print("Sorry!, your number and the computer number are not matching")
                continue
            break
        else:
            print("it's not a number between 1 and 100, try again!")
            continue


# random_one_to_hundred()

# Exercise 3
import string

num = 5
result = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(num))
print(f"Generate random String of {num} letters: {result} ")
