from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """ constructor of a snake object """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ method to put together the segments of a snake object """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """ method to create a new snake segment and add it to the current segments list """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """ method to initialize another snake object if a round of the game has ended
        because of the snake colliding with a wall or with its own tail """
        for seg in self.segments:
            seg.goto(1000, 1000)     # move all segments of the current snake outside the screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def extend(self):
        """ method to make a snake object extend (by adding another segment) if the snake
        has collected a food """
        self.add_segment(self.segments[-1].position())    # position of the last segment

    def move(self):
        """ method to move a snake object forward by 20 pixels """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """ method to set the snake's direction of movement to 'up' (~ North) """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ method to set the snake's direction of movement to 'down' (~ South) """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ method to set the snake's direction of movement to 'left' (~ West) """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ method to set the snake's direction of movement to 'right' (~ East) """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
