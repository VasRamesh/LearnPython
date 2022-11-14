# Dictionaries: (key,value) pairs <- Known as hashmaps
prevMap = {
    2: 0,
    3: 3,
    "Penis": 9,
    "statement": True,
    39.492: "Lebron",
}

# All keys must be unique (values do not have to be)
newMap = {"Jan": 100, "Feb": 200, "March": 300}

# Accessing values using keys
print(newMap["Jan"])  # Prints the value associated with the key
print(newMap.get("May", "Not a valid Key"))  # Similar to [] function (returns second value if nothing is found)

# Hashmap: Unordered, Mutable (No indices)
emptyMap = {}
emptyMap2 = dict(key="value", key2="value")  # Diff way to create dictionary
print(type(emptyMap2["key"]))  # Access a value based on the key
print(emptyMap2)

# Common functions for dictionaries
emptyMap2["New_key"] = "New_value"  # adding or accessing values in a dictionary (Only 1 key per 1 value)
del emptyMap2["key"]  # Delete a key-value pair
emptyMap2.pop("key2")  # Removes and returns the key-value pair

if "New_key" in emptyMap2:  # Check to see if dictionary contains a key (Can also use try-except statements)
    print("New_Key is in emptyMap2")

for key in emptyMap2:  # Iterate through a dictionary (with for:each loop)
    print(key)
    print(emptyMap2[key])

list10 = emptyMap2.keys()  # List of keys
print(list10)

emptyMap2_copy = emptyMap2.copy()  # creates a copy of the dict
emptyMap2_copy1 = dict(emptyMap2)  # alternate way to copy

emptyMap2.update(newMap)  # update/merge two dictionaries into emptyMap2
