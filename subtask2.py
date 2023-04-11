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

tp0 = (sheA1[0][1] - hoA[1] - 6) * 25.4 #+ (sheA1[0][1] - hoA[1] - 6) * (3.5/100)
way = (hoB[0] - hoA[0]) * 25.4 + (hoB[0] - hoA[0]) * (3.5/100)

def turn_left(a, gyro):
    while gyro.angle() > -a:
        m_left.run(-50)
        m_right.run(50)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)
    wait(1000)

def subtask2(tp0, way):
    robot.straight(tp0)
    robot.stop()
    m_left.brake()
    m_right.brake()
    turn_left(a, gyro)
    robot.straight(way)
    robot.stop()
    m_left.brake()
    m_right.brake()
    turn_left(a, gyro)
    robot.straight(tp0)
    robot.stop()
    m_left.brake()
    m_right.brake()
    while gyro.angle() > -170:
        m_left.run(-50)
        m_right.run(50)
        wait(1000)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)


subtask2(tp0, way)
