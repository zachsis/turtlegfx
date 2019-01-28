import turtle
import math

spiral = turtle.Turtle()
spiral.lt(180)
spiral.width(width=1)
spiral.speed(speed=100)

for a in range(1,333):

    for i in range(4):
        spiral.pencolor("blue")
        spiral.forward(a * math.pi)
        spiral.right(90)
        spiral.left(math.pi * i)

    for i in range(4):
        spiral.pencolor("red")
        spiral.forward(a * math.pi)
        spiral.right(90)
        spiral.left(-math.pi)
