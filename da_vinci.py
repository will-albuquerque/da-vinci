'''
This script reproduces images with colored, transparent triangles using
a genetic algorithm
'''

import random

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

# Define image width and height
WIDTH, HEIGHT = 100, 100

# Generate random genotype
GENES = 10
genotype = {}
for _ in range(GENES):
    triangle = tuple(
        (random.randrange(WIDTH), random.randrange(HEIGHT))
        for _ in range(3)
    )
    color = tuple(random.randrange(256) for _ in range(4))
    genotype[triangle] = color

# Create phenotype
image = Image.new('RGB', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image, 'RGBA')
for triangle, color in genotype.items():
    draw.polygon(triangle, color)

# Save image
try:
    image.save('test.png')
except OSError:
    print('Failed to create image')