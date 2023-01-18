# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# we can have duplicate data item in list


thislist = ["apple", "banana", "cherry"]
print(len(thislist))  # get length of list


# NOTE: The search will start at index 2 (included) and end at index 5 (not included).
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # ['cherry', 'orange', 'kiwi']

# Condition true
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
