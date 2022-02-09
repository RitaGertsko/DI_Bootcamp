# Daily Challenge : Exceptions
# Write a function to compute 5/0 and use try/except to catch the exceptions.


def compute():
    try:
        5 / 0
    except:
        print("5 can't be divided by 0")

# def compute():
#     print('We\'ll divide 5 by a number of your choice')
#     while True:
#         try:
#             userNumber = int(input('Insert a number\n>>>'))
#             computerOutputNum = 5 / userNumber
#         except ZeroDivisionError as divisionErr:
#             print(f'Error: "{divisionErr}".\n5 can\'t be divided by 0')
#         except ValueError as valueErr:
#             print(f'not a valid value, "{valueErr}"')
#         else:
#             print(f'The result of the division is: {computerOutputNum}\nGoodbye!')
#             break


compute()
