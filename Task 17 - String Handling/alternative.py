

# store string as variable
# use a loop to go through each character
# use enumerate function
# use modulus if equal to zero
# use upper and lower function
# output result

print("Question 1:")
string = "My name is Heather and I am female"
result = ""

#for char in range
for i, char in enumerate(string):
    if i % 2 == 0:
        result += char.upper()
    else:
        result += char.lower()

print(result)

print("\nQuestion 2:")

string = "My name is Heather and I am female"
list = string.split(" ")

# for loop through the list
# user enumerate function
# modulus function
# print list as one line

for index, element in enumerate(list):

    if index % 2 == 0:
        list1 = element.lower()
        print(list1, end= ' ')
    else:
        list1 = element.upper()
        print(list1, end= ' ')


