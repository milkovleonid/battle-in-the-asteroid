#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame import *
import os

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
health = 5
zrenie = 75
pull = False
MONSTER_COLOR = "#2110FF"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

turel_im = ('%s/py_file/turel.png' % ICON_DIR)


class TUREL(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.health = 5
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.image = turel_im
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)

    def update(self, platforms):
        if self.health < 1:
            self.kill()

    def collide(self, pula, hero):
        if sprite.collide_rect(self, pula):
            self.health -= 1
        if sprite.collide_rect(self, hero):
            pass
            # music

