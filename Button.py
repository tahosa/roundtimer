#!/usr/bin/python

import threading
import RPi.GPIO as GPIO
import time
import logging

class Button(threading.Thread):

    def __init__(self, channel, timerThread):
        super(Button, self).__init__()
        self.channel = channel
        self.depressed = False
        self.timer = timerThread
        self.stop = threading.Event()

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.channel, GPIO.FALLING, callback=self.edge_callback)

        while True:
            self.stop.wait()
            logging.info("Stopping thread")
            break
        return True

    def edge_callback(self, channel):
        if not GPIO.input(channel) and not self.depressed:
            self.depressed = True
            self.timer.pause.clear() if self.timer.pause.isSet() else self.timer.pause.set()
            counter = 0
            while not GPIO.input(channel): 
                time.sleep(0.1)
                counter += 1
                if (counter == 8):
                    self.timer.reset()
                elif (counter == 25):    
                    self.timer.off()
            self.depressed = False
    
