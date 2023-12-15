from display import Custom_screen
from snake import Snake
from food import Food
import time


screen = Custom_screen()
snake = Snake()
food = Food()

screen.screen.listen()

screen.screen.onkey(snake.up, "w")
screen.screen.onkey(snake.down, "s")
screen.screen.onkey(snake.left, "a")
screen.screen.onkey(snake.right, "d")


Flag = True

while Flag:
  
  screen.screen.update()
  time.sleep(0.5)

  snake.move()
    

screen.screen.exitonclick()