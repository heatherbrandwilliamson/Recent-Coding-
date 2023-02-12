
# store variables
# request user input and run while loop
# stop if user enters -1
# remove -1 from list
# return average from numbers entered
# calculation is sum divided by len

user_list = []
stop = -1

while True:
    n = int(input("Enter a number:"))
    user_list.append(n)
    len(user_list)
    if n == stop:
        user_list.remove(-1)
        len(user_list)
        calc = sum(user_list) / len(user_list)
        print(calc)
        break

