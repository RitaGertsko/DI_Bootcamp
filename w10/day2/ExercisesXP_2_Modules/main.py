# Exercises XP #2 - Modules
# Exercise 1
import datetime

# today = datetime.date.today().strftime('%d-%m-%Y')
# print(f"today is: {today}")


# Exercise 2
def time_left_till():
    date_today = datetime.date.today()
    date_target = datetime.date(date_today.year + 1, 1, 1)
    print(f"The 1st of January is in {date_target - date_today}")


# time_left_till()

# Exercise 3
def how_long_did_u_live(birthdate):
    try:
        user_birthday = datetime.datetime.strptime(birthdate, "%d/%m/%Y %H:%M:%S")
        date_now = datetime.datetime.now()
        time_delta = date_now - user_birthday
        total_seconds = time_delta.total_seconds()
        minutes = total_seconds / 60
        print(f"You have been alive for {minutes} minutes")

    except:
        print("Enter your birthday in the valid format (day/month/year)")


# how_long_did_u_live(0000)

# Exercise 4
purim = datetime.datetime(2022, 3, 15)

def next_holiday():
    today_date = datetime.datetime.now()
    print(f"Purim is in {str((purim - today_date)).replace(',', ' and')} hours")


# next_holiday()

# Exercise 5 : How Old Are You On Jupiter?

# age = int(input("What is your age in seconds?\n"))
# earth = age / 31557600
# mercury = earth * 0.2408467
# venus = earth * 0.61519726
# mars = earth * 1.8808158
# jupiter = earth * 11.862615
# saturn = earth * 29.447498
# uranus = earth * 84.016846
# neptune = earth * 164.79132

# print(f"You are {round(earth, 2)} Earth-years old")
# print(f"You are {round(mercury, 2)} Mercury-years old")
# print(f"You are {round(venus, 2)} Venus-years old")
# print(f"You are {round(mars, 2)} Mars-years old")
# print(f"You are {round(jupiter, 2)} Jupiter-years old")
# print(f"You are {round(saturn, 2)} Saturn-years old")
# print(f"You are {round(uranus, 2)} Uranus-years old")
# print(f"You are {round(neptune, 2)} Neptune-years old")

# Exercise 6 : Faker Module

from faker import Faker

fake = Faker()
user = [{}] * 5

def add_data():
    for i in user:
        i['name'] = fake.name()
        i['address'] = fake.address()
        i['language'] = fake.language_code()


# add_data()
# print(user)
