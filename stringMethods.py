# ! All string methods return new values. They do not change the original string.


# capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()  # capitalize just the first character.
print(x)


# casefold()
txt = "Hello, And Welcome To My World!"
y = txt.casefold()  # lower case all character in string
print(y)


# center()
txt = "banana"
z = txt.center(10)  # insert 10 space before & after word
xz = txt.center(10, "O")  # insert 10 "O" character before & after word
print(z)


# count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
x_limit = txt.count("apple", 10, 24)
print(x_limit)
print(x)


# encode()
txt = "My name is Ståle"
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))


# endwidth()
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")  # end width special character
print(x)

# expandtabs()
txt1 = "H\te\tl\tl\to"
xstr = txt1.expandtabs(6)  # set tab size
print(xstr)


# find()
# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txtf = "Hello, welcome to my world."
xf = txtf.find("welcome")  # first matched character
xf1 = txtf.index("q")  # first matched character
print(xf)
print(xf1)


# format()