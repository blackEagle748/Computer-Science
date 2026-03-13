import turtle as t  
t.hideturtle()
t.color("red","red")
t.begin_fill()
for _ in range(2):
  t.forward(150); t.left(90)
  t.forward(100);  t.left(90)
t.end_fill()
t.done()