# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
# then draw a circle
painter.pensize(3)
painter.fillcolor("lightblue")
painter.begin_fill()
painter.circle(70,360)
painter.end_fill()
# move the turtle to another part of the screen
painter.penup()
painter.goto(0,-170)

# change both the pen and fill colors
# then draw a polygon of your choice
painter.pensize(5)
painter.fillcolor("yellow")
painter.pendown()
painter.begin_fill()
painter.circle(80,360,6)
painter.end_fill()
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()