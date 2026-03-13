from turtle import *

speed(-1)
left(90)

def dreieck():
  for i in range(3):
    forward(100)
    left(120)
  
for i in range(3):
  dreieck()
  forward(100)

hideturtle()
done()