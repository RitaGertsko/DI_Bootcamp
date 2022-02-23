# Daily Challenge - Circle
import math

class Circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def __repr__(self):
        return f"{self.name}: {self.radius}r`".capitalize()

    def circle_area(self):
        return math.pi * (self.radius * 2)

    def __add__(self, other):
        return self.circle_area() + other.circle_area()

    def print_circle(self):
        my_circle = int(self.circle_area())
        print(f"Your circle area is: {self.circle_area()} and it looks like this:\n")

        for row in range((2 * my_circle) + 1):
            for col in range((2 * my_circle) + 1):
                area = math.sqrt((row - my_circle) * (row - my_circle) +
                                 (col - my_circle) * (col - my_circle))

                if my_circle - 0.5 < area < my_circle + 0.5:
                    print("*", end="")
                else:
                    print(" ", end="")

            print()

    def compare(self, other):
        if self.circle_area() == other.circle_area():
            return f"The circles {self.name} and {other.name} are equal!\n"
        elif self.circle_area() > other.circle_area():
            return f"{self.name} is the bigger circle!\n".capitalize()
        else:
            return f"{other.name} is the bigger circle!\n".capitalize()

    @staticmethod
    def circles_to_list(*args):
        sorted_circles_list = sorted([circle for circle in args], key=lambda c: c.name)
        return sorted_circles_list


c1 = Circle("c1", 1)
c2 = Circle("c2", 3)
c3 = Circle("c3", 7)
c4 = Circle("c4", 1)

c1.print_circle()
print(f"add: {c1.__add__(c2)}\n")
print(c2.compare(c1))
print(c1.compare(c4))
print(Circle.circles_to_list(c3, c1, c3, c4, c1, c2))
