# Exercises XP - OOP
class Human:
    def __init__(self, name, age=0, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building.address
        building.inhabitants.append(self)


class Building:
    def __init__(self, address):
        self.address = address
        self.inhabitants = []

    def __eq__(self, other):
        return (self.address == other.address) and (self.inhabitants == other.inhabitants)


class City:
    def __init__(self, name):
        self.name = name
        self.buildings = []

    def construct(self, address):
        self.buildings.append(Building(address))

    def info(self, address: Building):
        age = 0
        buildings = 0
        for building in self.buildings:
            if building.address == address:
                buildings += 1
                for inhabitants in address.inhabitants:
                    age += inhabitants.age
                age = age / len(address.inhabitants)
                print(f"At {address.address} the average age of the inhabitants is: {int(age)}")


p1 = Human("Human1", 27)
p2 = Human("Human2", 10)
p3 = Human("Human3", 90)
p4 = Human("Human4", 45)
p5 = Human("Human5", 35)


b1 = Building("random 1, Jerusalem")
b2 = Building("random 2, Jerusalem")

p1.move(b1)
p2.move(b1)
p3.move(b2)
p4.move(b1)
p5.move(b2)

c = City("Jerusalem")
c.construct(b1)
c.construct(b2)

c.info(b1)
c.info(b2)
