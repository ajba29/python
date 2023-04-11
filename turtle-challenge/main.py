# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# for line in range (4):
#     t.circle(20)
#     t.fd(100)
#     t.rt(90)
#
# turtle.done()

from turtle import *

timmy = Turtle()
jack = Turtle()

for t in range (4):
    timmy.fd(100)
    timmy.rt(90)

jack.rt(180)
for j in range (4):
    jack.fd(100)
    jack.rt(-90)

Screen()
done()
