#!/usr/bin/python

import threading
import logging

class DrawThread(threading.Thread):
    def __init__(self, image, size, position=(0,0), color=(255,255,255,255)):
        super(DrawThread, self).__init__()
        self._image = image
        self._size = size
        self._position = position
        self._color = color

        # Event triggers are backwards - we set the signal so we can wait for it
        # to trigger during 'pause' operations
        self.event = threading.Event()
        self.event.set()

        self.stop = threading.Event()

    def _draw(self, text, font=None):
        '''
        Draw the current time to the output buffer
        '''
        if(font == None):
            font = self._image.fontSm

        # Aquire a lock on the image
        self._image.lock()

        # Overdraw the region with a blank
        self._image.rectangle([(0,0), self._size], fill=(0,0,0,0))
        self._image.text(self._position, text, fill=self._color, font=self._image.fontSm)

        # Release the image so other threads can edit it
        self._image.unlock()
