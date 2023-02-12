
# ask the user how many students are registering.
# Create a for loop that runs for that amount of students
# Each time the loop runs it needs to ask the next student to enter their ID number.
# Write each of the ID numbers to a Text File called reg_form.txt
# open file and use write mode

myfile = open('reg_form.txt', 'w')
myfile.write("Here is the student register: \n")



# collect user data as int
# run for loop with range of student num
# write to file with input

student_num = int(input("Enter the number of students to register:"))

for i in range (0,student_num):
    student_id = input("Enter your student Id:")
    myfile.write(student_id)
    myfile.write("..........................\n")
    print (i)

# close file

myfile.close()