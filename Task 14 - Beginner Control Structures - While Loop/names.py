# request user to enter all the names in a class
# request user to enter stop to indicate all names have been entered
# run While loop until Stop entered
# print count of names entered, does not include stop.

count = -1

while True:
    names = input("Enter names of students in a class. Enter Stop when all names are entered: ")
    count = count + 1
    if names == "Stop":
        print(count)
        break




