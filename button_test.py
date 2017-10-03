#!/usr/bin/python

import RPi.GPIO as GPIO
import time

channels = {18:False, 19:False, 24:False, 25:False}

def main():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(channels.keys(), GPIO.IN, pull_up_down=GPIO.PUD_UP)

    for val in channels.keys():
        GPIO.add_event_detect(val, GPIO.FALLING, callback=edge_callback)

    while True:
        time.sleep(0.16)

def edge_callback(channel):
    if(not GPIO.input(channel) and channels[channel] == False):
        channels[channel] = True
        print ("%d Pressed" %(channel))
        sleeping_timer = 0
        #pause/unpause/start
        while (not GPIO.input(channel)): 
            time.sleep(0.1)
            sleeping_timer += 1
            if (sleeping_timer < 8):
                print ("%d Pause/Unpause" %(channel))
            elif (sleeping_timer < 25):    
                print ("%d Reset" %(channel))
                #reset timer
            else:
                print ("%d Off" %(channel))
                #turn off timer
        channels[channel] = False
    
main()
