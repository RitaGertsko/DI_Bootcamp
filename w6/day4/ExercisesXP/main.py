# Exercises XP
# Exercise 1 : Favorite Numbers
# 1. Create a set called my_fav_numbers with all your favorites numbers.
# 2. Add two new numbers to the set.
# 3. Remove the last number.
my_fav_numbers = [1, 2, 3, 4, 5]
new_numbers = [6, 7, 8]

my_fav_numbers.extend(new_numbers)
print(my_fav_numbers)

my_fav_numbers.pop()
print(my_fav_numbers)

# 4. Create a set called friend_fav_numbers with your friend’s favorites numbers.
# 5. Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
friend_fav_numbers = [9, 10, 11, 12, 13]
our_fav_numbers = my_fav_numbers + friend_fav_numbers

print(our_fav_numbers)

# Exercise 2: Tuple Given a tuple which value is integers, is it possible to add more integers to the tuple? No,
# Tuples are immutable lists, it means items can’t be changed.


# Exercise 3: Print A Range Of Numbers
# Use a for loop to print all numbers from 1 to 20, inclusive.

for i in range(1, 21):
    print(i)
    i += 1

# Exercise 4: Floats
# 1. Recap – What is a float? What is the difference between an integer and a float? A float is a
# number with a decimal point or a floating point number. An integer (more commonly called an int) is a number
# without a decimal point.
# Floats are used when more precision is needed.

# 2. Can you think of another way to generate a sequence of floats?
# 3. Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
sequence = " "
i = 1.5
while i <= 5:
    sequence += f"{i} "
    i += 0.5
print(sequence)

# Exercise 5: Shopping List
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

# Exercise 6 : Loop
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = "Rita"
user_name = input("What is you name?:")
while not my_name == user_name:
    user_name = input("What is you name?:")
print("Great!, We have the same name!")

# Exercise 7
# Given a list, use a loop to print out every element which has an even index.

fruits = ["Banana", "Apples", "Oranges", "Blueberries", "strawberries", "pineapple"]
fruits_length = len(fruits)
for i in range(0, fruits_length):
    if i % 2:
        print(fruits[i])

# Exercise 8
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for i in range(1500, 2501):
    if not i % 5:
        print(i)
    elif not i % 7:
        print(i)

# Exercise 9: Favorite Fruits
# 1. Ask the user to input their favorite fruit(s) (one or several fruits).
#     Hint: Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# 2. Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# 3. Now that we have a list of fruits, ask the user to input a name of any fruit.
#     If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
#     If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

user_first_answer = input(
    "What is your favorite fruit or fruits? (If you have several favorite fruits please separate them with a single space):")
user_favorite_fruit_s_list = user_first_answer.split()

user_second_answer = input(
    "give me a name of any one fruit:")

if user_second_answer in user_favorite_fruit_s_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 10: Who Ordered A Pizza ?
# 1. Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# 2. As they enter each topping, print a message saying you’ll add that topping to their pizza.
# 3. Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

customer_selected_topping_list = []
while True:
    user_response = input("enter a pizza topping (one at the time), if you want to stop enter 'quit':")
    customer_selected_topping_list.append(user_response)
    if user_response == "quit":
        customer_selected_topping_list.pop()
        customer_selected_topping_list_length = len(customer_selected_topping_list)
        total = 10 + (2.5 * customer_selected_topping_list_length)
        print(f"you have picked {customer_selected_topping_list_length} toppings and the total cost is ${total}")
        break
    print("you added that topping to your pizza")

# Exercise 11: Cinemax
# 1. A movie theater charges different ticket prices depending on a person’s age.
#      if a person is under the age of 3, the ticket is free.
#      if they are between 3 and 12, the ticket is $10.
#      if they are over the age of 12, the ticket is $15.
# 2. Ask a family the age of each person who wants a ticket.
# 3. Store the total cost of all the family’s tickets and print it out.

prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "
total_cost = 0

while True:
    age = input(prompt)
    if age == 'quit':
        print(f"Your total is: {total_cost}$")
        break
    age = int(age)

    if age <= 3:
        print("  You get in free!")
    elif 3 < age <= 15:
        total_cost += 10
        print("  Your ticket is $10.")
    else:
        total_cost += 15
        print("  Your ticket is $15.")

# 4. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.

permitted_customers = []

while True:
    age = input(prompt)
    if age == 'quit':
        print(f"All people above the following ages can enter: {sorted(permitted_customers)}")
        break
    age = int(age)

    if age <= 21:
        print("  Your not allowed to enter!")
    else:
        permitted_customers.append(age)

# Exercise 12 : Who Is Under 16?
# 1. Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
# 2. At the end, print the final list.
names = ["David", "Rita", "Alex", "Dan", "Shalom", "Lili", "Anastasia"]
prompt = "How old are you?"

for name in names:
    user_answer = input(f"Hi {name}, {prompt}")
    user_answer = int(user_answer)

    if user_answer <= 16:
        names.remove(name)
print(names)

# Exercise 13
# 1. Make a list called sandwich_orders and fill it with the names of various sandwiches .
# 2. Then make an empty list called finished_sandwiches.
# 3. As each sandwich is made, move it to the list of finished sandwiches.
# 4. After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    user_response = input(f"Is the {sandwich} is ready? (yes/no):")

    if user_response == 'yes':
        finished_sandwiches.append(sandwich)
print(finished_sandwiches)

# Exercise 14
# 1. Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# 2. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# 3. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["tuna sandwich", "avocado sandwich", "egg sandwich", "sabih sandwich", "pastrami sandwich",
                   "pastrami sandwich", "pastrami sandwich", "cheese sandwich"]
sandwichOutOfStock = "pastrami sandwich"
finished_sandwiches = []
outOfStockMessage = f"deli has run out of {sandwichOutOfStock}"
print(outOfStockMessage)
for sandwich in sandwich_orders:
    if sandwich == sandwichOutOfStock:
        continue
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
