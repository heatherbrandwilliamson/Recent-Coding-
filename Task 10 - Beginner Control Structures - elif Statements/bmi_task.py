# request users input for their weight in kg and their height and   as variable

weight = float(input("Enter your weight in kgs:"))
height = float(input("Enter your height in m:"))

# use formula to calculate the users BMI
BMI = weight / (height * height)
print(BMI)

# if statement for obese
# elif for overweight
# elif for normal
# else for underweight

if BMI > 30:
    print("You are obese")
elif BMI > 25:
    print("You are overweight")
elif BMI > 18.5:
    print("You are normal")
else:
    print("You are underweight")

