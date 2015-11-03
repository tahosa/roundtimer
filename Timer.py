#!/usr/bin/python

import logging
import time

import DrawThread

class Timer(DrawThread.DrawThread):
    def __init__(self, image, size, minutes=50, position=(0,0), offset=(0, 0), color=(255,255,255,255)):
        super(Timer, self).__init__(image, size, position, offset, color)
        self._time = 60 * minutes
        self._countdown = self._time
        self._blink = 0

    def run(self):
        '''
        Update the time left on the timer
        '''

        while True:
            # Break when given the exit signal
            if(self.stop.isSet()):
                return True
                
            # If the pause signal is given, block until it clears
            if(not self.pause.isSet()):
                self.pause.wait()

            # Update the timer
            if(self._countdown > 0):
                self._countdown -= 1

                # Compute minuntes and seconds
                minutes = self._countdown / 60
                seconds = self._countdown % 60

                timeStr = "{mn:02d}:{sc:02d}".format(
                    mn=minutes,
                    sc=seconds
                )

                logging.debug("Time left - {0}".format(timeStr))

                self._draw(timeStr)

                time.sleep(1.0)

            else:
                logging.debug("Timer at time")

                self._draw('TIME')
                return True

        return True

    def reset(self):
        self._countdown = self._time
