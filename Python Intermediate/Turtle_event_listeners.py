from turtle import Turtle, Screen

var = Turtle()#accessingthe Turtle class
screen = Screen()#accessing the Screen class
var.shape("turtle")
var.color("deep pink")
var.penup()
screen.listen()#accessing the screen methods

def move_forward():
	var.forward(100)

screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()
