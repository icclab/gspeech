#!/usr/bin/env python

# script that launches gspeech script by reading the state of a button
# pin connected to resistor is 48 (3.3v)
# pin connected to button is b_pin (GPIO)
# pin l_pin is a LED indicator for when gpseech script is running 

import mraa
import time
import subprocess
import os, sys
import rospy

# pin for button
b_pin = 35
# pin for LED 
l_pin = 100

# initialize GPIO pins 
button = mraa.Gpio(b_pin)
led = mraa.Gpio(l_pin)
print "Setting up GPIO pins"

# set button to input and LED to output 
button.dir(mraa.DIR_IN)
led.dir(mraa.DIR_OUT)
print "Setting up pin direction"

# Set initial value of button to be pulled low
button.mode(mraa.MODE_PULLDOWN)
print "Setting button pin mode to pulldown"

# continuously read the state of the button
while True:
    if button.read() == 1: #assert script is not running
        print("Button was pressed, initiating gspeech node...")
        os.system("roslaunch gspeech gspeech.launch")
        # 10 second delay before killing script 
        led.write(1)
    else:
        print("Button was not pressed")
        led.write(0)
    time.sleep(3)


