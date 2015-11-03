#!/usr/bin/python

from PIL import Image as PILImage
from rgbmatrix import Adafruit_RGBmatrix

from Image import Image
from Clock import Clock
from Timer import Timer
from Controller import Controller

import threading
import time
import signal
import sys
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)s) %(message)s')

# Set up threads and matrix output
threads = []
matrix = Adafruit_RGBmatrix(32, 2)

def kill(signal, frame):
    '''
    Trap the signal and kill any ongoing threads, then exit
    '''
    for thread in threads:
        thread.stop.set()
        sys.exit()

# Set up ctrl+c trap for exiting
logging.info("Creating signal trap")
signal.signal(signal.SIGINT, kill)

# Shared image resources for drawing
timerImage = PILImage.new('RGB', (64, 32))
timers = Image(timerImage)

clockImage = PILImage.new('RGB', (64, 32))
clock = Image(clockImage)

# Tread creation
logging.info("Creating threads")
clkThread = Clock(clock, (64, 32), position=(0, 0), color=(255, 0, 0, 255))
threads.append(clkThread)

tmrThread1 = Timer(timers, (32, 16), minutes=1, position=(0, 0), offset=(0, -6), color=(0, 0, 255, 255))
tmrThread2 = Timer(timers, (32, 16), minutes=1, position=(0, 16), offset=(0, -6), color=(255, 255, 0, 255))
tmrThread3 = Timer(timers, (32, 16), minutes=2, position=(32, 0), offset=(0, -6), color=(255, 0, 0, 255))
tmrThread4 = Timer(timers, (32, 16), minutes=2, position=(32, 16), offset=(0, -6), color=(255, 255, 255, 255))

threads.append(tmrThread1)
threads.append(tmrThread2)
threads.append(tmrThread3)
threads.append(tmrThread4)

logging.info("Starting control thread")
controller = Controller(threads)
controller.start()

logging.info("Entering wait loop")
while True:
    matrix.SetImage(timerImage.im.id, 0, 0)

    # Sleep to get to 60FPS
    time.sleep(0.16)
