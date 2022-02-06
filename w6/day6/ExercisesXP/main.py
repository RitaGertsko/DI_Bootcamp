# Exercise 1 : Convert Lists Into Dictionaries
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = {}
for key, value in zip(keys, values):
    dic[key] = value

print(dic)

# Exercise 2 : Cinemax #2
# 1. A movie theater charges different ticket prices depending on a person’s age.
#   if a person is under the age of 3, the ticket is free.
#   if they are between 3 and 12, the ticket is $10.
#   if they are over the age of 12, the ticket is $15.
# 2. Given the following object:
#       family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# 3. How much does each family member have to pay ?
# 4. Print out the family’s total cost for the movies.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
totalCost = 0

for name, age in family.items():
    if 3 <= age <= 12:
        print(f"{name} needs to pay $10")
        totalCost += 10
    elif age > 12:
        print(f"{name} needs to pay $15")
        totalCost += 15
    else:
        print(f"{name} doesnt need to pay!")

print(f"the total sum is {totalCost}")

# for name, age in family.items():
# #     match age:
# #         case age if 3 <= age <= 12:
# #             print(f"{name} needs to pay $10")
# #             totalCost += 10
# #         case age if 12 < age:
# #             print(f"{name} needs to pay $15")
# #             totalCost += 15
# #         case _:
# #             print(f"{name} doesnt need to pay!")

# Exercise 3: Zara
# 1. Here is some information about a brand.
#       name: Zara
#       creation_date: 1975
#       creator_name: Amancio Ortega Gaona
#       type_of_clothes: men, women, children, home
#       international_competitors: Gap, H&M, Benetton
#       number_stores: 7000
#       major_color:
#           France: blue,
#           Spain: red,
#           US: pink, green
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {"name": "Zara", "creation_date": 1975, 'creator_name': "Amancio Ortega Gaona",
         "type_of_clothes": ["men", "women", "children", "home"],
         "international_competitors": ["Gap", "H&M", "Benetton"], "number_stores": 2, "major_color": {
                "France": "blue",
                "Spain": "red",
                "US": ["pink", "green"]
             }
         }

# 3. Change the number of stores to 2.

# 4. Print a sentence that explains who Zaras clients are.
zaraClientsString = ""
zaraClients = brand["type_of_clothes"]
for index in range(len(zaraClients)):
    if index == (len(zaraClients) - 1):
        zaraClientsString = zaraClientsString[:-2]
        zaraClientsString += f" and {zaraClients[index]}"
        break
    zaraClientsString += f"{zaraClients[index]}, "

print(f"zara serve clothes to: {zaraClientsString}")

# 5. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if brand.keys().__contains__("international_competitors"):
    brand["international_competitors"].append("Desigual")

# 7. Delete the information about the date of creation.
del brand["creation_date"]
# 8. Print the last international competitor.
print(brand["international_competitors"][-1:])
# 9. Print the major clothes colors in the US.
print(brand["major_color"]["US"].__str__()[1:-1].replace("'", ""))

# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

# 11. Print the keys of the dictionary.
brandKeys = ""
for key in brand.keys():
    brandKeys += key + ", "
print(brandKeys[:-2])

# 12. Create another dictionary called more_on_zara with the following details:
#       creation_date: 1975
#       number_stores: 10 000
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000,
}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)

# 14. Print the value of the key number_stores. What just happened ?
print(brand)
# for existing keys their values got updated and for non-existing keys they got added.


# Exercise 4: Disney Characters
# Use this list :
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Analyse these results :
# 1.
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# 2.
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# 3.
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# 1. Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
disney_users_A = {}
value = 0
for name in users:
    disney_users_A[name] = value
    value += 1
print(disney_users_A)

# 2. Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
disney_users_B = {}
value = 0
for name in users:
    disney_users_B[value] = name
    value += 1
print(disney_users_B)

# 3. Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
disney_users_c = {}
users.sort()
value = 0

for name in users:
    disney_users_c[name] = value
    value += 1
print(disney_users_c)
# 4. Only recreate the 1st result for:
#       1. The characters, which names contain the letter “i”.
disney_users_A = {}
value = 0
for name in users:
    if name.count("i") == 0:
        continue
    disney_users_A[name] = value
    value += 1
print(disney_users_A)
#       2. The characters, which names start with the letter “m” or “p”.
disney_users_A = {}
value = 0
for name in users:
    if not (name[:1] == "M" or name[:1] == "P"):
        continue
    disney_users_A[name] = value
    value += 1
print(disney_users_A)
