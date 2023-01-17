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
# xf1 = txtf.index("q")  # first matched character
print(xf)
# print(xf1)


# isalnum()
txtIsl = "12e"
print(txtIsl.isalnum())  # check all the character in the string is number
print(txtIsl.isalpha())  # check all the character in the string is word
print(txtIsl.isdecimal())  # check all the character in the string is in 10 base
print(txtIsl.isdigit())  # Check if all the characters in the text are digits


# isidentifier()
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())  # True
print(b.isidentifier())  # True
print(c.isidentifier())  # False
print(d.isidentifier())  # False


# islower()
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())  # False
print(b.islower())  # True
print(c.islower())  # False


# isTitle()
txt = "Hello, And Welcome To My World!"
x = txt.istitle()  # Check if each word start with an upper case letter.
print(x)


# isupper()
txt = "THIS IS NOW!"
x = txt.isupper() # Check if all the characters in the text are in upper case
print(x)


# join()