from turtle import Turtle, Screen

'''
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
'''

turtle = Turtle()
turtle.hideturtle()


#==========================================================
# --- DIAMOND ---
# based on the design presented by user 'kashishmishra9911' at 
# https://www.geeksforgeeks.org/draw-diamond-shape-using-turtle-graphics-in-python/,
# with some necessary (minor) corrections 

# draw bigger triangle at the bottom 
turtle.left(60) 
turtle.forward(20) 
turtle.left(120) 
turtle.forward(20) 
turtle.left(120) 
turtle.forward(20) 
turtle.left(150) 

# draw three lines inside the bigger triangle 
turtle.forward(17.4)
turtle.backward(17.4)
turtle.left(16.5)
turtle.forward(18)
turtle.backward(18)
turtle.right(31.5)
turtle.forward(18)

turtle.right(75)

# draw upper triangle 1 
turtle.penup()
turtle.forward(5.3)
turtle.pendown()

turtle.left(120)
turtle.forward(5)
turtle.left(120)
turtle.forward(5)

# draw upper triangles 2,3,4
for n in range(3):
    turtle.right(120)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(5)

turtle.left(180) 
turtle.forward(5) 

# draw line above all upper triangles  
turtle.left(300) 
turtle.forward(15) 



#==========================================================
# --- BANANA ---

turtle.color("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-5, 0)
turtle.pendown()

turtle.color("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()



#==========================================================
# --- PLUM ---

def talloval(r):               # vertical Oval
    turtle.left(45)
    for _ in range(2):         # draws 2 halves of ellipse
        turtle.circle(r,90)    # long curved part
        turtle.circle(r/2,90)  # short curved part
# concerning this little function, the tribute goes to user 'Ollie', who 
# contributed the code at https://stackoverflow.com/questions/29465666/
# how-do-you-draw-an-ellipse-oval-in-turtle-graphics-python

# fruit
turtle.fillcolor("blue")
turtle.begin_fill()
talloval(10)
turtle.end_fill()

# leaf
turtle.penup()
turtle.goto(-3, 15)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(3, 180)
turtle.end_fill()
