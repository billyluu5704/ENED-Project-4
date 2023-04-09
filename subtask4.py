#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
m_left = Motor(Port.D)
m_right = Motor(Port.A)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)
robot = DriveBase(m_left, m_right, wheel_diameter = 56, axle_track = 100)

US = UltrasonicSensor(Port.S2)

m_arm = Motor(Port.B)
total = 0
a = 83
b1 = 3 * 25.4 + 3 * (3.5/100)
b2 = 9 * 25.4 + 9 * (3.5/100)
b3 = 15 * 25.4 + 15 * (3.5/100)
b4 = 21 * 25.4 + 21 * (3.5/100)
b5 = 27 * 25.4 + 27 * (3.5/100)
b6 = 33 * 25.4 + 33 * (3.5/100)


def pickup():
    m_arm.run(-1000)
    wait(500)
    m_arm.stop()
    while US.distance() > 120:
        robot.drive(100,0)
    robot.stop()
    m_left.brake()
    m_right.brake()
    m_arm.run(1000)
    wait(3000)
    m_arm.hold()
    while US.distance() > 55:
        robot.drive(100,0)
    robot.stop()
    m_left.brake()
    m_right.brake()
    m_arm.run(-1000)
    wait(2500)
    m_arm.hold()
    
pickup()

def goback(a):
    robot.straight(-90)
    robot.stop()
    m_left.brake()
    m_right.brake()
    while gyro.angle() > -a:
        m_left.run(-50)
        m_right.run(50)
        wait(1000)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)

goback(a)

def todrop(b4):
    robot.straight(b4)
    robot.stop()
    m_left.brake()
    m_right.brake()

todrop(b4)

def drop():
    m_arm.run(1000)
    wait(2500)
    m_arm.stop()
    robot.straight(-60)
    m_arm.run(-1000)
    wait(1500)

drop()