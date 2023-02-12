# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program")
print ("\n")
# no need for indentation & added parentheses

# no need for indentation and double equals sign incorrect
age = 24
#I'm 24 years old.
# cannot convert sting to int, remove additional text in string
print(f"I'm {age} years old.")
# removed string and inserted f function into print
three_andhalf = 3.5
# logic is not correct, should be 3.5 for 3 and half years

# no need for indentation & remove string double quote marks
# corrected variable naming format with lower case

answer_years = (age + three_andhalf)
print(answer_years)

print (f"The total number of years: {answer_years} ")
# added parentheses, inserted f function and included curly brackets for variable

answer_months = answer_years * 12
# incorrect name of variable
print(f"In 3 years and 6 months, I'll be {answer_months} months old")
# added parentheses

#HINT, 330 months is the correct answer

