# Classes & Objects: to store data that doesn't fit any primitive data type
class Car:
    def __init__(self, model, price, color, v8):  # Constructor for java
        self.model = model
        self.price = price
        self.color = color
        self.v8 = v8

    def get_model(self):
        return self.model

    def rare(self):
        if self.v8 is True and self.price > 10000:
            return True
        else:
            return False


# Use from Class&Object import Car to use class in other files
honda_accord = Car("Honda", 10000, "red", False)
print(honda_accord.color)  # Access specific object parameter values
print(honda_accord.rare())  # uses internal function of the class
print(honda_accord.get_model())
