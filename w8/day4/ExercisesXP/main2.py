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

from random import randint

from main import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        self.bark()

    def play(self, *args):
        arg_name = ", ".join(args)
        arg_name = arg_name + f" and {self.name}"
        print(arg_name)

    def do_a_trick(self):
        if self.trained:
            dog_trained_sentences = [
                                    f"{self.name} does a barrel roll",
                                    f"{self.name} stands on his back legs",
                                    f"{self.name} shakes your hand",
                                    f"{self.name} plays dead",
                                     ]
            sentence = randint(0, 3)
            print(dog_trained_sentences[sentence])


dog1 = PetDog("Rex", 3, 40)
dog2 = PetDog("Joh", 2, 35)
dog3 = PetDog("Alex", 9, 50)
dog4 = PetDog("Gerold", 500, 100)

dog1.train()
dog1.play(dog2.name, dog3.name, dog4.name)
dog1.do_a_trick()
