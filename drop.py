from pygame import *
import random
import os
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 22


ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
dropi = [('%s/py_files/vintovka.png' % ICON_DIR),
         ('%s/py_files/rygye.png' % ICON_DIR)]


class drop(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.a = random.randint(1, 10)
        if self.a in [1, 6]:
            self.image = image.load(dropi[0])
        else:
            self.image = image.load(dropi[1])
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


    def update(self, hero, veapon, sp_orug):
        if sprite.collide_rect(self, hero):

            if self.a in [1, 6]:
                sp_orug.append('1')

            else:
                sp_orug.append('1')
            self.kill()
