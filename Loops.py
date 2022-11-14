# While loops
i = 0
while i < 9:  # will run from i = 0 to i = 899
    print(i)
    i = i + 1  # i++ in java is i+=1

# For loops (Iterates from 0 to range-1)
ages = [1, 59, 3, 58]
names = ["Pee", "poo", "goo", "gaa"]

for x in range(6):  # x is a variable, range(6) is a collection
    print(x)

print("NEW LINE")
for i in ages:
    print(i + 3)

count = 0
for i in names:
    if i.__contains__("a"):  # Custom method (signaled by the __x__)
        count = count + 1
        print(str(count) + " hi")
