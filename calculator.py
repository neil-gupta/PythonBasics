# calculator.py

def add(x,y):
    z = x + y
    print("{} + {} = {}".format(x,y,z))
    return z

def sub(x,y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))
    return z

def mult(x,y):
    z = x * y
    print("{} * {} = {}".format(x, y, z))
    return z

def div(x,y):
    z = x / y
    print("{} / {} = {}".format(x, y, z))
    return z


x = input("Enter a letter: ")
print("You entered {}".format(x))

y = input("Enter a second letter: ")

print("This is the second letter -- {}. This is a line of code.".format(y))

if x == "a":
        d = add(100,200)
        if d > 100:
            print("{} is too high!".format(d))
elif x == "s":
        d = sub(100,200)
        if d > 100:
            print("{} is too high!".format(d))
elif x == "m":
        d = mult(100,200)
        if d > 100:
            print("{} is too high!".format(d))
elif x == "d":
        d = div(100,200)
        if d > 100:
            print("{} is too high!".format(d))