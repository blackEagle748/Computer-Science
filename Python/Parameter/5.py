import turtle

turtle.speed(0)
turtle.left(180)


def square(s, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(s)
        turtle.right(90)
    turtle.end_fill()

square(150, "red")
square(100, "blue")
square(50, "green")

turtle.done()