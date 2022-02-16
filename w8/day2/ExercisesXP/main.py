# Exercises XP
# Exercise 1: Cats

# 1. Instantiate three Cat objects using the code provided above.
# 2. Outside the class, create a function that finds the oldest cat and returns the cat.
# 3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
# from itertools import groupby


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("Gorg", 2)
cat2 = Cat("Ron", 9)
cat3 = Cat("lola", 4)


def finding_the_oldest_cat(c1, c2, c3):
    cats = [c1.age, c2.age, c3.age]
    return max(cats)


print(f'The oldest cat is {finding_the_oldest_cat(cat1, cat2, cat3)} years old.')


# Exercise 2 : Dogs
# 1. Create a class called Dog.
# 2. In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# 3. Create a method called bark that prints the following string “<dog_name> goes woof!”.
# 4. Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# 5. Outside the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# 6. Print the details of his dog (i.e. name and height) and call the methods bark and jump.
# 7. Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# 8. Print the details of her dog (i.e. name and height) and call the methods bark and jump.
# 9. Create an if statement outside the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x}cm high!")


davids_dog = Dog("Rex", 50)

print(f"Davids dog name id {davids_dog.name} and his height is {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)

print(f"Sarah`s dog name id {sarahs_dog.name} and his height is {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()

# def is_the_bigger_dog(*args):
#     bigger_dog = max(args)
#     print(bigger_dog.name)
#
#
# is_the_bigger_dog(davids_dog, sarahs_dog)


if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the biggest!")
else:
    print(f"{sarahs_dog.name} is the biggest!")


# Exercise 3 : Who’s The Song Producer?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object
# Then, call the sing_me_a_song method.

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for element in self.lyrics:
            print(element)


i_see_fire = Song(["Now I see fire Inside the mountain",
                   "And I see fire Burning the trees",
                   "And I see fire Hollowing souls",
                   "And I see fire Blood in the breeze",
                   "And I hope that you remember me"])

i_see_fire.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# 1. Create a class called Zoo.
# 2. In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# 3. Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# 4. Create a method called get_animals that prints all the animals of the zoo.
# 5. Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# 6. Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# 7. Create a method called get_groups that prints the animal/animals inside each group.
# 8. Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.groups = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        convert_list_to_str = (str(animal) for animal in self.animals)
        print(' , '.join(convert_list_to_str))

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        alpha = sorted(list({animal[0] for animal in self.animals}))
        for letter in alpha:
            self.groups[letter] = []
            for animal in self.animals:
                if animal[0] == letter:
                    self.groups[letter].append(animal)

    def get_groups(self):
        for key, group in self.groups.items():
            print(key + ": ", group)


ramat_gan_safari = Zoo("ramat_gan_safari")
ramat_gan_safari.animals = ["Kangaroo", "Cat", "Bear", "Koala", "Monkey", "Panther", "Tiger"]

ramat_gan_safari.add_animal("Penguin")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Tiger")
ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
