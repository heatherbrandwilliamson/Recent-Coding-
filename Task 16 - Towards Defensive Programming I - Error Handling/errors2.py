# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program")
print ("\n")    #Compilation error; incorrect space indentation. Added parentheses.
#



age = 24  #Compilation error; incorrect space indentation. Syntax error, single equal sign to store variable.
#I'm 24 years old.

# Syntax error. No need to convert to string, remove additional text in string and store as int.

print(f"I'm {age} years old.")

# Runtime error. removed string and inserted f function into print

three_and_half = 3.5   # logicical error:  should be 3.5 for 3 and half years

# Compilation error; incorrect space indentation. removed string double quote marks and store as float.
# Best practice - corrected variable naming format with lower case and underscore.

answer_years = (age + three_and_half)
print(answer_years)

print (f"The total number of years: {answer_years} ")
# Runtime error. added parentheses, inserted f function and included curly brackets for variable

answer_months = answer_years * 12
# Runtime error. incorrect name of variable
print(f"In 3 years and 6 months, I'll be {answer_months} months old")
# Syntax Error. added parentheses, and included f function.

#HINT, 330 months is the correct answer

