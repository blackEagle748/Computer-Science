import turtle

turtle.speed(1)

turtle.color("blue")

for i in range(8):
    turtle.fd(100)
    turtle.dot(20)
    turtle.bk(100)
    turtle.rt(45)

turtle.done()