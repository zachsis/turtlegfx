import turtle
import math

spiral = turtle.Turtle()
spiral.lt(45)
spiral.width(width=1)
spiral.speed(speed=100)
spiral.screen.bgcolor("black")
spiral.pencolor("violet")

rainbow = ["purple", "indigo"]


def ok():
    lt = 1
    while True:
        for color in rainbow:
            spiral.pencolor(color)
            lt += 0.5
            spiral.lt(lt)
            for a in range(2):
                for i in range(900):
                    # spiral.forward(333)
                    spiral.forward(i / math.pi - a)
                    spiral.left(i / math.pi - a)
                    spiral.forward(i / math.pi - a)
                    spiral.right(i / math.pi - a)
                    spiral.forward(i / 2)
                    spiral.right(72)
                spiral.penup()
                spiral.setposition(0, 0)
                spiral.pendown()

def main():
    while True:
        ok()

main()