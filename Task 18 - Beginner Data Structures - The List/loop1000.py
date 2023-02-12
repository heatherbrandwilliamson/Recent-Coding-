#You are asked to print out all the numbers from 1 to 1000.
# Write 2 lines of code in your file to print out all numbers from 1 to 1000.
# for loop using the in function
# even numbers modulus is equal to zero

x = range(1001)

for i in x:
    if i % 2 == 0:
        print(i)

