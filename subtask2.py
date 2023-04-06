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

hoA = [6, -6]
hoB = [102, -6]

tp0 = (sheA1[0][1] - hoA[1] - 6) * 25.4 + (sheA1[0][1] - hoA[1] - 6) * (3.5/100)
way = (hoB[0] - hoA[0]) + (hoB[0] - hoA[0]) * (3.5/100)

def turn_left(a, gyro):
    while gyro.angle() > -a:
        m_left.run(-50)
        m_right.run(50)
        wait(1000)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)

def backtoA(tp0, way, gyro):
    robot.straight(tp0)
    robot.stop()
    m_left.brake()
    m_right.brake()
    turn_left(a, gyro)
    robot.straight(way)
    robot.stop
    m_left.brake()
    m_right.brake()
    turn_left(a, gyro)
    robot.straight(tp0)
    robot.stop()
    m_left.brake()
    m_right.brake()
    while gyro.angle() > -175:
        m_left.run(-50)
        m_right.run(50)
        wait(1000)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)

