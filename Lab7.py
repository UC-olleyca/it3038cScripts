#Lab7 By Corey Olley

#The plugin I am using is Turtle Graphics and it allows for creating many different shapes, drawings, animations, and small games.

from turtle import *

#Here I used turtles Window/Screen control functions to control the look of the screen and also control the animation speed.
bgcolor('purple')
bgpic("download.gif")
delay(2)

#This is the customizable pen function, it provides filling/color control, drawing states, and drawing control
color('blue', 'red')
begin_fill()
pensize(4)

#This shows use of the move and draw functions that Turtle Graphics makes possible. In other words this is how it draws.
while True:
    forward(300)
    left(150)
    right(10)
    if abs(pos()) < 1:
        break

while True:
    forward(-300)
    left(-150)
    right(-10)
    if abs(pos()) < 1:
        break

while True:
    forward(-2)
    left(2)
    right(-2)
    if abs(pos()) < 1:
        break
end_fill()
done()
#You can also see many ways Turtle Graphics by checking out my snakegame code as it using turtle graphics to function.