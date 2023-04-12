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
US = UltrasonicSensor(Port.S2)
US = UltrasonicSensor(Port.S2)
m_arm = Motor(Port.B)
CS = ColorSensor(Port.S4)

robot = DriveBase(m_left, m_right, wheel_diameter = 56, axle_track = 230)

sp = 1000000000
a = 86
turn = 175 
v = sp
m_arm.angle_limit = 180
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


#input
she = str(input("Enter which shelve (A1, A2, B1, B2, C1, C2, D1, D2): "))
while she != "A1" and she != "A2" and she != "B1" and she != "B2" and she != "C1" and she != "C2" and she != "D1" and she != "D2":
    print("Retry")
    she = str(input("Enter which shelve (A1, A2, B1, B2, C1, C2, D1, D2): "))

box = int(input("Enter number of box from 1 to 12: "))
while box >= 13 and box <= 0:
    box = int(input("Enter number of box from 1 to 12: "))

given_barcode = int(input("Enter the type of box you want to check: "))
while given_barcode <= 0 and given_barcode >= 5:
    print("Reenter\n")
    given_barcode = int(input("Enter the  type of box you want to check: "))

s = (sheA1[0][0] - hoA[0]) * 25.4 + (sheA1[0][0] - hoA[0]) * (3.5/100)
way = (hoB[0] - hoA[1]) * 25.4 + (hoB[0] - hoA[1]) * (3.5/100)

def turn_right(a, gyro):
    while gyro.angle() < a:
        m_left.run(100)
        m_right.run(-100)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)
    wait(1000)

def turn_left(a, gyro):
    while gyro.angle() > -a:
        m_left.run(-100)
        m_right.run(100)
    robot.stop()
    m_left.brake()
    m_right.brake()
    gyro.reset_angle(0)
    wait(1000)


def shelve(she, tp0, tp1, tp2, tp3, tp4, st1, s, gyro):
    if 1 <= box <= 6:
        robot.straight(tp0)
        robot.stop()
        m_left.brake()
        m_right.brake()
        turn_right(a, gyro)
        robot.straight(way)
        robot.stop()
        m_left.brake()
        m_right.brake()
        turn_right(a, gyro)
        robot.straight(tp0)
        robot.stop()
        m_left.brake()
        m_right.brake()
        turn_right(turn, gyro)
        #to turning points
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
        turn_left(a, gyro)
        robot.straight(s)
        robot.stop()
        m_left.brake()
        m_right.brake()
        #to shelves A1 or A2 or C1 or C2
        if she == "A1" or she == "A2" or she == "C1" or she == "C2":
            robot.straight(st1)
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
        turn_right(a, gyro)
        robot.straight(s)
        robot.stop()
        m_left.brake()
        m_right.brake()
        if she == "B1" or she == "B2" or she == "D1" or she == "D2":
            robot.straight(st1)
        robot.stop()
        m_left.brake()
        m_right.brake()
        
shelve(she, tp0, tp1, tp2, tp3, tp4, st1, s, gyro)

#Distance to the boxes
b1 = 3 * 25.4 + 3 * (3.5/100)
b2 = 9 * 25.4 + 9 * (3.5/100)
b3 = 15 * 25.4 + 15 * (3.5/100)
b4 = 21 * 25.4 + 21 * (3.5/100)
b5 = 27 * 25.4 + 27 * (3.5/100)
b6 = 33 * 25.4 + 33 * (3.5/100)


#to the box

def boxes(b1, b2, b3, b4, b5, b6, gyro, box): 
    if 1 <= box <= 6:
        if box == 6:
            robot.straight(b1 + 2)
        elif box == 5:
            robot.straight(b2 + 2)
        elif box == 4:
            robot.straight(b3 + 2)
        elif box == 3:
            robot.straight(b4 + 2)
        elif box == 2:
            robot.straight(b5 + 2)
        elif box == 1:
            robot.straight(b6 + 2)
        robot.stop()
        m_left.brake()
        m_right.brake()
    elif 7 <= box <= 12:
        if box == 7:
            robot.straight(b1 + 2)
        elif box == 8:
            robot.straight(b2 + 2)
        elif box == 9:
            robot.straight(b3 + 2)
        elif box == 10:
            robot.straight(b4 + 2)
        elif box == 11:
            robot.straight(b5 + 2)
        elif box == 12:
            robot.straight(b6 + 2)
        robot.stop()
        m_left.brake()
        m_right.brake()


boxes(b1, b2, b3, b4, b5, b6, gyro, box)

def pickup():
    wait(1000)
    robot.straight(-20)
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
    robot.straight(-70)
    robot.stop()
    m_left.brake()
    m_right.brake()

#scan the barcode
def scanBarcode(given_barcode):
    boxtype_1 = [True, False, False, False]
    boxtype_2 = [True, False, True, False]
    boxtype_3 = [True, True, False, False]
    boxtype_4 = [True, False, False, True]
    #sets a barcode list to the given boxtype
    if given_barcode == 1:
        g_barcode_list = boxtype_1
    if given_barcode == 2:
        g_barcode_list = boxtype_2
    if given_barcode == 3:
        g_barcode_list = boxtype_3
    if given_barcode == 4:
        g_barcode_list = boxtype_4
    #actual barcode scan
    barcode = [True, True, True, True]
    for i in range(4):
        if CS.color() == Color.BLACK:
            barcode[i] = True
            print("Black")
        else:
            barcode[i] = False
            print("White")
        robot.straight(12)
        robot.stop()
        m_left.brake()
        m_right.brake()
        wait(3000)
    #prints which barcode it scanned (does not tell whether or not its correct)
    if barcode == boxtype_1:
        print("The barcode is of type 1")
        ev3.screen.print("Barcode type 1")
    if barcode == boxtype_2:
        print("The barcode is of type 2")
        ev3.screen.print("Barcode type 2")
    if barcode == boxtype_3:
        print("The barcode is of type 3")
        ev3.screen.print("Barcode type 3")
    if barcode == boxtype_4:
        print("The barcode is of type 4")
        ev3.screen.print("Barcode type 4")
    wait(3000)
    if barcode == g_barcode_list:      
        ev3.screen.print("Correct BARCODE!")
        print("This is the correct barcode!")
        wait(2000)
        turn_right(a,gyro)
        pickup()
    else:
        ev3.screen.print("WRONG BARCODE!")
        print("This is the wrong barcode")
        wait(2000)
        turn_right(a, gyro)

scanBarcode(given_barcode)


s1 = b1 + s
s2 = b2 + s
s3 = b3 + s
s4 = b4 + s
s5 = b5 + s
s6 = b6 + s

#get back on track after picking up the box
def backontrack(s1, s2, s3, s4, s5, s6, box, gyro, she):
    if 1 <= box <= 6:
        if she == "A1" or she == "A2" or she == "C1" or she == "C2":
            turn_left(a, gyro)
        elif she == "B1" or she == "B2" or she == "D1" or she == "D2":
            turn_right(a, gyro)
    elif 7 <= box <= 12:
        if she == "A1" or she == "A2" or she == "C1" or she == "C2":
            turn_right(a, gyro)
        elif she == "B1" or she == "B2" or she == "D1" or she == "D2":
            turn_left(a, gyro)
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
        robot.stop()
        m_left.brake()
        m_right.brake()
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
        robot.stop()
        m_left.brake()
        m_right.brake()

backontrack(s1, s2, s3, s4, s5, s6, box, gyro, she)


def turning(a, gyro, she):
    if she == "A1" or she == "A2" or she == "D1" or she == "D2":
        turn_left(a, gyro)
        #robot.turn(-84)
    if she == "C1" or she == "C2" or she == "B1" or she == "B2":
        turn_right(a, gyro)
        #robot.turn(84)

turning(a, gyro, she)


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

#drop the box
def drop():
    m_arm.run_target(500, 1800)
    m_arm.stop()
    robot.straight(-70)
    robot.stop()
    m_left.brake()
    m_right.brake()

    m_arm.run_target(-500, -10)
    m_arm.hold()
    m_arm.stop()

drop()
   
sca = (hoC[1] - hoA[1]) * 25.4 + (hoC[1]- hoA[1]) * (3.5/100)
sdb = (hoD[1] - hoB[1]) * 25.4 + (hoD[1] - hoB[1]) * (3.5/100)
sba = (hoB[0] - hoA[0]) * 25.4 + (hoB[0] - hoA[0]) * (3.5/100)



def returntoA(sca, sdb, sba, she, gyro, a, turn):
    if she == "C1" or she == "C2" or she == "D1" or she == "D2":
        turn_right(turn, gyro)
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
            turn_right(a, gyro)
            robot.straight(sba)
        robot.stop()
        m_left.brake()
        m_right.brake()
        turn_right(turn, gyro)
    elif she == "B1" or she == "B2":
        turn_right(a, gyro)
        robot.straight(sba)
        robot.stop()
        m_left.brake()
        m_right.brake()
        turn_right(a, gyro)
    elif she == "A1" or she == "A2":
        turn_right(turn, gyro)

returntoA(sca, sdb, sba, she, gyro, a, turn)