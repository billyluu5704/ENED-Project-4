#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
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
a = 90
b1 = 5 * 25.4 + 3 * (3.5/100)
b2 = 11 * 25.4 + 9 * (3.5/100)
b3 = 17 * 25.4 + 15 * (3.5/100)
b4 = 23 * 25.4 + 21 * (3.5/100)
b5 = 29 * 25.4 + 27 * (3.5/100)
b6 = 35 * 25.4 + 33 * (3.5/100)
m_arm.angle_limit = 180

#pick up the box
def pickup():
    while gyro.angle() < a:
        m_left.run(40)
        m_right.run(-60)
    robot.stop()
    m_left.brake()
    m_right.brake()
    wait(1000)
    robot.straight(-70)
    robot.stop()
    m_left.brake()
    m_right.brake()
    while US.distance() > 100:
        robot.drive(100,0)
    robot.stop()
    m_left.brake()
    m_right.brake()
    m_arm.run_target(500, 1850)
    m_arm.stop()
    while US.distance() > 44:
        robot.drive(100,0)
    robot.stop()
    m_left.brake()
    m_right.brake()
    wait(3000)
    m_arm.run_target(-500, -10)
    m_arm.hold()
    robot.straight(-144)
    robot.stop()
    m_left.brake()
    m_right.brake()
    
pickup()

def goback(a):
    while gyro.angle() > -a:
        m_left.run(-50)
        m_right.run(50)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)
    wait(1000)

goback(a)

#go to drop off point
def todrop(b4):
    robot.straight(b4)
    robot.stop()
    m_left.brake()
    m_right.brake()

todrop(b4)

#drop off the box
def drop():
    m_arm.run_target(500, 1800)
    m_arm.stop()
    robot.straight(-70)
    m_arm.run_target(-500, -10)
    m_arm.hold()

drop()