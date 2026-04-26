import turtle 
s=turtle.Turtle()

s.color("blue")


sides=6
sidelength=70
angle=360.0/sides

s.begin_fill()
s.pendown()

for i in range (0,sides):
    s.forward(sidelength)
    s.left(angle)

s.end_fill()

turtle.done()