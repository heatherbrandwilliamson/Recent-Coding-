# request user input
# store variables
# run for loop with a counter plus one
# print output

i = int(input("Enter a number:"))
count = 0

for x in range(1, 13):
    count = count + 1
    print(f"{i} * {count} = {i * count}")
