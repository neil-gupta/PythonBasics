#basics
x = input("Enter a letter: ")
print("You entered {}".format(x))

y = input("Enter a second letter: ")

print("This is the second letter -- {}. This is a line of code.".format(y))

if x == "a":
        a = 1
        b = 2
        c = a + b
        print("{} + {} = {}".format(a,b,c))
elif x == "s":
        a = 20
        b = -3
        c = a - b
        print("{} - {} = {}".format(a,b,c))
elif x == "m":
        a = 5
        b = 6
        c = a * b
        print("{} * {} = {}".format(a,b,c))
elif x == "yeet":
        a = "yah"
        b = "yuh"
        c = a + b
        print("{} + {} = {}".format(a,b,c))
else:
        print("The {} statement is not recognized".format(x))
print("DONE")