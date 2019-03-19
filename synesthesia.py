from PIL import Image
from color import Color
from color import *

path = "image.jpg"

im = Image.open(path)

# Convert the image to RGB colour mode, in case it isn't already.
rgb_im = im.convert("RGB")

# Get the image's dimensions.
width, height = im.size

# Initialize a 2-dimensional list, one for each channel.
colors = [[0 for x in range(width)] for y in range(height)]

for i in range(width):
    for j in range(height):
        # Extract the image's RGB channels.
        r, g, b = rgb_im.getpixel((i, j))
        # Assign
        colors[i][j] = quantize_pixel(r, g, b)

