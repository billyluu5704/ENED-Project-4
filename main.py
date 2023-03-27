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

robot = DriveBase(m_left, m_right, wheel_diameter = 56, axle_track = 210)

sp = 1000000
a = 90
v = sp
robot.settings(v, turn_rate = 360)

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

#turning points
tp0 = (sheA1[0][1] - hoA[1] - 6) * 25.4 + (sheA1[0][1] - hoA[1] - 6) * (3.5/100)
tp1 = (sheA1[1][1] - hoA[1] + 6) * 25.4 + (sheA1[1][1] - hoA[1] + 6) * (3.5/100)
tp2 = (sheA2[1][1] - hoA[1] + 6) * 25.4 + (sheA2[1][1] - hoA[1] + 6) * (3.5/100)
tp3 = (sheC1[1][1] - hoA[1] + 6) * 25.4 + (sheC1[1][1] - hoA[1] + 6) * (3.5/100)
tp4 = (sheC2[1][1] - hoA[1] + 6) * 25.4 + (sheC2[1][1] - hoA[1] + 6) * (3.5/100) 

#straight to points
st1 = (sheB1[0][0] - sheA1[0][0]) * 25.4 + (sheB1[0][0] - hoA[0]) * (3.5/100)
st2 = (sheB2[0][0] - sheA2[0][0]) * 25.4 + (sheB2[0][0] - hoA[0]) * (3.5/100)
st3 = (sheD1[0][0] - sheC1[0][0]) * 25.4 + (sheD1[0][0] - hoA[0]) * (3.5/100)
st4 = (sheD2[0][0] - sheC2[0][0]) * 25.4 + (sheD2[0][0] - hoA[0]) * (3.5/100)
st5 = (sheD2[1][0] - sheC2[1][0]) * 25.4 + (sheD2[1][0] - hoA[0]) * (3.5/100)

she = str(input("Enter which shelve (A1, A2, B1, B2, C1, C2, D1, D2): "))
while she != "A1" and she != "A2" and she != "B1" and she != "B2" and she != "C1" and she != "C2" and she != "D1" and she != "D2":
    print("Retry")
    she = str(input("Enter which shelve (A1, A2, B1, B2, C1, C2, D1, D2): "))
box = int(input("Enter number of box from 1 to 12: "))
while box >= 13 and box <= 0:
    box = int(input("Enter number of box from 1 to 12: "))

s = (sheA1[0][0] - hoA[0]) * 25.4 + (sheA1[0][0] - hoA[0]) * (3.5/100)





def shelve(she, tp0, tp1, tp2, tp3, tp4, st1, st2, st3, st4, st5, s, gyro):
    if 1 <= box <= 6:
        if she == "A1" or she == "B1":
            robot.straight(tp0)
        elif she == "A2" or she == "B2":
            robot.straight(tp1)
        elif she == "C1" or she == "D1":
            robot.straight(tp2)
        elif she == "C2" or she == "D2":
            robot.straight(tp3)
        robot.stop()
        m_left.brake()
        m_right.brake()
        """ while gyro.angle() > -a:
            m_left.run(200)
            m_right.run(-200)
            wait(1000)
        gyro.reset_angle(0)
        robot.stop()
        m_left.brake()
        m_right.brake() """
        robot.turn(90)
        robot.stop()
        m_left.brake()
        m_right.brake()
        robot.straight(s)
        robot.stop()
        m_left.brake()
        m_right.brake()
        if she == "B1":
            robot.straight(st1)
        elif she == "B2":
            robot.straight(st2)
        elif she == "D1":
            robot.straight(st3)
        elif she == "D2":
            robot.straight(st4)
        robot.stop()
        m_left.brake()
        m_right.brake()
    elif 7 <= box <= 12:
        if she == "A1" or she == "B1":
            robot.straight(tp1)
        elif she == "A2" or she == "B2":
            robot.straight(tp2)
        elif she == "C1" or she == "D1":
            robot.straight(tp3)
        elif she == "C2" or she == "D2":
            robot.straight(tp4)
        robot.stop()
        m_left.brake()
        m_right.brake()
        """ while gyro.angle() > -a:
            m_left.run(200)
            m_right.run(-200)
            wait(1000)
        gyro.reset_angle(0)
        robot.stop()
        m_left.brake()
        m_right.brake() """
        robot.turn(90)
        robot.stop()
        m_left.brake()
        m_right.brake()
        robot.straight(s)
        robot.stop()
        m_left.brake()
        m_right.brake()
        if she == "B1":
            robot.straight(st2)
        elif she == "B2":
            robot.straight(st3)
        elif she == "D1":
            robot.straight(st4)
        elif she == "D2":
            robot.straight(st5)
        robot.stop()
        m_left.brake()
        m_right.brake()
        
shelve(she, tp0, tp1, tp2, tp3, tp4, st1, st2, st3, st4, st5, s, gyro)

#Coming to the chosen box
b1 = 3 * 25.4 + 3 * (3.5/100)
b2 = 9 * 25.4 + 9 * (3.5/100)
b3 = 15 * 25.4 + 15 * (3.5/100)
b4 = 21 * 25.4 + 21 * (3.5/100)
b5 = 27 * 25.4 + 27 * (3.5/100)
b6 = 33 * 25.4 + 33 * (3.5/100)


wait(2000)


def boxes(b1, b2, b3, b4, b5, b6, gyro, box): 
    if 1 <= box <= 6:
        if box == 1:
            robot.straight(b1)
        elif box == 2:
            robot.straight(b2)
        elif box == 3:
            robot.straight(b3)
        elif box == 4:
            robot.straight(b4)
        elif box == 5:
            robot.straight(b5)
        elif box == 6:
            robot.straight(b6)
        robot.stop()
        m_left.brake()
        m_right.brake()
        """ while gyro.angle() < a:
            m_left.run(-200)
            m_right.run(200)
            wait(1000)
        gyro.reset_angle(0)
        robot.stop()
        m_left.brake()
        m_right.brake() """
        robot.turn(-90)
        robot.stop()
        m_left.brake()
        m_right.brake()
    elif 7 <= box <= 12:
        if box == 7:
            robot.straight(b1)
        elif box == 8:
            robot.straight(b2)
        elif box == 9:
            robot.straight(b3)
        elif box == 10:
            robot.straight(b4)
        elif box == 11:
            robot.straight(b5)
        elif box == 12:
            robot.straight(b6)
        robot.stop()
        m_left.brake()
        m_right.brake()
        """ while gyro.angle() > -a:
            m_left.run(200)
            m_right.run(-200)
            wait(1000)
        gyro.reset_angle(0)
        robot.stop()
        m_left.brake()
        m_right.brake() """
        robot.turn(90)
        robot.stop()
        m_left.brake()
        m_right.brake()

boxes(b1, b2, b3, b4, b5, b6, gyro, box)

s1 = b1 + s
s2 = b2 + s
s3 = b3 + s
s4 = b4 + s
s5 = b5 + s
s6 = b6 + s

wait(2000)

#get back on track after picking up the box
def backontrack(s1, s2, s3, s4, s5, s6, box, gyro, she):
    if 1 <= box <= 6:
        if she == "A1" or she == "A2" or she == "C1" or she == "C2":
            """ while gyro.angle() < a:
                m_left.run(-200)
                m_right.run(200)
                wait(1000)
            gyro.reset_angle(0)
            robot.stop()
            m_left.brake()
            m_right.brake() """
            robot.turn(-90)
            robot.stop()
            m_left.brake()
            m_right.brake()
        elif she == "B1" or she == "B2" or she == "D1" or she == "D2":
            """ while gyro.angle() > -a:
                m_left.run(200)
                m_right.run(-200)
                wait(1000)
            gyro.reset_angle(0)
            robot.stop()
            m_left.brake()
            m_right.brake() """
            robot.turn(90)
            robot.stop()
            m_left.brake()
            m_right.brake()
    elif 7 <= box <= 12:
        if she == "A1" or she == "A2" or she == "C1" or she == "C2":
            """ while gyro.angle() > -a:
                m_left.run(200)
                m_right.run(-200)
                wait(1000)
            gyro.reset_angle(0)
            robot.stop()
            m_left.brake()
            m_right.brake() """
            robot.turn(90)
            robot.stop()
            m_left.brake()
            m_right.brake()
        elif she == "B1" or she == "B2" or she == "D1" or she == "D2":
            """ while gyro.angle() < a:
                m_left.run(-200)
                m_right.run(200)
                wait(1000)
            gyro.reset_angle(0)
            robot.stop()
            m_left.brake()
            m_right.brake() """
            robot.turn(-90)
            robot.stop()
            m_left.brake()
            m_right.brake()
    if she == "A1" or she == "A2" or she == "C1" or she == "C2":
        if box == 1 or box == 7:
            robot.straight(s1)
        elif box == 2 or box == 8:
            robot.straight(s2)
        elif box == 3 or box == 9:
            robot.straight(s3)
        elif box == 4 or box == 10:
            robot.straight(s4)
        elif box == 5 or box == 11:
            robot.straight(s5)
        elif box == 6 or box == 12:
            robot.straight(s6)
    if she == "B1" or she == "B2" or she == "D1" or she == "D2":
        if box == 1 or box == 7:
            robot.straight(s6)
        elif box == 2 or box == 8:
            robot.straight(s5)
        elif box == 3 or box == 9:
            robot.straight(s4)
        elif box == 4 or box == 10:
            robot.straight(s3)
        elif box == 5 or box == 11:
            robot.straight(s2)
        elif box == 6 or box == 12:
            robot.straight(s1)

backontrack(s1, s2, s3, s4, s5, s6, box, gyro, she)

wait(2000)

def turning(a, gyro, she):
    if she == "A1" or she == "A2" or she == "D1" or she == "D2":
        """ while gyro.angle() < a:
            m_left.run(-200)
            m_right.run(200)
            wait(1000)
        gyro.reset_angle(0)
        robot.stop()
        m_left.brake()
        m_right.brake() """
        robot.turn(-90)
        robot.stop()
        m_left.brake()
        m_right.brake()
    if she == "C1" or she == "C2" or she == "B1" or she == "B2":
        """ while gyro.angle() > -a:
            m_left.run(200)
            m_right.run(-200)
            wait(1000)
        gyro.reset_angle(0)
        robot.stop()
        m_left.brake()
        m_right.brake() """
        robot.turn(90)
        robot.stop()
        m_left.brake()
        m_right.brake()
    
turning(a, gyro, she)

wait(1000)

def waybackhome(she, box, tp0, tp1, tp2):
    if 1 <= box <= 6:
        if she == "A1" or she == "B1":
            robot.straight(tp0)
        elif she == "A2" or she == "B2" or she == "C2" or she == "D2":
            robot.straight(tp1)
        elif she == "C1" or she == "D1":
            robot.straight(tp2)
        robot.stop()
        m_left.brake()
        m_right.brake()
    elif 7 <= box <= 12:
        if she == "A1" or she == "B1" or she == "C1" or she == "D1":
            robot.straight(tp1)
        elif she == "A2" or she == "B2":
            robot.straight(tp2)
        elif she == "C2" or she == "D2":
            robot.straight(tp0)
        robot.stop()
        m_left.brake()
        m_right.brake()

waybackhome(she, box, tp0, tp1, tp2)
wait(1000)

turn = 180    
sca = (hoC[1] - hoA[1]) * 25.4 + (hoC[1]- hoA[1]) * (3.5/100)
sdb = (hoD[1] - hoB[1]) * 25.4 + (hoD[1] - hoB[1]) * (3.5/100)
sba = (hoB[0] - hoA[0]) * 25.4 + (hoB[0] - hoA[0]) * (3.5/100)

wait(2000)

def returntoA(sca, sdb, sba, she, gyro, a, turn):
    if she == "C1" or she == "C2" or she == "D1" or she == "D2":
        """ while gyro.angle() < turn:
            m_left.run(-200)
            m_right.run(200)
            wait(1000)
        gyro.reset_angle(0)
        m_left.brake()
        m_right.brake() """
        robot.turn(180)
        robot.stop()
        m_left.brake()
        m_right.brake()
        if she == "C1" or she == "C2":
            robot.straight(sca)
            robot.stop()
            m_left.brake()
            m_right.brake()
        elif she == "D1" or she == "D2":
            robot.straight(sdb)
            robot.stop()
            m_left.brake()
            m_right.brake()
            """ while gyro.angle() > -a:
                m_left.run(200)
                m_right.run(-200)
                wait(1000)
            gyro.reset_angle(0)
            m_left.brake()
            m_right.brake() """
            robot.turn(90)
            robot.stop()
            m_left.brake()
            m_right.brake()
            robot.straight(sba)
        robot.stop()
        m_left.brake()
        m_right.brake()
        """ while gyro.angle() < turn:
            m_left.run(-200)
            m_right.run(200)
            wait(1000)
        gyro.reset_angle(0)
        m_left.brake()
        m_right.brake() """
        robot.turn(180)
        robot.stop()
        m_left.brake()
        m_right.brake()
    elif she == "B1" or she == "B2":
        """  while gyro.angle() > -a:
            m_left.run(200)
            m_right.run(-200)
            wait(1000)
        gyro.reset_angle(0)
        m_left.brake()
        m_right.brake() """
        robot.turn(90)
        robot.stop()
        m_left.brake()
        m_right.brake()
        robot.straight(sba)
        robot.stop()
        m_left.brake()
        m_right.brake()
        """ while gyro.angle() > -a:
            m_left.run(200)
            m_right.run(-200)
            wait(1000)
        gyro.reset_angle(0)
        m_left.brake()
        m_right.brake() """
        robot.turn(90)
        robot.stop()
        m_left.brake()
        m_right.brake()
    elif she == "A1" or she == "A2":
        """ while gyro.angle() < turn:
            m_left.run(-200)
            m_right.run(200)
            wait(1000)
        gyro.reset_angle(0)
        m_left.brake()
        m_right.brake() """
        robot.turn(180)
        robot.stop()
        m_left.brake()
        m_right.brake()

returntoA(sca, sdb, sba, she, gyro, a, turn)