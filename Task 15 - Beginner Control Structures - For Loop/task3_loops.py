

# ************ Question 1 ************
# while loop that will display count down from 20 to 0
# declare variable for count as 20 to start
# count down to 0 using while loop, count -1

print("\n")
print("Question 1: Display a count down from 20 to 0 ")
print("\n")

count = 20

while count >= 0:
    print(count)
    count = count - 1

# ************ Question 2 ************
# while loop that will display even numbers from 0 to 20
# declare variable as 0
# count to add 2

print("\n")
print("Question 2: Show even numbers from 0 to 20 ")
print("\n")
count = 0

while count <= 20:
    print(count)
    count = count + 2

# ************ Question 3 ************
# nested for loop that will display star pyramid
# declare rows as variable, run loop for rows
# use nested for loops for columns

print("\n")
print("Question 3: Display output of pyramid of stars ")
print("\n")

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end =' ')
    print("\r")


print("\n")
print("Question 4: Find the Highest Common Factor of two positive numbers ")
print("\n")

# Finally, write the code to compute the greatest common divisor
# (GCD, or highest common factor) of two positive integers
# import math and use gcd function

import math

int1 = int(input("Input a positive number?:"))
int2 = int(input("Input a second positive number?:"))

print (math.gcd(int1, int2))
