# calculator.py

a = input("Enter the First Number: ")
a = float(a)
b = input("Enter the Second Number: ")
b = float(b)
x = input(" Enter the first letter of the operation of interest (a,s,m,d): ")



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



if x == "a":
        d = add(a,b)
elif x == "s":
        d = sub(a,b)
elif x == "m":
        d = mult(a,b)
elif x == "d":
        d = div(a,b)