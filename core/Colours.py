import pygame


# TODO: Fix type-checking for colours
Colour = tuple[float, float, float]


def from_rgb(colour: str) -> tuple:
    as_str = colour[4:-1].split(",")
    return tuple(int(i) for i in as_str)


def from_hsv(colour: str) -> tuple:
    as_str = colour[4:-1].split(",")
    temp = pygame.Color((0, 0, 0))
    temp.hsva = [int(i) for i in as_str]
    return temp[0:3]


def from_hex(colour: str) -> tuple:
    if len(colour) == 7:
        colour = colour[1:]
    return int(colour[0:2], 16), int(colour[2:4], 16), int(colour[4:6], 16)


def parse_colour(colour: str) -> tuple:
    if colour in pygame.colordict.THECOLORS:
        return pygame.colordict.THECOLORS[colour]
    elif colour.lower().startswith("rgb("):
        return from_rgb(colour)
    elif colour.lower().startswith("hsv("):
        return from_hsv(colour)
    elif len(colour) in (6, 7):
        return from_hex(colour)
