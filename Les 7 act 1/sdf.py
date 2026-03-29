x=2
if (type(x)is int):
    print("true")
else:
    print("false")

x=2.4

if (type(x)is not float):
    print("false")
else:
    print("true")

x=20
y=20

if (x is y):
    print("x and y have SAME identity")

y=30

if (x is not y):
    print("x and y have DIFFERENT identity")
else:
    print("x and y have SAME identity")