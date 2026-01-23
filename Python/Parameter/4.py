import turtle

def circle (r):
    turtle.fillcolor("cyan")
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

r = 100
turtle.left(90)
turtle.speed(0)

for i in range(30):
    circle(r)
    turtle.forward(10)
    r *= 0.9

turtle.done()