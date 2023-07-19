import skies
from random import randint
from math import floor

def random_region(canvas):
    pad = floor(max(canvas.width, canvas.height) * 0.1)
    low = [randint(pad, canvas.width - 1 - pad), randint(pad, canvas.height - 1 - pad)]
    high = [randint(pad, canvas.width - 1 - pad), randint(pad, canvas.height - 1 - pad)]
    canvas.region(low[0], low[1], high[0], high[1])

def regions(canvas, count):
    for i in range(0, count):
        canvas.color = skies.Color.WHITE if i % 2 == 0 else skies.Color.BLACK
        random_region(canvas)

width = 800
height = 1200

canvas = skies.Canvas(width, height)
regions(canvas, 500)

skies.save_n(canvas, 'test/test.png', 10, regions, [50])
