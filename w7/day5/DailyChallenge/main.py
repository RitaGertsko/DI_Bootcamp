
# Daily Challenge: Sorting
user_input = input("give me words separated by a comma only: ")
user_input = [word for word in user_input.split(",")]
user_input.sort()
ans = ','.join(user_input)
print(ans)

