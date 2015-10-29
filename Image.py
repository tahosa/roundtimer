#!/usr/bin/python

from PIL import ImageDraw, ImageFont
import threading

class Image:
    def __init__(self, image):
        '''
        Create the imagedraw parent object and the lock mechanism
        '''
        self._image = ImageDraw.Draw(image)
        self._lock = threading.Lock()
        self.fontLg = ImageFont.truetype('Antonio-Light.ttf', 36)
        self.fontSm = ImageFont.truetype('Antonio-Light.ttf', 18)

        self.rectangle = self._image.rectangle
        self.text = self._image.text

    def lock(self):
        '''
        Lock this image to prevent it from being altered by more than one thread
        at a time
        '''
        return self._lock.acquire(True)

    def unlock(self):
        '''
        Release the lock on this image so another thread can modify it
        '''
        return self._lock.release()
