#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import time
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 2)

image = None
draw = None

def reset():
    global image
    image = Image.new('RGB', (64, 32))
    global draw
    draw = ImageDraw.Draw(image)
    matrix.Clear()

fnt = ImageFont.truetype('/usr/share/fonts/truetype/antonio/Antonio-Light.ttf', 18)
reset()

t = 1 * 60

while t > -5:
    minutes = t / 60
    seconds = t % 60

    text = "{0:02d}:{1:02d}".format(minutes, seconds)

    reset()

    draw.text((0,-5), text, font=fnt, fill=(255,255,255,128))
    draw.text((32, -5), text, font=fnt, fill=(255, 0, 0, 128))
    draw.text((0, 11), text, font=fnt, fill=(255, 255, 0, 128))
    draw.text((32, 11), text, font=fnt, fill=(0, 0, 255, 128))

    matrix.SetImage(image.im.id, 0, 0)
    time.sleep(1.0)

    t = t - 1

matrix.Clear()

