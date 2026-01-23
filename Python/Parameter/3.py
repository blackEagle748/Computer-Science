import turtle

turtle.speed(0)

def circle (r, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


circle(150, "red")
circle(120, "blue")
circle(90, "green")

turtle.done()