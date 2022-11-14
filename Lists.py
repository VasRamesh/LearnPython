# LISTS (Arrays)
names = ["Bob", "Sarah", "Johna", "Joe"]  # str List
ages = [1, 2, 3, 4]  # int List
all_over = ["Bob", 3, False, 7.0]  # Multiple datatypes in List

# List indices
print("names 2: " + names[2])
print(names[-2])  # Ordered backwards starting from -1
print(names[1:3])  # Select a multiple range of elements (Not including last one: from 1 to 2 inclusively)

# List functions
print(names)  # Print out entire list
names.extend(ages)  # adds ages list to names
names.extend(all_over)
names.append("Edgardo")  # appends an item to the 'names' list (end)
names.insert(1, "Joey")  # insert at a specific index (automatically pushes up other elements
names.remove("Bob")  # removes an element
names.pop()  # 'pops' the last element off the list
print(names.count(3))  # count number of times it appears
print(names)

# Find the index of an element
index_of_joe = names.index("Joe")
print(index_of_joe)

# Clear a list
names.clear()

# Sort list either in ascending order (alphabetical) or numerical (VERY POWERFUL)
integers = [3, 5, 4, 9, 2, 2, 5, 78, 4, 23, 7568]
integers.sort()
print(integers)

# Reverse a list
integers.reverse()
print(integers)

# Copy a list
copy_of_integers = integers.copy()
print(copy_of_integers)

# Tuple is a data structure that can store multiple values

coordinates = (2, 3)  # once created, a tuple cannot be changed or modified
print(coordinates[0])  # tuple data can be accessed with indices
print(coordinates[1])

longer_tuple = (3, 7, "Penis")

# Tuples are more niche - not used as often as lists

# Common list functions
list2 = list(range(10))  # creates a list from 0-9
char_list = list("String is a array of chars")
print(char_list)

# Accessing items in a list
index = 0
value_at_index = list2[index]  # accessing value via index
print(list2[0:7])  # accessing a range of indices
print(list2[::2])  # "step 2" = prints every other element in the list
print(list2[::-1])  # iterates the list in reverse order

for number in list2:
    print(number)

for number in enumerate(list2):  # Prints in index and value bc of enumerate object (tuple)
    print(number[0])  # print indices
    print(number[1])  # print values
    print(number)  # print tuple
for index, value in enumerate(list2):
    print(index, value)

# Adding and removing from a list
list2.append(10)  # append things to the end of a list
list2.remove(10)  # removes an item (not index)
index = 10
value = 50
list2.insert(index, value)  # insert at a specific index
del list2[index]  # del a value at an index (can also be a range with [x:y]

# Finding objects in a list
if 9 in list2:
    list2.index(9)  # returns the index at which 9 is stored at

print(list2)
