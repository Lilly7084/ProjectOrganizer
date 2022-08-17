import pygame
import re


Colour = tuple[int, int, int]


def from_hex(code: int) -> Colour:
    red = int((code >> 16) & 0xFF)
    grn = int((code >> 8) & 0xFF)
    blu = int(code & 0xFF)
    return red, grn, blu


def from_rgb(red: int, grn: int, blu: int) -> Colour:
    # Haha data-spitter-outer go brrrr
    return red, grn, blu


PARSERS = [
    (r'#([0-9a-f]{6})', from_hex),
    (r'rgb\((.*?)\)', from_rgb)
]


def parse_colour(colour: str) -> Colour:
    """Attempt to convert a colour from a string to a `Colour` object.
    Checks built-in color list (`pygame.colordict.THECOLORS`),
    before trying all available converters/parsers.
    If all fails, returns a default color (black)."""
    colour = colour.strip().lower()  # Make input a bit more resilient
    # Try the built-in color table
    if colour in pygame.colordict.THECOLORS:
        return pygame.colordict.THECOLORS[colour]

    # Try the converters/parsers
    for (check, parse) in PARSERS:
        match = re.match(check, colour)
        if match:
            vals = match.group(1).split(',')  # Split apart components
            vals = map(lambda x: float(x.strip()), vals)  # Strip and parse
            return parse(*vals)

    # Failure condition: Still needs to return a color
    return 0, 0, 0
