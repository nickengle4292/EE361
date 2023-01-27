import turtle
from draw import *
from pi import *

turtle = turtle.Turtle()

turtle.up()
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.down()
drawPolygon(turtle, 100, 6)
turtle.up()
turtle.left(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(50)
turtle.down()
drawCircle(turtle, 100)

print(archimedes(1000))
print(leibniz(1000))
print(wallis(1000))
print(montePi(1000))