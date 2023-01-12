

import math

# request user input for investment or bond
# show error message for no type from user & accept capitals from user
# if statement for investment or bond
# if investment then run if statement for simple or compound
# declare variables
# run formula and output result


investment_type = input("Choose either 'investment' or 'bond' from the menu below to proceed; "
                "\n"
                    "\n Investment -  to calculate the amount of interest you'll earn on your investment"
                    "\n Bond -  to calculate the amount you'll have to pay on your home loan \n")

if investment_type == "Investment" or investment_type == "INVESTMENT" or investment_type == "investment":
    print("Investment has been selected")
    investment_amount = float(input("Enter the amount you wish to deposit:"))
    interest_rate = float(input("Enter the interest rate %:"))
    term = int(input("Enter the amount of years you want plan on investing:"))
    interest = input("Type of interest (simple or compound):")
    if interest == "Compound" or interest == "COMPOUND" or interest == "compound":
        print("Compound")
        P = investment_amount
        r = interest_rate / 100
        t = term
        A = P * math.pow((1 + r), t)
        print("Your investment at the end of your investment term will be: ")
        print (round(A))

    # Simple interest calculation below
    elif interest == "Simple" or interest == "SIMPLE" or interest == "simple":
        print("Simple:")
        P = investment_amount
        r = interest_rate / 100
        t = term
        A = P * (1 + r * t)
        print("Your investment at the end of your investment term will be: ")
        print(A)

    else:
        print("error")

# Bond calculation below
elif investment_type == "Bond" or investment_type == "BOND" or investment_type == "bond":
    print("Bond has been selected")
    house_price = int(input("The current price of your house:"))
    annual_interest = float(input("The interest rate:"))
    months = float(input("The number of months you plan to take to repay your bond:"))
    monthly_interest = (annual_interest/100 ) / 12
    x = (monthly_interest*house_price) / (1 - (1 + monthly_interest) ** (-months))
    print("Your monthly repayment will be: ")
    print(round(x))

# show error message for incorrect input
else:
    print("Error")