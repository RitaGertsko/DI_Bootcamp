# Exercise 1 : Built-In Functions
my_num = 5

# Print function
def print_functions(func):
    print(func)


print_functions(f"Int Doc:\n{int.__doc__}\n")
print_functions(f"Abs Doc:\n{abs.__doc__}\n")
print_functions(f"Input Doc:\n{input.__doc__}\n")

print_functions(my_num.__int__())
print_functions(abs(my_num))
print_functions(input(my_num))


# Exercise 2: Currencies
class Currency:
    def __init__(self, currency, amount=0):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"'{self.amount} {self.currency}'"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"'{self.amount} {self.currency}'"

    def __add__(self, other):
        if type(other) is int:
            return Currency(self.currency, self.amount + other)

        try:
            if self.currency != other.currency and type(other) != type(int):
                raise TypeError
            else:
                return Currency(self.currency, self.amount + other.amount)
        except TypeError:
            print(f"Not possible to add different types of currency: {self.currency} and {other.currency}")

    def __iadd__(self, other):
        if type(other) is int:
            return Currency(self.currency, self.amount + other)

        try:
            if self.currency != other.currency and type(other) != type(int):
                raise TypeError
            else:
                return Currency(self.currency, self.amount + other.amount)
        except TypeError:
            print("Not possible to add different currency types")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))

print(c1 + 5)
print(c1 + c2)

c1 += 5
print(c1)

c1 += c2
print(c1)

print(c1 + c3)
