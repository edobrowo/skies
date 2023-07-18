import skies
from random import randint
from math import floor
from sys import argv

def random_polygon(canvas, xlow, ylow, xhigh, yhigh, count):
    pts = [[randint(xlow, xhigh), randint(ylow, yhigh)] for _ in range(count)]
    canvas.polygon(pts)

def polygons(canvas, n, m, lc):
    dx = floor(canvas.width / n)
    dy = floor(canvas.height / m)
    pad = floor(0.1 * max(dx, dy))
    for i in range(0, width, dx):
        for j in range(0, height, dy):
            random_polygon(canvas, i + pad, j + pad, i + dx - pad, j + dy - pad, lc)

width = 800
height = 1200

canvas = skies.Canvas(width, height)
polygons(canvas, 4, 3, 50)

skies.save_n(canvas, 'polygons/poly.png', 10, polygons, [4, 3, 10])
