

#store names as empty list
# request user input
# append names to a list
# while loop if true
# include upper and lower functions.

names = []
stop = "JOHN"

# convert to upper

while True:
    name = input("Please enter a name: ")
    if (name.upper()) == stop:
        print(f"Incorrect names:{names}")
        break
    names.append(name)



