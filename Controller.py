#!/usr/bin/python

from PIL import Image as PILImage
#from rgbmatrix import Adafruit_RGBmatrix

from Image import Image
from Clock import Clock
from Timer import Timer
import threading
import time
import signal
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

# Set up threads and matrix output
threads = []
#matrix = Adafruit_RGBmatrix(32, 2)

def kill(signal, frame):
    '''
    Trap the signal and kill any ongoing threads, then exit
    '''
    for thread in threads:
        thread.stop.set()
        exit()

# Set up ctrl+c trap for exiting
logging.info("Creating signal trap")
signal.signal(signal.SIGINT, kill)

# Shared image resources for drawing
image = PILImage.new('RGB', (64, 32))
draw = Image(image)

# Tread creation
logging.info("Starting threads")
clkThread = Clock(draw, (64, 32), position=(0, 0), color=(255, 0, 0, 255))
#threads.append(clkThread)
#clkThread.start()

tmrThread = Timer(draw, (64, 32), minutes=1, position=(0, 0), color=(0, 0, 255, 255))
threads.append(tmrThread)
tmrThread.start()

logging.info("Entering wait loop")
while True:
    #matrix.SetImage(image.im.id, 0, 0)

    # Sleep to get to 60FPS
    time.sleep(0.16)
