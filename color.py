from enum import Enum
from enum import auto

"""
class Color(Enum):
    # Values represent the hue ranges of that colour.
    RED = (0, 20)
    ORANGE = (20, 50)
    YELLOW = (50, 70)
    GREEN = (70, 150)
    CYAN = (150, 200)
    BLUE = (200, 270)
    VIOLET = (270, 330)
    # Colour wheel wraps back around to red.
    RED_HI = (330, 360)
"""
Color = {
    # Values represent the hue ranges of that colour.
    "RED": (0, 20),
    "ORANGE": (20, 50),
    "YELLOW": (50, 70),
    "GREEN": (70, 150),
    "CYAN": (150, 200),
    "BLUE": (200, 270),
    "VIOLET": (270, 330),
    # Colour wheel wraps back around to red.
    "RED_HI": (330, 360)
}


def hue_from_rgb(r, g, b):
    # Formula taken from https://www.rapidtables.com/convert/color/rgb-to-hsv.html
    rp = r/255
    gp = g/255
    bp = b/255

    cmax = max(rp, gp, bp)
    cmin = min(rp, gp, bp)
    delta = cmax - cmin

    # Hue calculation
    hue = 0

    if delta == 0:
        hue = 0
    elif cmax == rp:
        hue = 60 * ((gp-bp)/delta % 6)
    elif cmax == gp:
        hue = 60 * ((bp-rp)/delta + 2)
    elif cmax == bp:
        hue = 60 * ((rp-gp)/delta + 4)

    return hue


def get_closest_color(hue):
    for key, rng in Color.items():
        if hue in range(rng[0], rng[1]):
            if key == "RED_HI":
                return "RED"
            return key
    return None


def quantize_pixel(r, g, b):
    return get_closest_color(hue_from_rgb(r, g, b))
