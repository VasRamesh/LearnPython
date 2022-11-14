# IF statements (program decision-making)
longer_tuple = (3, 7, 2, 3, 7)
if True:
    print("This will always run")
if 4 in longer_tuple:
    print("4")
elif 5 in longer_tuple:  # runs if first if-statement doesn't work
    print("5")
elif 6 in longer_tuple:
    print("6")
else:
    print("haha")  # only runs if no other if-statement ran

true = True
false = False

if true or false:  # one must be true to run
    print("one or the other")
if true and false:  # both must be true to run
    print("both must be true")
if true and not false:  # similar to != in java
    print("Goo")
if true == false:  # similar to == in java
    print("cap")


# Comparisons using if-statements
def largest_number(num1, num2, num3):
    maxi = num1
    if num1 < num2:
        maxi = num2
        if num2 < num3:
            maxi = num3
    elif num1 < num3:
        maxi = num3
    return maxi


print(largest_number(100, 10, 100))
