# write a program to input a year and a number of years
# delcare and store variables for input, convert to ints
# write a for loop to check if divisible by 4 and print if it is leap year

year = int(input("What year do you want to start with?:"))
num_years_to_check = int(input("How many years do you want to check:"))
calc = year + num_years_to_check

for i in range (year, calc):
	if i % 4 == 0 :
		print(f"{i} is a leap year")
	else:
		print(f"{i} is not a leap year")
