# Exercises XP
# Exercise 1 – Random Sentence Generator
import json
import random

words = []

def get_words_from_file():
    with open('sowpods.txt', 'r') as f:
        for line in f.readlines():
            words.append(line.strip())


def get_random_sentence(length: int):
    sentence = ' '.join([random.choice(words) for _ in range(length)])
    print(sentence.capitalize())


def main():
    print('This program will create a random sentence')

    try:
        length = int(input('How long do you want the sentence to be? Must be 2~20\n>>>'))
        if 1 < length < 21:
            get_words_from_file()
            get_random_sentence(length)
        else:
            print('Incorrect number!')
    except ValueError as v:
        print(f"\nValue error: {v}\nyou should've entered an integer")


print(f"---------------------Exercise 1--------------------------")
main()

# Exercise 2: Working With JSON
sampleJson = {
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}

print(f"\n---------------------Exercise 2--------------------------")
# 1.
print(f"Salary value is: {sampleJson['company']['employee']['payable']['salary']}")
# 2.
sampleJson['company']['employee']['birth_date'] = '14/12/1945'
# 3.
json_file = 'my_file.json'
with open(json_file, 'w') as file_obj:
    json.dump(sampleJson, file_obj, indent=3)
