#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)

	channels = [18,19,24,25]
    GPIO.setup(channels, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    for val in channels
    	GPIO.add_event_detect(val, GPIO.BOTH, callback=edge_callback(val))

    while True:
        time.sleep(0.16)

def edge_callback(channel):
    if(GPIO.input(channel)):
        print (channel+' Rising edge')
    else:
        print(channel+' Falling edge')
    
main()
