"""
Feb 2021
@ Walter Seiffert
The basic structure of this program has been borrowed from the final project of Day 21
of Angela Yu's Python Bootcamp, as offered on the learning platform Udemy
(s. "100 Days of Code - The Complete Python Pro Bootcamp for 2021")
"""

import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def sketch_restart_button():
    """ sketch a restart button (placed beyond the 'game over' message, cf. the
    scoreboard class), that is: draw a rectangle and write 'Restart' in it """
    self = Turtle()
    self.hideturtle()
    self.color("white")
    self.penup()
    self.goto(-70, -60)
    self.pendown()
    for _ in range(2):
        self.forward(140)
        self.left(90)
        self.forward(40)
        self.left(90)

    self.penup()
    self.goto(-53, -54)
    self.write("Restart", font=("Courier", 20, "normal"))


def button_click(x, y):
    """ when the button is 'clicked', that is: a mouse event is trapped within
    the area of the button object, clear the screen from anything hitherto drawn
    on it and call the function play() again """
    if -70 < x < 70 and -60 < y < -20:
        screen.clearscreen()
        play()


def play():
    """ design the screen, create required objects, define key events that allow
    the player to control the movements of the snake figure, and implement the
    functional logic in a game loop """
    # setting the size/dimensions of the screen
    screen.setup(width=600, height=600)
    # setting the background colour of the screen
    screen.bgcolor("black")
    # setting a title for the screen
    screen.title("My Snake Game")
    screen.tracer(0)

    # add another turtle shape (= used for one of the food variants)    
    screen.addshape("diamond_pic.GIF")

    # creating the required objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # defining key events
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # --- GAME LOOP ---
    game_is_on = True
    while game_is_on:
        screen.update()   # refresh the screen
        time.sleep(0.1)   # wait for 0.1 sec

        # move the snake one step
        snake.move()

        # if the food appearing is a turtle, move it towards the right margin
        if food.variant == 4:
            food.speed("slow")
            food.forward(3)
            if not 280 > food.xcor() > -280 or not 280 > food.ycor() > -280:
                food.refresh()

        # detect any collision with a food object, update the scoreboard
        if snake.head.distance(food) < 15:        # distance in pixels
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect a collision with a wall --> trigger "game over"
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # detect a collision with the snake's tail -
        # if the head collides with any segment of the tail --> trigger "game over"
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    # prepare the restart of the game
    sketch_restart_button()
    screen.onscreenclick(button_click)
    screen.listen()

    screen.mainloop()


# --- START THE GAME ---
screen = Screen()
play()