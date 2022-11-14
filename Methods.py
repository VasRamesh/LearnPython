# Functions (similar to methods in java)
def say_hi(name):  # name is the parameter of this function
    print("Hello " + str(name) + "!")


say_hi("bob")
say_hi(1)  # because of str() cast in function, parameter can be any data type

ex_bool = False
say_hi(ex_bool)  # lol it is printing a boolean


# Functions with returns
def num_cuber(number):
    return number ** 3


print(num_cuber(9))

