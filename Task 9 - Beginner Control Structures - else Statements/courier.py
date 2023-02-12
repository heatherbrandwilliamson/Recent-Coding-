#Ask the user to enter the price of package they would like to send

parcel_price = int(input("Enter the price of the package you would like to send: \n"))
distance = int(input("Enter your total distance of the delivery in KMs \n"))

# declare variables

air_price= 0.36
freight_price = 0.25
full_insurance = 50
limited_insurance = 25
gift = 15
no_gift = 0
priority = 100
no_priority = 20

# distance multiplied by air or freight fare

air_check= input("Do you want to post via air? (Yes or No)")
if air_check == "Yes":
    total = distance * air_price
else:
    total = distance * freight_price

# If statement for insurance & store new total as variable

insurance_check= input("Do you want full insurance? (Yes or No)")
if insurance_check == "Yes":
    total_with_insurance = total + full_insurance
else:
    total_with_insurance = total + limited_insurance

# If statement for gift & store new total as variable

gift_check= input("Do you want to send as a gift? (Yes or No)")
if gift_check == "Yes":
    total_with_gift = total_with_insurance + gift
else:
    total_with_gift = total_with_insurance + no_gift

# If statement for priority & store new total as variable

priority_check= input("Do you want to send as via priority? (Yes or No)")
if priority_check == "Yes":
    total_with_priority = total_with_gift + priority
else:
    total_with_priority = total_with_gift + no_priority

# calculate final cost with cost of parcel & print out
total_cost = total_with_priority + parcel_price

print(f"Total cost to send the pacakge is: £{total_cost}")
