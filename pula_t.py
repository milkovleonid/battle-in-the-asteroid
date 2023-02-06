#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from pygame import *
import os

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
health = 5
zrenie = 75
pull = False
MONSTER_COLOR = "#2110FF"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

class TUREL_p(sprite.Sprite):
    def __init__(self, x, y, coords):
        super().__init__(x, y, coords)
        self.pos = x, y
        self.dir = (coords[0] - self.pos[0], coords[1] - self.pos[1])
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = Surface((7, 2)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = transform.rotate(self.bullet, angle)
        self.speed = 2

    def updat(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed, self.pos[1] + self.dir[1] * self.speed)

    def draw(self):
        self.bullet_rect = self.bullet.get_rect(center=self.pos)