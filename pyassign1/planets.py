#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does.

__author__ = "Xuefeng Wang"
__pkuid__  = "1800011707"
__email__  = "1800011707@pku.edu.cn"
"""

import turtle
import math
wn = turtle.Screen()
sun = turtle.Turtle()
mercury = turtle.Turtle()
venus = turtle.Turtle()
earth = turtle.Turtle()
mars = turtle.Turtle()
jupiter = turtle.Turtle()
saturn = turtle.Turtle()

def start(t, distance, color):
    """规定了各行星的近日点为起始点，t代表相应的行星，distance代表近日点距离太阳的距离，color代表相应行星轨道的表示颜色
    """
    t.shape("circle")
    t.speed(0)
    t.color(color)
    t.up()
    t.fd(distance)
    t.down()

def orbit():
    """轨道函数，coefficient与轨道周期成正比，a与半长轴成正比，e为离心率，b与半短轴成正比（与a相对应），利用椭圆参数方程表达了行星的坐标
    """
    for i in range(10000):
        coefficient = [87.7, 224.7, 365.2, 687.0, 4332.7, 10759.5]
        angle = 720*(i//6)/(coefficient[i%6])
        a_ = [19.5, 36, 50, 75, 260, 475]
        a = a_[i%6]
        e_ = [0.206, 0.007, 0.017, 0.093, 0.048, 0.056]
        e = e_[i%6]
        b = a*math.sqrt(1-e**2)
        planet = [mercury, venus, earth, mars, jupiter, saturn]
        pl = planet[i%6]
        pl.goto(a*math.cos(math.radians(angle))-a*e, b*math.sin(math.radians(angle)))

def main():
    """main 模块
    """
    start(sun, 0, "yellow")
    start(mercury, 15.483, "blue")
    start(venus, 35.748, "green")
    start(earth, 49.15, "red")
    start(mars, 68.025, "black")
    start(jupiter, 247.52, "orange")
    start(saturn, 448.4, "light blue")
    orbit()

if __name__ == '__main__':
    main()
turtle.done()
