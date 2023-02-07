import argparse
import pathlib
import PIL.Image as Image

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