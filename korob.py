import pygame.time
from pygame import *
import os


puhka = 0
PLATFORM_WIDTH = 64
PLATFORM_HEIGHT = 64
GRAVITY = 0.25
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class korob(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.puhka = 0
        puhka = self.puhka
        self.health = 2
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load('%s/py_files/korob.png' % ICON_DIR)
        self.image = transform.scale(self.image, (64, 64))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


    def update(self):
        if self.health < 1:
            self.kill()

    def collide(self, zomba, pulli, korobk):
        for i in zomba:
            if sprite.collide_rect(self, i):
                self.star = pygame.time.get_ticks()
                self.health -= 1
                if (pygame.time.get_ticks() - self.star)/1000 > 3:
                    self.health -= 1
        for p in pulli:
            if Rect.colliderect(self, p):
                self.health -= 1

