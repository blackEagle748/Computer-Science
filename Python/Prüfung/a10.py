from turtle import *

penup()
speed(-1)
back(200)
right(90)



color = ["red", "yellow", "green", "blue"]



def dreieck():
  for i in range(3):
    pendown()
    forward(100)
    left(120)
    penup()



def dreieckeReihe():
  for i in range(4):
    
    fillcolor(color[i])
    pencolor(color[i])

    begin_fill()

    dreieck()

    end_fill()

    forward(50)
    left(90)
    forward(110)
    right(90)
    back(50)



dreieckeReihe()

hideturtle()
done()