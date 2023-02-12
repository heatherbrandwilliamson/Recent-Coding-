
#declare numbers and store as three variables

num_one = 99
num_two = 77
num_three = 9

# compare num1 with num 2 and print largest number
print("What is the highest number:")
if num_one > num_two:
    print(num_one)
elif num_one < num_two:
    print (num_two)

# determine if num 1 is odd or even and display result
# use modulus operator and equal to zero display even
print("Is the number even or odd?")
if num_one % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# write a conditional statement to sort the three numbers from largest to smallest
# determine the highest number and store as variable

if (num_one > num_two) and (num_one > num_three):
    highest_number = num_one
elif (num_two > num_one) and (num_two > num_three):
    highest_number = num_two
elif (num_three > num_two) and (num_three > num_two):
    highest_number = num_three

# determine the middle number and store as variable

if (num_one < num_two) and (num_one < num_three):
    lowest_number = num_one
elif (num_two < num_one) and (num_two < num_three):
    lowest_number = num_two
elif (num_three < num_two) and (num_three < num_two):
   lowest_number = num_three

# determine the lowest number and store as variable

if (num_one < num_two) and (num_one > num_three):
    middle_number = num_one
elif (num_two < num_one) and (num_two > num_three):
    middle_number = num_two
elif (num_three < num_two) and (num_three > num_two):
   middle_number = num_three

print("highest number is:")
print(highest_number)

print("middle number is:")
print(middle_number)

print("lowest number is:")
print(lowest_number)




