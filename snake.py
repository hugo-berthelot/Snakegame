from turtle import Turtle

class Snake:

  def __init__(self):
    
    x = 0
    self.snake = []
    
    for i in range(3):
      self.snake.append(Turtle())
      self.snake[i].shape("square")
      self.snake[i].color("white")
      self.snake[i].penup()
      self.snake[i].goto(x,0)
      x += 20


  def move(self):

    for i in range(len(self.snake)-1, 0, -1):
        new_coord  = self.snake[i-1].pos()
        self.snake[i].goto(new_coord)

    self.snake[0].forward(20)

  def up(self):
    if self.snake[0].heading() != 270:
      self.snake[0].setheading(90)
    
  def down(self):
    if self.snake[0].heading() != 90:
      self.snake[0].setheading(270)

  def left(self):
    if self.snake[0].heading() != 0:
      self.snake[0].setheading(180)

  def right(self):
    if self.snake[0].heading() != 180:
      self.snake[0].setheading(0)