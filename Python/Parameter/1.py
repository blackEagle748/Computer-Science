import turtle

# Funktion zum Zeichnen eines Quadrats
def square(s):
    for _ in range(4):
        turtle.forward(s)
        turtle.right(90)

# Setup
turtle.speed(0) 
turtle.left(90)

# Startlänge
size = 180

# Zeichne 100 Quadrate
for _ in range(100):
    square(size)
    size *= 0.95  # verkleinere die Seitenlänge um 5%
    turtle.left(10)

# Beende Turtle beim Klicken
turtle.done()
