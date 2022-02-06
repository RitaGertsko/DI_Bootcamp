text1 = """
If he had anything confidential to say, he wrote it in cipher, that is,
by so changing the order of the letters of the alphabet, that not a word could be made out.
"""
userPromptText = """
hello! please enter:
[1] to cipher
[2] to decipher
** enter either 1 or 2
"""


def cipher(text, increment):
    cypher_text = ""
    for letter in text:
        if ord("a") <= ord(letter) <= ord("z"):
            cypher_text += chr(ord("a") + ((ord(letter) + increment) - ord("a")) % 26)
        elif ord("A") <= ord(letter) <= ord("Z"):
            cypher_text += chr(ord("A") + ((ord(letter) + increment) - ord("A")) % 26)
        else:
            cypher_text += letter

    return cypher_text


def decipher(text, decrement):
    cypher_text = ""
    for letter in text:
        if ord("a") <= ord(letter) <= ord("z"):
            cypher_text += chr(ord("a") + ((ord(letter) - ord("a")) - decrement) % 26)
        elif ord("A") <= ord(letter) <= ord("Z"):
            cypher_text += chr(ord("A") + ((ord(letter) - ord("A")) - decrement) % 26)
        else:
            cypher_text += letter

    return cypher_text


toCipher = input(userPromptText)
while not (toCipher == "1" or toCipher == "2"):
    print("wrong input, please try again")
    toCipher = input(userPromptText)

userInputText = input("please enter the text to by ciphered:")
userIncriptionValue = input("please enter the letter shift value - needs to be a number")
while not userIncriptionValue.isnumeric():
    print("insert a number please")
    userIncriptionValue = input("please enter the letter shift value - need to be a number")

if toCipher == "1":
    print(cipher(userInputText, int(userIncriptionValue)))
else:
    print(decipher(userInputText, int(userIncriptionValue)))
