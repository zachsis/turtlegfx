import turtle
import math

spiral = turtle.Turtle()
spiral.lt(45)
spiral.width(width=1)
spiral.speed(speed=100)
spiral.screen.bgcolor("black")
spiral.pencolor("violet")

rainbow = ["blue", "indigo"]


def ok():
    lt = 1
    while True:
        for color in rainbow:
            spiral.pencolor(color)
            lt += 0.5
            spiral.lt(lt)
            for a in range(1):
                for i in range(1,333):
                    # spiral.forward(333)
                    spiral.forward(math.cos(i) * i / math.pi )
                    spiral.backward(i / math.pi)
                    spiral.right(72)
                spiral.penup()
                spiral.setposition(0, 0)
                spiral.pendown()

def main():
    while True:
        ok()

main()
