# Daily Challenge: Build Up A String
# 1. Using the input function, ask the user for a string. The string must be 10 characters long
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
from random import shuffle

user_answer = input("give me a sentence 10 letters long")
user_answer_length = len(user_answer)

if user_answer_length > 10:
    print("string too long")
elif user_answer_length < 10:
    print("string not long enough")
else:  # 2. print the first and last characters of the given text.
    print(user_answer[0], user_answer[9])

# 3. Construct the string character by character: Print the first character, then the second, then the third,
# until the full string is printed.

new_sentence = " "
for i in range(user_answer_length):
    new_sentence += user_answer[i]
    print(new_sentence)

# 4. Swap some characters around then print the newly jumbled string

user_answer_into_a_list = list(user_answer)
shuffle(user_answer_into_a_list)
user_answer_into_a_string = "".join(user_answer_into_a_list)
print(user_answer_into_a_string)
