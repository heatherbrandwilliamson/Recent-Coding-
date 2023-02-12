
# open file
f = open('DOB.txt', 'r+')
data = f.readlines()

# read contents and store as variable
# use the split function to seperate data


print("Name:")


for line in data:
    list = line.split()
    updated_list = (list[0:2])
    print(" ".join(updated_list))

print("\n")

print("Birthdate:")

f = open('DOB.txt', 'r+')

data = f.readlines()

# read contents and store as variable
# split function to seperate data
# read from item 2 onwards

for line in data:
    words = line.split()
    updated = (words[2:])
    print(" ".join(updated))






