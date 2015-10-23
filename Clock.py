#!/usr/bin/python

import threading
import logging
import datetime
import time

import MatrixDraw

class Clock(threading.Thread):
    
    def run(self):
        while True:
            self.currentTime = datetime.datetime.now()
            logging.debug("ClockTime {0}:{1:02d} {2}".format(self.currentTime.time().hour, self.currentTime.time().minute, 'p'))
            time.sleep(1.0)
        return

    def draw(self):
    
