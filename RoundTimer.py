#!/usr/bin/python

from PIL import Image as PILImage
from rgbmatrix import Adafruit_RGBmatrix

from Image import Image
from Clock import Clock
from Timer import Timer
from Controller import Controller
from Button import Button

import threading
import time
import signal
import sys
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)s) %(message)s')

# Set up threads and matrix output
matrix = Adafruit_RGBmatrix(32, 2)

def kill(signal, frame):
    '''
    Trap the signal and kill any ongoing threads, then exit
    '''
    for thread in threads:
        try:
            thread.pause.set()
        except:
            pass
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

tmrThreads = []
tmrThreads.append(Timer(timers, (32, 16), minutes=50, position=(0, 0), offset=(0, -6), color=(0, 0, 255, 255)))
tmrThreads.append(Timer(timers, (32, 16), minutes=50, position=(0, 16), offset=(0, -6), color=(255, 255, 0, 255)))
tmrThreads.append(Timer(timers, (32, 16), minutes=50, position=(32, 0), offset=(0, -6), color=(255, 0, 0, 255)))
tmrThreads.append(Timer(timers, (32, 16), minutes=50, position=(32, 16), offset=(0, -6), color=(255, 255, 255, 255)))

btnThreads = []
btnChannels = [18, 19, 24, 25]
for index, channel in enumerate(btnChannels):
	btnThreads.append(Button(channel, tmrThreads[index]))

logging.info("Starting timer, clock, and button threads")
threads = [clkThread]+tmrThreads+btnThreads
for thread in threads:
    thread.start()

logging.info("Entering wait loop")
while True:
    matrix.SetImage(timerImage.im.id, 0, 0)

    # Sleep to get to 60FPS
    time.sleep(0.16)
