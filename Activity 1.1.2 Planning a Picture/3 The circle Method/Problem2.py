import turtle as trtl
painter = trtl.Turtle()

painter.pensize(5)
painter.penup()
painter.forward(60)
painter.left(75)
painter.pendown()
painter.circle(100,360,5)
painter.penup()
painter.right(45)
painter.backward(180)
painter.left(90)
painter.forward(65)
painter.right(90)
painter.right(65)
painter.forward(40)
painter.pendown()
painter.circle(100,360,5)

wn = trtl.Screen()
wn.mainloop()