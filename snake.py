import turtle as t

POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.turtles = []

    def createSnake(self):
        for position in POSITIONS:
            self.addSegment(position)

    def addSegment(self, position):
        turtle = t.Turtle()
        turtle.color("white")
        turtle.shape("square")
        turtle.penup()
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend(self):
        self.addSegment(self.turtles[-1].position())

    def move(self):
        for seg in range(len(self.turtles) - 1, 0, -1):
            newX = self.turtles[seg - 1].xcor()
            newY = self.turtles[seg - 1].ycor()
            self.turtles[seg].goto(newX, newY)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)