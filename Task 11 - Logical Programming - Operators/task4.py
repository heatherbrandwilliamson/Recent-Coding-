
# request user input
num = int(input("Please enter an integer:"))
calc_1 = num / 5
calc_2 = num / 2
print(calc_1)
print(calc_2)

# determine if num is divisible by 2 and 5

if (num % 5 == 0) and (num % 2 == 0) :
    print("number is divisible by 2 and 5")

# determine if num is divisible by 2 or 5

elif (num % 5 == 0) or (num % 2 == 0) :
    print("number is divisible by 2 or 5")

# determine if num is not divisible by 2 or 5

elif (num % 5 != 0) or (num % 2 != 0) :
    print("number is not divisible by 2 or 5")