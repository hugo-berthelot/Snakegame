from turtle import Screen

class Custom_screen:

  def __init__(self):
    self.screen = Screen()
    self.screen.screensize(700, 700)
    self.screen.bgcolor("black")
    self.screen.title("The Good Old Snake Game")
    self.screen.tracer(0)