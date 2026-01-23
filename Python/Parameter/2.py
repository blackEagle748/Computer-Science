import turtle

turtle.speed(0)

def dreieck(s, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(s)
        turtle.left(120)
    turtle.end_fill()



dreieck(100, "red")
turtle.left(90)
dreieck(100, "blue")
turtle.left(90)
dreieck(100, "green")
turtle.left(90)
dreieck(100, "yellow")
turtle.left(90)

turtle.done() 