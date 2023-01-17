a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())  # remove whitespace from the beginning or the end.
print(a.replace("H", "J")) # find char in first input and replace it with second input char
print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
aa = "Hello"
b = "World"
c = aa + b
print(c)


# String format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
