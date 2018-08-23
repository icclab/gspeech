#!/usr/bin/env python

# script that launches gspeech script by reading the state of a button
# pin connected to resistor is 48 (3.3v)
# pin connected to button is b_pin (GPIO)
# pin l_pin is a LED indicator for when gpseech script is running 

import mraa
import subprocess
import rospy

# pin for button
b_pin = 35

# pin for LED 
l_pin = 100

# initialize GPIO pins 
button = mraa.Gpio(b_pin)
led = mraa.Gpio(l_pin)
print("Setting up GPIO pins")

# set button to input and LED to output 
button.dir(mraa.DIR_IN)
led.dir(mraa.DIR_OUT)
print("Setting up pin direction")

# set initial value of button to be pulled low
button.mode(mraa.MODE_PULLDOWN)
print("Setting button pin mode to pulldown")

# declare gspeech cmd variable 
gcmd = None 

# assert LED is off
led.write(0)

# continuously read the state of the button
while True:
    if button.read() == 1 and not(hasattr('gcmd', 'pid')): #assert script is not already running
        print("Button was pressed, initiating gspeech node...")
        gcmd = subprocess.Popen(['roslaunch', 'gspeech', 'gspeech.launch'])
       
        # light indicating gspeech node is running
        led.write(1) 

        # record speech for 10 seconds then terminate node
        rospy.sleep(15)
        print("Done recording speech sample, terminating gspeech node..")
        gcmd.terminate()
        led.write(0)
        
    elif button.read() == 1 and gcmd.returncode == None: 
        print("Terminating gspeech node..")
        gcmd.terminate()
        led.write(0)

    rospy.sleep(0.2)


