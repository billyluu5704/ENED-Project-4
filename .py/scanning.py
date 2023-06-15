#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

import Pickup
from Pickup import pickup
import main
from main import backontrack
# Initialize the EV3 screen

ev3 = EV3Brick()
m_left = Motor(Port.D)
m_right = Motor(Port.A)
robot = DriveBase(m_left, m_right, wheel_diameter = 56, axle_track = 100)
gyro = GyroSensor(Port.S1)
gyro.reset_angle(0)



US = UltrasonicSensor(Port.S2)

m_arm = Motor(Port.B)

CS = ColorSensor(Port.S4)
sp = 1000000000
a = 90
turn = 170
v = sp
robot.settings(-v, turn_rate = 360)

# IMPORTANT, "m.arm_run_angel(-30, 180)"
# makes the arm move about .5 inch

b1 = 5 * 25.4 + 3 * (3.5/100)
b2 = 11 * 25.4 + 9 * (3.5/100)
b3 = 17 * 25.4 + 15 * (3.5/100)
b4 = 23 * 25.4 + 21 * (3.5/100)
b5 = 29 * 25.4 + 27 * (3.5/100)
b6 = 35 * 25.4 + 33 * (3.5/100)

hoA = [6, -6]
sheA1 = [[12, 12], [12, 24], [48, 24], [48, 12]]
s = (sheA1[0][0] - hoA[0]) * 25.4 + (sheA1[0][0] - hoA[0]) * (3.5/100)
s1 = b1 + s
s2 = b2 + s
s3 = b3 + s
s4 = b4 + s
s5 = b5 + s
s6 = b6 + s


given_barcode = int(input("Enter the type of box you want to check: "))

#inputs
she = str(input("Enter which shelve (A1, A2, B1, B2, C1, C2, D1, D2): "))
while she != "A1" and she != "A2" and she != "B1" and she != "B2" and she != "C1" and she != "C2" and she != "D1" and she != "D2":
    print("Retry")
    she = str(input("Enter which shelve (A1, A2, B1, B2, C1, C2, D1, D2): "))

given_barcode = int(input("Enter the type of box you want to check: "))
while given_barcode < 1 and given_barcode > 4:
    print("Reenter\n")
    given_barcode = int(input("Enter the  type of box you want to check: "))

box = int(input("Enter number of box from 1 to 12: "))
while box >= 13 and box <= 0:
    box = int(input("Enter number of box from 1 to 12: "))


def tobox(b3):
    robot.straight(b3)
    robot.stop()
    m_left.brake()
    m_right.brake()

tobox(b3)


def scanBarcode(given_barcode):

    ev3 = EV3Brick()
    m_left = Motor(Port.D)
    m_right = Motor(Port.A)
    robot = DriveBase(m_left, m_right, wheel_diameter = 56, axle_track = 100)
    # Takes the barcode parameter and creates a
    # list that helps check for if it is the
    # right barcode
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
        #Code that moves to next block in barcode
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
        pickup()
    else:
        ev3.screen.print("WRONG BARCODE!")
        print("This is the wrong barcode")
        wait(2000)
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
    backontrack(s1, s2, s3, s4, s5, s6, box, gyro, she)
       

scanBarcode(given_barcode)
