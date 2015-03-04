"""
Sprite classes for game pets
"""

import pygame.draw as draw
from pygame.rect import Rect
import pygame.sprite as sprite
import pygame.surface as surface
from random import randint
from vector import Vector2 as Vector


COLOR_KEY = (255, 105, 180)
GRASS = (161, 199, 107)
GHOST = (102, 114, 153)
BLACK = (0, 0, 0)


class Spirit(sprite.DirtySprite):
    """
    Generic spirit
    """

    def __init__(self, x, y):
        super(Spirit, self).__init__()
        self.image = surface.Surface((30, 45))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.image.set_colorkey(COLOR_KEY)
        self.image.set_alpha(64)
        self.image.fill(COLOR_KEY)
        draw.circle(self.image, GHOST, (15, 15), 15)
        body = Rect((0, 15, 30, 25))
        draw.rect(self.image,
                  GHOST,
                  body)
        for count in xrange(4):
            count += 1
            draw.circle(self.image,
                        GHOST,
                        (count * 6, 40),
                        5)
        self.facing = Vector(1, 0).normalize()
        self._x = x
        self._y = y
        self.speed = 20

    def update(self, delta):
        self._x += self.facing.x * self.speed * delta
        self._y += self.facing.y * self.speed * delta
        self.rect.center = self._x, self._y
        self.facing = self.facing.rotate(randint(-8, 8)).normalize()


class Shade(Spirit):
    pass