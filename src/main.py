# ! Float can also be scientific numbers with an "e" to indicate the power of 10.
# ? Note: You cannot convert complex numbers into another number type.


i = 1
while i < 6:
    print(i)  # 1 2 3
    if i == 3:
        break
    i += 1


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)  # 1 2 4 5 6

for x in range(2, 30, 3):
    print(x)  # loop 2 to 30 with 3 steps


'''----------------------------------------'''
'''                  Function              '''
'''----------------------------------------'''


def my__function(fname):  # fname param
    print(fname + " Refsnes")


my__function("Emil")  # "Emil" arg
my__function("Tobias")
my__function("Linus")


# send multiple value to function
def MyFunc(*kids):
    print("The youngest child is " + kids[2])


MyFunc("Emil", "Tobias", "Linus")


def my___function(**kid):  # If the number of keyword arguments is unknown
    print("His last name is " + kid["lname"])


my___function(fname="Tobias", lname="Refsnes")


# passing a list
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# function with no body
def myfunction():
    pass





'''----------------------------------------'''
'''            Lambda  Function            '''
'''----------------------------------------'''
# like arrow func in js
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))