# Exercises XP
# Exercise 1 : Pets
# 1. Create another cat breed. In order to do so, create a class which inherits from the Cat class.
# 2. Create a few cat instances.
# 3. Create a list called my_cats, which will hold all the created cat instances.
# 4. Create a variable called my_pets. Its value is an instance of the Pet class.
# Hint : Use the my_cats variable to create the instance.
# 5. Take all the cats for a walk, use the walk method.

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1 = Bengal("John", 2)
cat2 = Chartreux("Gollum", 500)
cat3 = Persian("Garfield", 4)

my_cats = [cat1, cat2, cat3]

my_pets = Pets(my_cats)

my_pets.walk()


# Exercise 2 : Dogs
# 1. Create a class called Dog with the following attributes name, age, weight.
# 2. Implement the following methods in the Dog class:
#       *bark: returns a string which states: “<dog_name> is barking”.
#       *run_speed: returns the dogs running speed (weight/age*10).
#       *fight : takes a parameter which value should be another dog called other_dog, returns a string stating which dog won the fight.
#           The winner should be the dog with the higher run_speed x weight.
# 3. Create 3 dogs and run them through your class.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        speed_calculation = (self.weight / self.age) * 10
        return speed_calculation

    def fighting_power(self):
        return self.weight * self.run_speed()

    def fight(self, other_dog):
        if other_dog.fighting_power() > self.fighting_power():
            print(f"the winner is {other_dog.name}")
        else:
            print(f"the winner is {self.name}")


john_wick = Dog("John wick", 40, 110)
neo = Dog("Neo", 25, 85)
john_constantine = Dog("John Constantine", 30, 75)

john_wick.fight(neo)
neo.fight(john_constantine)
john_constantine.fight(john_wick)

# Exercise 3 : Dogs Domesticated
# 1. Create a new python file and import your Dog class from the previous exercise.
# 2. In the new python file, create a class named PetDog that inherits from Dog.
# 3. Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# 4. Add the following methods:
#       *train: prints the output of bark and switches the trained boolean to True
#       *play: takes a parameter which value is a few names of other dogs (use *args). The method should print the following string: “dog_names all play together”.
#       *do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#               *“dog_name does a barrel roll”.
#               *“dog_name stands on his back legs”.
#               *“dog_name shakes your hand”.
#               *“dog_name plays dead”.


