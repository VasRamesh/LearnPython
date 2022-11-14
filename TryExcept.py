# Try and Except

try:
    num1 = input("Give me a number")  # Will return an error: go to except function
    num2 = input("Give me a second number")
    print(int(num1)/int(num2))
except ZeroDivisionError as err:  # Will run if try function returns an error # Only Catches ZeroDivisionError
    print("Cannot Divide by 0")
    print(err)
except ValueError:
    print("Invalid Input ")
