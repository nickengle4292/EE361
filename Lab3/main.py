import turtle
from draw import *
from pi import *

turtle = turtle.Turtle()

drawPolygon(turtle, 100, 10)
drawCircle(turtle, 100)

print(archimedes(1000))
print(leibniz(1000))
print(wallis(1000))
print(montePi(1000))