from turtle import Turtle
import random

DIRECTIONS = (0, 90, 180, 270)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.variant = 1
        self.penup()
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.variant = random.randint(1, 5)
        if self.variant == 1:
            self.shape("circle")
            self.color("yellow")
            self.shapesize(stretch_len=1, stretch_wid=0.4)
        elif self.variant == 2:
            self.shape("circle")
            self.color("red")
            self.shapesize(stretch_len=1, stretch_wid=1)
        elif self.variant == 3:
            self.shape("circle")
            self.color("blue")
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        elif self.variant == 4:
            self.shape("turtle")
            self.color("green")
            self.shapesize(stretch_len=1, stretch_wid=1)
        elif self.variant == 5:
            self.shape("diamond_pic.GIF")

        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.setheading(random.choice(DIRECTIONS))
