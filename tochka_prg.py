from pygame import *
PLATFORM_WIDTH, PLATFORM_HEIGHT = 64, 64

class Plat_(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x + PLATFORM_WIDTH, y - PLATFORM_HEIGHT + 5
        self.image = Surface((1, 1))
        self.image.fill((0, 0, 0))
        self.rect.x, self.rect.y = x, y - PLATFORM_HEIGHT + 5
