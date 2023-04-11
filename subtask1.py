#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
m_left = Motor(Port.D)
m_right = Motor(Port.A)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)
US = UltrasonicSensor(Port.S2)

robot = DriveBase(m_left, m_right, wheel_diameter = 56, axle_track = 230)

sp = 1000000000
a = 90
v = sp
robot.settings(-v, turn_rate = 360)

hoA = [6, -6]
hoB = [102, -6]
hoC = [6, 114]
hoD = [102, 114]
sheA1 = [[12, 12], [12, 24], [48, 24], [48, 12]]
sheA2 = [[12, 36], [12, 48], [48, 48], [48, 36]]
sheB1 = [[60, 12], [60, 24], [96, 24], [96, 12]]
sheB2 = [[60, 36], [60, 48], [96, 48], [96, 36]]
sheC1 = [[12, 60], [12, 72], [48, 72], [48, 60]]
sheC2 = [[12, 84], [12, 96], [48, 96], [48, 84]]
sheD1 = [[60, 60], [60, 72], [96, 72], [96, 60]]
sheD2 = [[60, 84], [60, 96], [96, 96], [96, 84]]
s = (sheA1[0][0] - hoA[0]) * 25.4 + (sheA1[0][0] - hoA[0]) * (3.5/100)
tp1 = (sheA1[1][1] - hoA[1] + 6) * 25.4 + (sheA1[1][1] - hoA[1] + 6) * (10/100)

box = int(input("Enter number of box from 1 to 12: "))
while box >= 12 and box <= 7:
    box = int(input("Enter number of box from 1 to 12: "))

b1 = 3 * 25.4 + 3 * (3.5/100)
b2 = 9 * 25.4 + 9 * (3.5/100)
b3 = 15 * 25.4 + 15 * (3.5/100)
b4 = 21 * 25.4 + 21 * (3.5/100)
b5 = 27 * 25.4 + 27 * (3.5/100)
b6 = 33 * 25.4 + 33 * (3.5/100)

def turn_right(a, gyro):
    while gyro.angle() < a:
        m_left.run(50)
        m_right.run(-50)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)
    wait(1000)

def startofshelves(tp1, gyro):
    robot.straight(tp1)
    robot.stop()
    m_left.brake()
    m_right.brake()
    turn_right(a, gyro)

startofshelves(tp1, gyro)

def toboxes(b1, b2, b3, b4, b5, b6, gyro, box, s): 
    if box == 7:
        robot.straight(s+b1)
    elif box == 8:
        robot.straight(s+b2)
    elif box == 9:
        robot.straight(s+b3)
    elif box == 10:
        robot.straight(s+b4)
    elif box == 11:
        robot.straight(s+b5)
    elif box == 12:
        robot.straight(s+b6)
    robot.stop()
    m_left.brake()
    m_right.brake()

toboxes(b1, b2, b3, b4, b5, b6, gyro, box, s)

wait(3000)

def backtob(b1, b2, b3, b4, b5, b6, gyro,box, s):
    if box == 7:
        robot.straight(b5 + s * 2 + b6 + s + 1.5 * s)
    elif box == 8:
        robot.straight(b4 + s * 2 + b6 + s + 1.5 * s)
    elif box == 9:
        robot.straight(b3 + s * 2 + b6 + s + 1.5 * s)
    elif box == 10:
        robot.straight(b2 + s * 2 + b6 + s + 1.5 * s)
    elif box == 11:
        robot.straight(b1 + s * 2 + b6 + s + 1.5 * s)
    elif box == 12:
        robot.straight(s * 2 + b6 + s + 1.5 * s)
    robot.stop()
    m_left.brake()
    m_right.brake()
    turn_right(a, gyro)
    robot.straight(tp1)
    robot.stop()
    m_left.brake()
    m_right.brake()
    robot.turn(180)

backtob(b1, b2, b3, b4, b5, b6, gyro,box, s)

