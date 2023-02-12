#====Login Section====
#Here you will write code that will allow a user to login.
# Open user.txt file and run read mode
# request the user to put input in for username and check against user file.

my_file = open("user.txt", "r", encoding='utf-8')    # open file
data = my_file.read()       # read the data
split_data = data.replace(',',"")
split_data = split_data.split()     #split to create list
my_file.close()
passwords_list = []    # store the variables for the username and password in 2 lists.
username_list = []

for index, item in enumerate(split_data, 0):   # Create two lists for username and password and store each item
    if index % 2 == 0:
        username_list.append(item)
    else:
        passwords_list.append(item)

username = str()
password = str()

# While loop for username, then while loop for password
# check that credentials are correct.
# show error message if input doesn't exist
while username not in username_list:
    username = input("please enter your username:")
    if username not in username_list:
        print("Incorrect username: please try again")
else:
    print("Correct username - Access is granted")
while password not in passwords_list:
    password = input("please enter your password:")
    if password not in passwords_list:
        print("Incorrect password: please try again")
else:
    print("Correct Password - Access is granted\n")

my_file = open("user.txt", "a", encoding='utf-8')

while True:
    if username.lower() == "admin":  #presenting the alternative menu to admin only.
        menu = input('''\nSelect one of the following options below:
            r - Registering a user
            a - Adding a task 
            va - View all tasks
            vm - view my task
            e - Exit
            s- Statistics 
            : ''').lower()
    else:
        menu = input('''\nSelect one of the following Options below:  
        a - Adding a task  
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()


# request input of a new username & password
# request input of a mew password
# confirmation of the new password, run a while true loop
# show error message
# check that username is equal to admin, to allow access to "r"

    if menu == 'r' and username == "admin":
        new_username = input("please enter the new username for the new user:")
        new_password = input("Please enter the new password for the new user:")
        confirmed_password = ()
        my_file.write("\n")
        my_file.write(new_username)
        my_file.write(", ")
        while new_password != confirmed_password:
            confirmed_password = input("Please confirm the new password:")
            if new_password != confirmed_password:
                print("passwords do not match: please try again")
        else:
            my_file.write(confirmed_password)
            print("New user has been added to the file user.txt \n")

# if "a" then append the file once open
# request the user input for task, task assigned to, description, due date and todays date.
# add field for task complete as yes or no.
# write to file

    elif menu == 'a':
        pass
        task_file = open("tasks.txt", "a", encoding='utf-8')
        user_task = input("please enter the username the task is assigned to:")
        title_task = input("please enter the title of the task:")
        description_task = input("please enter a description of the task:")
        date_today = input("Enter todays date: DD MONTH YEAR") #can change to be automatic?
        due_task = input("please enter the due date of the task in the following format: DD MONTH YEAR ")
        task_complete = "No"
        task_file.write("\n")
        task_file.write(user_task)
        task_file.write(", ")
        task_file.write(title_task)
        task_file.write(", ")
        task_file.write(description_task)
        task_file.write(", ")
        task_file.write(date_today)
        task_file.write(", ")
        task_file.write(due_task)
        task_file.write(", ")
        task_file.write(task_complete)
        task_file.close()

# read a line from the file, open file using with function
# for loop function
# split data by comma and convert to a list
# print data by index and next to title as per output 2

    elif menu == 'va':
        with open("tasks.txt", 'r') as file_data:
            for line in file_data:
                data = line.split(",")
                print("Task:               " + data[1])
                print("Assigned to:         " + data[0])
                print("Date Assigned:      " + data[3])
                print("Due date:           " + data[4])
                print("Task description:   " + data[2])
                print("Is task complete?:  " + data[5])

# Using with function, run a for loop to read data on each line.
# split data by comma and call out each index
# display data in readable format

    elif menu == 'vm':
        with open("tasks.txt", 'r') as file_data:
            for line in file_data:
                data = line.split(",")
                if data[0] == username:
                    print("Here are your assigned tasks:\n")
                    print("Task:               " + data[1])
                    print("Assigned to:         " + data[0])
                    print("Date Assigned:      " + data[3])
                    print("Due date:           " + data[4])
                    print("Task description:   " + data[2])
                    print("Is task complete?:  " + data[5])

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

# S is the option for admin to read a report on total users and total tasks.
    elif menu == "s" and username == "admin":
        with open("user.txt", 'r') as my_file:
            for count, line in enumerate(my_file):
                pass
        print('Total users:', count + 1)

        with open("tasks.txt", 'r') as my_file:
            for count, line in enumerate(my_file):
                pass
        print('Total tasks:', count + 1)

    else:
        print("You have made a wrong choice, Please Try again")


def reg_user()
    new_username = input("please enter the new username for the new user:")
    new_password = input("Please enter the new password for the new user:")
    confirmed_password = ()
    my_file.write("\n")
    my_file.write(new_username)
    my_file.write(", ")
    while new_password != confirmed_password:
        confirmed_password = input("Please confirm the new password:")
        if new_password != confirmed_password:
            print("passwords do not match: please try again")
    else:
        my_file.write(confirmed_password)
        print("New user has been added to the file user.txt \n")
    return

result = reg_user() # call function.
print(result)



# close the file
my_file.close()


