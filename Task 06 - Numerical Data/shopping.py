
# Request user for input

print("Please enter 3 shopping items")
item_one = (input("Item 1:"))
item_two = (input("Item 2:"))
item_three = (input("Item 3:"))

# request the price of all items and print

print("Please enter the price of the 3 items")
price_one = float(input("Price of item one:"))
price_two = float(input("Price of item two:"))
price_three = float(input("Price of item three:"))

# calculate the total of all items
total= price_one + price_two + price_three

# calculate the average price
average_price = total / 3

# round average price to 2 decimal places
import math
calculation_rounded=(math.floor(average_price*100)/100)

# print out results in sentence

print(f"The Total of {item_one}, {item_two}, {item_three} is £{total} and the average is £{calculation_rounded}")

