#request user input and store as three variables
# request input from use
shape = input("Enter the building shape (square, rectangular, round):")
pi = 3.14159265359

#if statements based on user input
if shape == "square":
    print("Your building is square.")
    #request user input for length and width
    length = int(input("Enter the building length:"))
    area_of_square = length * length
    print("The area of your building is:")
    print(area_of_square)

if shape == "rectangular":
    print("Your building is rectangular.")
    #request user input for length and width
    length = int(input("Enter the building length:"))
    width = int(input("Enter the building width:"))
    area_of_rectangular = length * width
    print("The area of your building is:")
    print(area_of_rectangular)

if shape == "round":
    print("Your building is round.")
    #request user input for radius
    radius = float(input("Enter the building radius:"))
    area_of_round = pi * (radius * radius)
    print("The area of your building is:")
    # round up area of round for calculation
    print(round(area_of_round))


