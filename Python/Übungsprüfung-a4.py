import turtle as t

t.pencolor("blue")
t.penup()
def square():
    t.pendown()
    for i in range(4):
      t.forward(80)
      t.left(90)
    t.penup()
    t.forward(100)
    
for i in range(3):
  square()
t.hideturtle()
t.done()