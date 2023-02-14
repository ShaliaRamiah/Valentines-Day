import turtle
import time
turtle.bgcolor("black") 
# Creating a turtle object(draw)
draw = turtle.Turtle()
draw.pencolor("red")
# Defining a method to draw bend
def bend(x):
 for i in range(x):
  draw.right(1)
  draw.forward(2*1) 
# Defining method to draw a heart
def heart(): 
 draw.fillcolor('red')
 draw.begin_fill()
 draw.left(140)
 draw.forward(2*113)
 bend(200)
 draw.end_fill()
 draw.pencolor("#FF00E4")
 draw.fillcolor('#FF00E4')
 draw.begin_fill()
 draw.left(120)
 bend(200)
 draw.forward(2*112)
 draw.end_fill()
# Defining method to write text
def write():
 draw.up()
 draw.setpos(-2*68, 2*95)
 #draw.down()
 draw.color('#FF00E4')
 draw.write("Will you be ", font=( "Verdana", 14, "bold"))
 draw.setpos(10, 2*95)
 draw.color('red')
 draw.write("my Valentine?", font=( "Verdana", 14, "bold"))
 draw.ht()
heart()
write()
t=input()
# https://weirdtechie.com/python-code/