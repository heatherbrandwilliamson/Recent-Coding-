
# open files and store as two variables
# store list as numbers
# store variable for combined files

myfile = open('numbers1.txt', "r")

myfile_two = open("numbers2.txt","r")

numbers = []

combined_files = open('all_numbers.txt', "w")

#for loop over the first file, and append to list
for line in myfile:
    numbers.append(line.strip("\n"))

#for loop over the second file, and append to list
for line in myfile_two:
    numbers.append(line.strip("\n"))

# sort the list in order and then write to the new file
# using loop to change list into ints from str
# then sort list of numbers
# sort list in ascending
# write to file as string


for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

numbers.sort()
print(numbers)

combined_files.write(str(numbers))

myfile.close()


