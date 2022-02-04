
# Daily Challenge: Happy Birthday
# 1. Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# 2. Display a little cake
# 3. The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

from datetime import datetime

my_date = input("Enter Birthday date in mm/dd/yyyy format:")
birthdayDateFormatted = datetime.strptime(my_date, '%d/%m/%Y')
print(type(datetime.today() - birthdayDateFormatted))

age = int(((datetime.today() - birthdayDateFormatted).days / 365))
print(f"Age : {age}")

cake = """
       ___________
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
print(cake.replace("_", "i", age % 10))
