import math
import turtle

from turtle import *

import colorsys
speed(0)
bgcolor('black')
pensize(2)
h=0.1
for i in range(250):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.1
    circle(i,100)
    rt(100)
    for j in range(4):
        rt(40)
done()

# 2

# t = turtle.Turtle()
# s = turtle.Screen().bgcolor('black')
# t.speed(0)
# n = 70
# h = 0
# for i in range(360):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h += 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for j in range(2):
#         t.left(2)
#         t.circle(140)

# turtle.bgcolor("black")
#
# squary = turtle.Turtle()
# squary.speed(20)
# squary.pencolor("red")
# for i in range(400):
#     squary.forward(i)
#     squary.left(91)
#
# turtle.bgcolor("black")
#
# squary = turtle.Turtle()
# squary.speed(200)
#
# for i in range(100):
#     for color in ["red","blue","yellow"]:
#         squary.pencolor(color)
#         squary.forward(i)
#         squary.right(60)







