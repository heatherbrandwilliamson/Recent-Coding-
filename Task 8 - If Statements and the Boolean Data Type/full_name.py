# request input from use
name = input("Enter your name:")

# calculate length and display
num_characters = len(name)
print(num_characters)

# decalare variables

no_input = 0
min_length = 4
max_lenth = 25


# Check if they have entered anything, else return error

if num_characters == no_input:
	print("You haven't entered anything. Please enter your full name")
	name = input("Enter your name:")

# Check if they have first and second name, else return error

elif num_characters <= min_length:
	print("You have entered less than 4 characters. Please make sure you have entered your full name")
	name = input("Enter your name:")

# Check if they have entered too many characters, else return error
# This is not the best test, as some people may have longs names - mine is 24 characters!

elif num_characters >= max_lenth:
	print("You have entered more than 25 characters. Please make sure you have only entered your full name")
	name = input("Enter your name:")

# print to say they have entered correctly
else:
	print("Thank you, you have entered your full name!")