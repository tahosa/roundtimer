#!/usr/bin/python

import logging
import datetime
import time

import DrawThread

class Clock(DrawThread.DrawThread):

    def run(self):
        '''
        Update the time and the clock
        '''

        while True:
            # Break when given the exit signal
            if(self.stop.isSet()):
                return True

            # Update the time
            self.currentTime = datetime.datetime.now()
            timeStr = "{hr:02d}{colon}{mn:02d}".format(
                hr=self.currentTime.time().hour,
                mn=self.currentTime.time().minute,
                colon=":" if self.blink else " "
            )

            logging.debug("ClockTime - {0}".format(timeStr))

            # Set the colon to blink
            self.blink = (self.blink + 1) % 2

            # Redraw the time
            self._draw(timeStr, font=self._image.fontLg)

            time.sleep(1.0)

        return True

    def start(self):
        '''
        Initialize the data for the thread
        '''

        self.blink = 0
        self.run()
