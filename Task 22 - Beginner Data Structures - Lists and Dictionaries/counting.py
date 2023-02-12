# count the number of times a character appears in a string
# char frequency

# store each letter followed by number of occurrences in a dictionary
# store word/ sentence in a variable
# set up dictionary


sentence1 ="google.com"
count = {}
for i in sentence1:
    if i in count:
        count[i.lower()] = count[i.lower()] + 1
    else:
        count[i.lower()] = 1
print(count)

