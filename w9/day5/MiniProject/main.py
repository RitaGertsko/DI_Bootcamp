# Mini Project : Vaccines
class Human:
    blood_type_list = ["A", "B", "AB", "O"]

    def __init__(self, blood_type, id_number=str(), name=str(), age=int(), prioritary=False):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.prioritary = prioritary
        self.blood_type = [element for element in Human.blood_type_list if element == blood_type]
        self.family = []

    def __repr__(self):
        return f"Name: {self.name}, Id: {self.id_number}, Age: {self.age}, Blood Type: '{' '.join(self.blood_type)}', Prioritary: {self.prioritary}\n"

    def __str__(self):
        return f"{self.name}: {self.age}"

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if type(person) == Human:
            if person.age >= 60 or person.prioritary is True:
                if person.prioritary is False:
                    person.prioritary = True
                self.humans.insert(0, person)
            else:
                self.humans.append(person)
        else:
            raise TypeError("TypeError: check the type of the argument")

    def find_in_queue(self, person):
        if type(person) == Human:
            if person in self.humans:
                return self.humans.index(person)
            else:
                return f"{person.name} is not in Queue yet"
        else:
            raise TypeError("TypeError: check the type of the argument")

    def swap(self, person1, person2):
        if person1 in self.humans and person2 in self.humans:
            index_person1 = self.humans.index(person1)
            index_person2 = self.humans.index(person2)

            self.humans[index_person1], self.humans[index_person2] = self.humans[index_person2], self.humans[
                index_person1]
            return

        if person1 not in self.humans and person2 not in self.humans:
            return f"Both {person1.name} and {person2.name} are not in Queue yet"
        elif person1 not in self.humans:
            return f"{person1.name} is not in Queue yet"
        else:
            return f"{person2.name} is not in Queue yet"

    def get_next(self):
        if len(self.humans) == 0:
            return None
        person_next_in_line = self.humans[0]
        self.humans.remove(person_next_in_line)
        return person_next_in_line

    def get_next_blood_type(self, blood_type):
        if blood_type in Human.blood_type_list:
            for person in self.humans:
                if ''.join(person.blood_type) == blood_type:
                    print(f"{person.name} is the first person with the blood type '{blood_type.upper()}'")
                    self.humans.remove(person)
                    return person
            print("No one with that blood type is in queue")
        else:
            return None

    def sort_by_age(self):
        if len(self.humans) > 1:
            self.humans.sort(key=lambda human: human.age, reverse=True)
        else:
            raise Exception("Error: No one is in queue")

    def rearrange_queue(self):
        if len(self.humans) > 2:
            for person in self.humans:
                if self.humans.index(person) == len(self.humans) - 1:
                    return
                if person in self.humans[self.humans.index(person) + 1].family:
                    self.humans.insert(len(self.humans) - 1, self.humans.pop(self.humans.index(person)))


rita = Human(id_number="1234", name="Rita", age=20, blood_type="A")
alex = Human(id_number="1235", name="Alex", age=30, blood_type="B")
patrik = Human(id_number="1236", name="Patrik", age=27, blood_type="O")
yuri = Human(blood_type="O", id_number="1237", name="Yuri", age=65)
luda = Human(blood_type="AB", id_number="1238", name="Luda", age=61)

q = Queue()

q.add_person(alex)
q.add_person(yuri)
q.add_person(luda)

print(q.humans)

print(f"Alex place in line is: {q.find_in_queue(alex)}")
print(q.find_in_queue(patrik))

q.swap(luda, yuri)
print(q.humans)

# print(q.get_next())

# q.get_next_blood_type("B")
# print(q.get_next_blood_type("C"))

q.sort_by_age()
print(q.humans)

luda.add_family_member(yuri)
# print(luda.family)
# print(yuri.family)
q.rearrange_queue()
print(q.humans)
