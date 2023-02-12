# request users input for their age and store as variable


age = int(input("Enter your age:"))

# if statement for over 18
# elif for between 16 and 18
# else not old enough

if age >= 18:
    print("You are old enough!")
elif age > 16:
        print("Almost there")
else:
    print("Sorry you are not old enough!")