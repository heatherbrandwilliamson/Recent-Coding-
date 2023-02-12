

# create a list called menu
# store the stock items in a dictionary
# store the price items in a second dictionary
# calculate the total stock with stock * price
# for loop to access each value in dictionary
# add up for each menu item
# Value of stock = price per item * stock per item


menu = ["Flat white", "Hot chocolate", "Croissant", "Muffin"]

stock = {
  menu[0]: 10,
  menu[1]: 17,
  menu[2]: 19,
    menu[3]: 5
}

price = {
    menu[0]: 3,
    menu[1]: 2,
    menu[2]: 3,
    menu[3]: 4
}

print(stock)
stock_value = [i for i in stock.values()]

print(price)
stock_price = [i for i in price.values()]

value_of_item0 = stock_price[0] * stock_value[0]
value_of_item1 = stock_price[1] * stock_value[1]
value_of_item2 = stock_price[2] * stock_value[2]
value_of_item3 = stock_price[3] * stock_value[3]

print("total stock value:")
total = (value_of_item0) + (value_of_item1) + (value_of_item2) + (value_of_item3)
print(total)
