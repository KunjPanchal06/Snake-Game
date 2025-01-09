from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"Score : {self.score}", False, "center", ('Arial', 20, 'normal'))

    def updateScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ('Arial', 20, 'normal'))