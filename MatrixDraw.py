#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont

class MatrixDraw:
    fontSmall = ImageFont.truetype('/usr/share/fonts/truetype/antonio/Antonio-Light.ttf', 18)
    fontLarge = ImageFont.truetype('/usr/share/fonts/truetype/antonio/Antonio-Light.ttf', 32)

    @staticmethod
    def text(text):
         
