import pygame
import textwrap


def draw_text(text: str, line_width: int, font: pygame.font.Font,
              dest: pygame.Surface | None, position: tuple[int, int]) -> pygame.Surface:
    """Render multi-line text onto a PyGame surface"""
    lines = textwrap.wrap(text, line_width)
    text_colour = (0, 0, 0)
    surfaces = [font.render(line, False, text_colour) for line in lines]

    # Calculate combined size of surfaces
    text_width = 0
    text_height = 0
    for surf in surfaces:
        width, height = surf.get_size()
        text_width = max(text_width, width)
        text_height += height

    # Create surface if requested
    if dest is None:
        dest = pygame.Surface((text_width, text_height), pygame.SRCALPHA)
        dest.fill((255, 255, 255, 0))
        position = (text_width / 2, text_height / 2)

    # Blit text surfaces
    line = 0
    pos_x = position[0] - text_width / 2
    pos_y = position[1] - text_height / 2
    for surf in surfaces:
        width, height = surf.get_size()
        offset = (text_width - width) / 2
        dest.blit(surf, (pos_x + offset, pos_y + line))
        line += height

    return dest
