#!/usr/bin/python3

from PIL import Image
from numpy import empty, uint8, uint32
from math import pi
import os

PI = pi
TPI = 2 * pi
HPI = pi / 2
QPI = pi / 4
EPI = pi / 8

class Color:
    # Color integer/rgb-list conversion lambdas
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


class Canvas:
    def __init__(self, width, height, bg_color = Color.BLACK):
        self.width = width
        self.height = height
        self.raster = empty((height, width, 3), dtype=uint8)

        self.bg_color = bg_color
        self.color = Color.WHITE
        self.stroke_width = 1
        self.opacity = 1
        self.fill = False

        self.raster[:,:] = self.bg_color

    # Draw modes
    def point(self, x, y):
        self.raster[y, x] = self.color

    def region(self, x0, y0, x1, y1):
        self.raster[y0:y1, x0:x1] = self.color

    def line(self, x0, y0, x1, y1):
        def low(x0, y0, x1, y1):
            dx = x1 - x0
            dy = y1 - y0
            yi = 1
            if dy < 0:
                yi = -1
                dy = -dy
            D = 2 * dy - dx
            y = y0
            for x in range(x0, x1):
                self.raster[y, x] = self.color
                if D > 0:
                    y = y + yi
                    D = D + (2 * (dy - dx))
                else:
                    D = D + 2 * dy
            pass

        def high(x0, y0, x1, y1):
            dx = x1 - x0
            dy = y1 - y0
            xi = 1
            if dx < 0:
                xi = -1
                dx = -dx
            D = 2 * dx - dy
            x = x0
            for y in range(y0, y1):
                self.raster[y, x] = self.color
                if D > 0:
                    x = x + xi
                    D = D + (2 * (dx - dy))
                else:
                    D = D + 2 * dx
            pass

        if (abs(y1 - y0) < abs(x1 - x0)):
            if x0 > x1:
                low(x1, y1, x0, y0)
            else:
                low(x0, y0, x1, y1)
        else:
            if y0 > y1:
                high(x1, y1, x0, y0)
            else:
                high(x0, y0, x1, y1) 

    # Convenience
    def clear(self):
        self.region(0, self.width - 1, 0, self.height - 1)

    def rect(self, x, y, w, h):
        self.region(x, y, x + w, y + h)

    def polyline(self, pts):
        for pt0, pt1 in zip(pts, pts[1:]):
            self.line(pt0[0], pt0[1], pt1[0], pt1[1])

    def polygon(self, pts):
        self.polyline(pts + [pts[0]])

def save(canvas, path):
    img = Image.fromarray(canvas.raster)
    img.save(path)

def save_n(canvas, path, n, draw_fun, args):
    base_path, extension = os.path.splitext(path)
    for i in range(0, n):
        canvas.clear()
        draw_fun(canvas, *args)
        save_path = base_path + str(i).zfill(4) + extension
        save(canvas, save_path)
