import turtle
s = turtle.Turtle()
s.color("black")


size=0
while True:
    for i in range(4):
        s.fd(size+1)
        s.left(90)
        size=size-5
    size=size+1
turtle.done()