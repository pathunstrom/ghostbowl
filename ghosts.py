"""
Sprite classes for game pets
"""

from math import cos, pi, sin
import pygame.draw as draw
from pygame.rect import Rect
import pygame.sprite as sprite
import pygame.surface as surface
from random import randint, uniform
from vector import Vector2 as Vector


COLOR_KEY = (255, 105, 180)
GRASS = (161, 199, 107)
GHOST = (102, 114, 153)
SHADE = (64, 64, 64)
BLACK = (0, 0, 0)

tau = 2 * pi


class Ba(sprite.DirtySprite):
    """
    Generic spirit
    """

    def __init__(self, x, y, color):
        super(Ba, self).__init__()
        self.image = surface.Surface((30, 45))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.image.set_colorkey(COLOR_KEY)
        self.image.set_alpha(64)
        self.image.fill(COLOR_KEY)
        draw.circle(self.image, color, (15, 15), 15)
        body = Rect((0, 15, 30, 25))
        draw.rect(self.image,
                  color,
                  body)
        for count in xrange(4):
            count += 1
            draw.circle(self.image,
                        color,
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


class Spirit(Ba):

    def __init__(self, x, y):
        super(Spirit, self).__init__(x, y, GHOST)

    def update(self, delta):
        super(Spirit, self).update(delta)
        self.facing = self.facing.rotate(randint(-8, 8)).normalize()


class Shade(Ba):

    def __init__(self, x, y):
        super(Shade, self).__init__(x, y, SHADE)
        self.radius = 10
        self.range = 10
        self.t = 4.71238898038469
        self.target_t = self.t

    def update(self, delta):
        super(Shade, self).update(delta)
        self.facing = Vector(*self._get_target(delta)).normalize

    def _get_target(self, delta):
        center = Vector(self._x, self._y) + (self.facing * self.range)
        print(center)
        x = center.x + self.radius * cos(self.t)
        y = center.y + self.radius * sin(self.t)
        self.t += uniform(-1, 1) * delta
        if self.t > tau:
            self.t -= tau
        elif self.t < 0:
            self.t += tau
        return x, y