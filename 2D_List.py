import random

# 2D List (arrays)
two_d_array = [[1, 2], [3, 4], [5, 6]]
rows = 5
columns = 5
empty_2d_array = [[random.random() for x in range(columns)] for y in range(rows)]  # creates an 10 * 20 2D array

# First 2D array visualized like:
#  1 , 2
#  3 , 4
#  5 , 6

# Accessing values:
print(two_d_array[0][1])  # Should return 2

for x in range(rows):  # Nested for-loop to print values in 2D array
    for y in range(columns):
        print(empty_2d_array[x][y])

print("GOO")
for row in empty_2d_array:  # Alternate way to iterate through 2D array
    for col in row:
        print(col)
