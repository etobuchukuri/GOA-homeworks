from turtle import *


#we want to paint a house

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("green")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#penup 

penup()
goto(200,200)
pendown()

#drawing a roof

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing right window

penup()
goto(200,200)
pendown()

color("yellow")
begin_fill()
right(60)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

#2nd window
penup()
goto(0,200)
pendown()

color("yellow")
begin_fill()
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

exitonclick()