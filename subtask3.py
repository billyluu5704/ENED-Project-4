#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


# Initialize the EV3 screen

ev3 = EV3Brick()
m_left = Motor(Port.D)
m_right = Motor(Port.A)
robot = DriveBase(m_left, m_right, wheel_diameter = 56, axle_track = 100)




US = UltrasonicSensor(Port.S2)

m_arm = Motor(Port.B)

CS = ColorSensor(Port.S3)

# IMPORTANT, "m.arm_run_angel(-30, 180)"
# makes the arm move about .5 inch



def scanBarcode(given_barcode):

    ev3 = EV3Brick()
    m_left = Motor(Port.D)
    m_right = Motor(Port.A)
    robot = DriveBase(m_left, m_right, wheel_diameter = 56, axle_track = 100)

    US = UltrasonicSensor(Port.S2)

    m_arm = Motor(Port.B)

    CS = ColorSensor(Port.S3)
    # Sets poistion of arm
    # and moves robot close to box

    # Takes the barcode parameter and creates a
    # list that helps check for if it is the
    # right barcode
    boxtype_1 = [False, False, False, True]
    boxtype_2 = [False, True, False, True]
    boxtype_3 = [False, False, True, True]
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


        robot.straight(10)
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
        return True
       

    else:

        ev3.screen.print("WRONG BARCODE!")
       

        print("This is the wrong barcode")
        wait(2000)
        return False        
   
    wait(10000)


#robot moves straight to where the box is
robot.straight(300)

#robot scans barcode and prints
scanbarcode(2)