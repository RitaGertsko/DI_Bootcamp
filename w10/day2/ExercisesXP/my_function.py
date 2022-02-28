class Human:
    pass


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
