#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(18, GPIO.BOTH, callback=edge_callback)

    while True:
        time.sleep(0.16)

def edge_callback(channel):
    if(GPIO.input(channel)):
        print ('Rising edge')
    else:
        print('Falling edge')
    
main()
