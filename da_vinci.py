'''
This script reproduces images with colored, transparent triangles using
a genetic algorithm
'''

import argparse
import pathlib
import random
import typing

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

class Point(typing.NamedTuple):
    '''A 2D point'''
    x: int
    y: int

    @staticmethod
    def random(max_x: int, max_y: int) -> typing.Self:
        '''
        Returns a random point in the positive quadrant bounded by
        max_x and max_y
        '''
        assert max_x > 0
        assert max_y > 0
        return Point(random.randrange(max_x), random.randrange(max_y))
    
class Triangle(typing.NamedTuple):
    '''A 2D triangle'''
    a: Point
    b: Point
    c: Point

    @staticmethod
    def random(max_x: int, max_y: int) -> typing.Self:
        '''
        Returns a random triangle in the positive quadrant bounded by
        max_x and max_y
        '''
        assert max_x > 0
        assert max_y > 0
        return Triangle(
            Point.random(max_x, max_y),
            Point.random(max_x, max_y),
            Point.random(max_x, max_y),
        )

class RGBA(typing.NamedTuple):
    '''A color in RGBA format'''
    r: int
    g: int
    b: int
    a: int

    @staticmethod
    def random() -> typing.Self:
        '''Returns a random RGBA color'''
        return RGBA(
            random.randrange(256),
            random.randrange(256),
            random.randrange(256),
            random.randrange(256)
        )

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    'image_path',
    type=pathlib.Path,
    help='the path to the image'
)
args = parser.parse_args()

# Load image
try:
    with Image.open(args.image_path) as image:
        image.load()
except OSError:
    raise SystemExit(f'Cannot open file: {args.image_path.name}')