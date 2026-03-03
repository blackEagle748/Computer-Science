import turtle

def stripe(color):
  t.fillcolor(color)
  t.begin_fill()
  for _ in range(2):
    t.forward(600)
    t.right(90)
    t.forward(100)
    t.right(90)
  t.end_fill()
  t.right(90)
  t.forward(100)
  t.left(90)

screen = turtle.Screen()
screen.setup(640, 360)
screen.title("Deutschlandflagge")

t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
t.penup()
t.goto(-300, 150)
t.pendown()

stripe("black")
stripe("red")
stripe("gold")

screen.mainloop()