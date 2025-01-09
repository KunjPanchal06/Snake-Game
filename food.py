from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        RANDOM_X = random.randint(-280, 280)
        RANDOM_Y = random.randint(-280, 280)
        self.goto(RANDOM_X, RANDOM_Y)