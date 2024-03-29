from turtle import Turtle, Screen
import time
from random import randint
from snake import Snake
 
varscreen = Screen()
varscreen.bgcolor("black")
varscreen.title("cee_amOby-Snake-Game!")
varscreen.setup(1200, 800)
varscreen.tracer(0)

snake = Snake()

#creating the wall
wall = Turtle()
wall.shape("square")
wall.color("pink")
wall.ht()
wall.penup()
wall.goto(-590, 0)
wall.pendown()
wall.pencolor("pink")
wall.pensize(11)
wall.setheading(90)
wall.forward(390)
wall.setheading(0)
wall.forward(1170)
wall.setheading(270)
wall.forward(770)
wall.setheading(180)
wall.forward(1170)
wall.setheading(90)
wall.forward(390)
wall.penup()
wall.setheading(0)
wall.forward(100)
wall.pendown()
wall.setheading(90)
wall.forward(280)
wall.setheading(0)
wall.forward(100)
wall.setheading(270)
wall.forward(100)
wall.setheading(0)
wall.forward(150)
wall.penup()
wall. forward(100)
wall.pendown()
wall.setheading(90)
wall.forward(100)
wall.setheading(180)
wall.forward(80)
wall.penup()
wall.setheading(0)
wall.forward(200)
wall.pendown()
wall.forward(400)
wall.setheading(270)
wall.forward(80)
wall.setheading(0)
wall.forward(70)
wall.setheading(270)
wall.penup()
wall.forward(120)
wall.setheading(180)
wall.pendown()
wall.forward(300)
wall.setheading(270)
wall.forward(150)
wall.setheading(0)
wall.penup()
wall.forward(100)
wall.pendown()
wall.forward(200)
wall.setheading(90)
wall.forward(150)
wall.penup()
wall.setheading(270)
wall.forward(150)
wall.pendown()
wall.forward(100)
wall.setheading(180)
wall.forward(850)
wall.penup()
wall.forward(100)
wall.pendown()
wall.forward(90)
wall.penup()
wall.setheading(270)
wall.forward(110)
wall.setheading(0)
wall.pendown()
wall.forward(500)
wall.penup()
wall.forward(100)
wall.setheading(270)
wall.pendown()
wall.forward(110)
wall.setheading(90)
wall.penup()
wall.forward(110)
wall.setheading(0)
wall.pendown()
wall.forward(450)
wall.penup()
wall.goto(-100, 80)
wall.pendown()
wall.setheading(180)
wall.forward(200)
wall.setheading(270)
wall.forward(150)
wall.setheading(0)
wall.forward(300)
wall.setheading(90)
wall.penup()
wall.forward(250)
wall.pendown()
wall.forward(210)

#random things
new_x = randint(-500, 500)
new_y = randint(-300, 300)

#creating the food
food = Turtle()
food.shape("circle")
food.color("blue")
food.penup()
food.shapesize(0.8, 0.8)
food.speed("fastest")

#creating a score board
score = 0
board = Turtle()
board.ht()
        
game = True
while game:
    varscreen.update()
    time.sleep(0.4)
    
    snake.move()

varscreen.listen()
varscreen.onkey(snake.forward, "Right")
varscreen.onkey(snake.backward, "Left")
varscreen.mainloop()
    
varscreen.exitonclick()
