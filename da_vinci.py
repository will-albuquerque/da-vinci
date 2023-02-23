'''
This script reproduces images with colored, transparent triangles using
a genetic algorithm
'''

import random

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

# Generate a randomly colored triangle
image = Image.new('RGB', (100, 100))
draw = ImageDraw.Draw(image, 'RGBA')
triangle = tuple(
    (random.randrange(image.width), random.randrange(image.height))
    for _ in range(3)
)
color = tuple(random.randrange(256) for _ in range(4))
draw.polygon(triangle, color)

# Save image
try:
    image.save('test.png')
except OSError:
    print('Failed to create image')