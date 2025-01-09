import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)
game = False

snake = Snake()
food = Food()
scoreboard = Scoreboard()

snake.createSnake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.updateScore()

    if snake.turtles[0].xcor() > 300 or snake.turtles[0].xcor() < -300 or snake.turtles[0].ycor() > 300 or \
            snake.turtles[0].ycor() < -300:
        scoreboard.gameOver()
        game = False

    for turtle in snake.turtles:
        if turtle == snake.turtles[0]:
            pass
        elif snake.turtles[0].distance(turtle) < 10:
            scoreboard.gameOver()
            game = False

screen.exitonclick()