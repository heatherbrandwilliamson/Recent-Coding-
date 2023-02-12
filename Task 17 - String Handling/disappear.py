

# Ask the user to input a string and then ask the user which characters they would like to make disappear.
# store input a variable
# use the translate function to remove the letters


string = "The quick brown fox jumps over the lazy dog."
user_input = input("Enter the characters you want to make disappear:")

print(string.translate({ord(i): None for i in user_input}))


