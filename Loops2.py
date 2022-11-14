# Continuation of For Loops
friends = [1, 2, 3, 4, 5, 6, 7, 8]
for char in "SpongeBob":
    print(char)

maxim = 0
for value in friends:  # variable 'value' can be named anything (for-each loop)
    maxim = maxim + value

print(maxim)

# Nested For Loop (n^2 runtime)
for i in range(5):  # similar to for(int i = 0; i < 10; i++) in java
    for j in friends:
        maxim += 1
print(maxim)

# For loops that do not start at 0
summer = 0
for i in range(2, 10):  # i goes from 2 to 9
    summer += i
print(summer)
