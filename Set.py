# HashSets (no duplicates, order doesn't matter) Similar to list

set1 = set([1, 2, 3, 4, 5])  # creates a set from a list
set2 = {1, 2, 3, 4, 5}  # alternate way to create set (cannot be empty - will create a dictionary)
set_empty = set([])  # empty set creation
print(set1)

# Set functions
set1.add(6)
set2.remove(5)
set2.discard(5)  # will not throw an error if the value doesn't exist in the set

# Update a set(add many values)
set1.update([3, 9, 32, 23, 15], set2)  # will add all these values to set1 (including set2)
print(set1)

# Intersection function (are the values shared between sets)
s1 = {12, 94, 189, 100}
s2 = {100, 189, 76, 3}
s3 = {93, 73, 189, 100, 4}
s4 = set(s1.intersection(s2, s3))  # create a new set with shared values between s1, s2, and s3
print(s4)

s5 = set(s1.difference(s2, s3))  # creates a new set with unshared values between s1, s2, and s3
print("s4: " + str(s4))

