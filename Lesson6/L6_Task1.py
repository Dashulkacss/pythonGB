import turtle as t
from time import sleep


class TrafficLight:

    def __init__(self, color="black"):
        self.__color = color

    def running(self, counter):
        while counter > 0:
            self.__color = "red"
            circle(50, 150, 25, self.__color)
            circle(50, 100, 25, 0)
            circle(50, 50, 25, 0)
            sleep(7)
            self.__color = "yellow"
            circle(50, 150, 25, 0)
            circle(50, 100, 25, self.__color)
            # circle(50, 50, 25, 0)
            sleep(2)
            self.__color = "green"
            circle(50, 100, 25, 0)
            circle(50, 50, 25, self.__color)
            sleep(7)
            counter -=1


t.screensize(800, 800)


def circle(x, y, r, color):
    t.up()
    t.goto(x, y - r)
    t.down()
    t.fillcolor("black")
    if color == "red":
        t.fillcolor("red")
    if color == "yellow":
        t.fillcolor("yellow")
    if color == "green":
        t.fillcolor("green")
    t.begin_fill()
    t.circle(r, 360)
    t.end_fill()


traffic = TrafficLight()
traffic.running(2)

