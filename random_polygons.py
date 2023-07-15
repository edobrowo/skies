from skieslib import Canvas, Color
from random import randint

def random_polygon(canvas, xlow, ylow, xhigh, yhigh, count):
    pts = [[randint(xlow, xhigh), randint(ylow, yhigh)] for _ in range(count)]
    canvas.polygon(pts)

width = 800
height = 1200

canvas = Canvas(width, height)
canvas.fillbg(Color.BLACK)

for i in range(0, width, 200):
    for j in range(0, height, 200):
        random_polygon(canvas, i + 20, j + 20, i + 200 - 20, j + 200 - 20, 10)

canvas.save('test.png')
