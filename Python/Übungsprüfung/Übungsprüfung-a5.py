import turtle as t

t.speed(-1)
t.left(90)

def dreieck():
  for i in range(3):
    t.forward(100)
    t.left(120)
  
for i in range(3):
  dreieck()
  t.forward(100)

t.hideturtle()
t.done()