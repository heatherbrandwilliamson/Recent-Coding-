# request input from use
str_manip = input("Enter a sentence:")

# calculate length and display
print()
print(len(str_manip))

# find the last letter in the string
# store as variable
last_char = str_manip[-1]
print()
print(last_char)

# replace last character with @
print()
print(str_manip.replace((last_char),"@"))

# print last 3 digits in reverse, perhaps this can be one step and improved?

string_reversed = str_manip[::-1]
print()
print(string_reversed[0:3])

# create five letter word made up of first 3 characters and last 2 characters

#call first 3 characters
first_3char=str_manip[0:3]
#call last 2 characters
last_2char=str_manip[-2:]
first_and_last_char =first_3char +last_2char

print()
print(first_and_last_char)

# print each word on a new line using replace
str_manip = str_manip.replace(" ", "\n")
print()
print(str_manip)