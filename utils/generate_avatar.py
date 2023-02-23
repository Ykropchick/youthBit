from random import random, choice

from PIL import Image, ImageDraw


def create_avatar(width=512, resolution=16, fill_prob=0.5):
    size = width // resolution
    im = Image.new('RGB', (width, width), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    color = choice(["red", "green", "blue", "orange", "lightblue"])

    for x in range(8):
        for y in range(16):
            if random() > fill_prob:
                left = (size * x, size * y)
                op_left = (width - size * x - size, left[1])
                draw.rectangle((left, (left[0] + size, left[1] + size)), fill=color)
                draw.rectangle((op_left, (op_left[0] + size, op_left[1] + size)), fill=color)

    return im
