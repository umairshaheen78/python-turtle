'''
3/22/2021
Intro to Python Turtle

#1: import turtle library
import turtle

#2. Create a pen / turtle
variable1 = turtle.Turtle()

#3. Create a paper / screen
variable2 = turtle.Screen()

#4: Ways to move around the screen
    a. Move forward:
    variable1.foward(distance)
    variable1.fd(distance)

    b. Move backward:
    variable1.backward(distance)
    variable.bk(distance)

    c. Turn Right:
    variable1.right(angle)

    d. Turn left:
    variable1.left(angle)

    e. Pen up:
    variable1.penup()

    f. Pen Down:
    variable1.pendown()

    g. Go to home
    variable1.home()

    h. Go to a specific point
    variable1.goto(x,y)

import turtle

pen = turtle.Turtle() # Origin (0,0)
# Forward -->
pen.forward(100)      # (100,0)
# Backward <--
pen.backward(200)     # (-100, 0)
# Left <-- by 90 degrees
pen.left(90)
# Right --> by 180 degrees
pen.right(180)
# Left <-- by 1800 degrees (5 turns that are each 360 degrees)
pen.left(1800)

# Exericse 1: Draw a Window
import turtle
t1 = turtle.Turtle() 

t1.forward(100)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(100)

t1.circle(75)

# Exercise 2: Draw a house with a door
import turtle 
t = turtle.Turtle() 
  
# for creating base of 
# the house 
t.fillcolor('cyan') 
# I searched up if you can fill blocks of shapes, and there was a .fillcolor, so i used it! I only used it twice in my whole code, so yeah!
t.begin_fill() 
t.right(90) 
t.forward(250) 
t.left(90) 
t.forward(400) 
t.left(90) 
t.forward(250) 
t.left(90) 
t.forward(400) 
t.right(90) 
t.end_fill() 
  
# for top of 
# the house 
t.fillcolor('brown') 
t.begin_fill() 
t.right(45) 
t.forward(200) 
t.right(90) 
t.forward(200) 
t.left(180) 
t.forward(200) 
t.right(135) 
t.forward(259) 
t.right(90) 
t.forward(142) 
t.end_fill() 
  
# for door and 
# windows 
t.right(90) 
t.forward(400) 
t.left(90) 
t.forward(50) 
t.left(90) 
t.forward(150) 
t.right(90) 
t.forward(200) 
t.right(180) 
t.forward(200) 
t.right(90) 
t.forward(200) 
t.right(90) 
t.forward(150) 
t.right(90) 
t.forward(200) 
t.right(90) 
t.forward(150) 
t.right(90) 
t.forward(100) 
t.right(90) 
t.forward(150) 
t.right(90) 
t.forward(100) 
t.right(90) 
t.forward(75) 
t.right(90) 
t.forward(200) 
t.right(180) 
t.forward(200) 
t.right(90) 
t.forward(75) 
t.left(90) 
t.forward(15) 
t.left(90) 
t.forward(200) 
t.right(90) 
t.forward(15) 
t.right(90) 
t.forward(75) 
'''