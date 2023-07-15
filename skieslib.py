from PIL import Image
from numpy import empty, uint8, uint32
from math import pi

PI = pi
TPI = 2 * pi
HPI = pi / 2
QPI = pi / 4
EPI = pi / 8


# Color - color constants and utility functions
class Color:
    # Color integer-list conversion lambdas
    irgb = lambda rgb_int : list(rgb_int.to_bytes(3, byteorder = 'big'))
    rgbi = lambda rgb : uint32((int.from_bytes(rgb)))

    BLACK = irgb(0x000000)
    WHITE = irgb(0xFFFFFF)
    OFFWHITE = irgb(0xEEEEEE)
    NAVY = irgb(0x071952)
    BLUE = irgb(0x6528F7)
    SKYBLUE = irgb(0x068FFF)
    PURPLE = irgb(0xA076F9)
    TURQOISE = irgb(0x35A29F)
    ORANGE = irgb(0xFFB07F)
    YELLOW = irgb(0xFBD85D)
    GREEN = irgb(0xC3EDC0)
    LIME = irgb(0xCCEEBC)
    RED = irgb(0xEF6262)


# Canvas - primitive draw operations
class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = empty((720, 1080, 3), dtype=uint8)
    
    def set(self, x, y, rgb):
        self.array[y, x] = rgb

    def fillbg(self, rgb):
        self.array[:,:] = rgb

    def save(self, path):
        img = Image.fromarray(self.array)
        img.save(path)
