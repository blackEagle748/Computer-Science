import turtle

def draw_colored_hexagon(side_length=100):
  colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
  t = turtle.Turtle()
  t.speed('normal')
  t.pensize(3)

  for color in colors:
    t.pencolor(color)
    t.forward(side_length)
    t.left(60)

if __name__ == '__main__':
  draw_colored_hexagon(120)
  turtle.done()