# Exercise 1: Hello World
print("Hello World, " * 4)


# Exercise 2: Some Math
num1 = 99 * 99 * 99
num2 = 8
calculator = num1 * num2
print(calculator)
# or
# calculator2 = (99 * 99 * 99) * 8
# print(calculator2)


# Exercise 3: What Is The Output?
# 5 < 3           prediction: False
# 3 == 3           prediction: True
# 3 == "3"           prediction: False
# "3" > 3           prediction: Error
# "Hello" == "hello"           prediction: False


# Exercise 4: Your Computer Brand
computer_brand = "ASUS"
print(f"I have a {computer_brand} computer")


# Exercise 5: Your Information
name = "Rita"
age = 27
shoe_size = 39
info = f"My name is {name} I am a {age} years old and my shoe size is {shoe_size}"
print(info)


# Exercise 6: A & B
# a = 2
a = 7
b = 5

if a > b:
    print("Hello World")
else:
    print("damnnn a is not bigger than b")


# Exercise 7: Odd Or Even
user_answer = int(input("please give me a number! only number!:"))

if not user_answer % 2:
    print("it`s an even number")
else:
    print("it`s an odd number")


# Exercise 8: What’s Your Name ?
my_name = "Rita"
user_name = input("what is your name?:")

if my_name == user_name:
    print("We have the same name!! LOL")
else:
    print("Damn! Your name is Cute! and My name is Rita")


# Exercise 9: Tall Enough To Ride A Roller Coaster
# Write code that will ask the user for their height in *cm* - please, thank you,  i don`t understand inches.
user_height = int(input("Hi! Tell me how Tall you are? (in cm please):"))

if user_height >= 145:
    print("Yes! You are tall enough to ride!")
else:
    print("Oh you are not tall enough for the ride\nyou need to to grow a bit...Sorry!")



