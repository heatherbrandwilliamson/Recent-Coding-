# request year born from user and store as integer

year_born = int(input("Enter the year you were born:"))

# if statement for over 18, based on born before 2004

if year_born <= 2004:
    print("Congrats you are old enough!")
else:
    print("Sorry you are not old enough!")

