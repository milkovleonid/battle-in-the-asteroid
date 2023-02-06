import pygame
from pygame import *
import os

ICON_DIR = os.path.dirname(__file__)
MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 64
GRAVITY = 0.25  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
veapon = 1
magazins = 3
coords = [66, 512]


class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.coords = coords
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = self.coords[0]  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = self.coords[1]
        self.left_shg = [image.load('%s/py_files/lshag_1.png' % ICON_DIR),
                         image.load('%s/py_files/left.png' % ICON_DIR),
                         image.load('%s/py_files/lshag_3.png' % ICON_DIR),
                         image.load('%s/py_files/lshag_4.png' % ICON_DIR),
                         image.load('%s/py_files/lshag_5.png' % ICON_DIR)]

        self.prav_shg = [image.load('%s/py_files/shag_1.png' % ICON_DIR),
                         image.load('%s/py_files/right.png' % ICON_DIR),
                         image.load('%s/py_files/shag_3.png' % ICON_DIR),
                         image.load('%s/py_files/shag_4.png' % ICON_DIR),
                         image.load('%s/py_files/shag_5.png' % ICON_DIR)]
        self.health = 4
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = True  # На земле ли я?
        self.image = Surface((WIDTH, HEIGHT))
        self.image = image.load('%s/py_files/right.png' % ICON_DIR)
        self.image = transform.scale(self.image, (32, 64))
        self.rect = Rect(self.coords[0], self.coords[1], WIDTH, HEIGHT)  # прямоугольный объект
        self.q = 0
        self.rq = 0

        #        Анимация движения вправо

    def update(self, left, right, up, platforms, sp_orug, r, f, puli_tur, zomba, veapon, oboyma_0, oboyma_1, oboyma_2,
               bullets_0, bullets_1, bullets_2, ideal_oboyma_0, ideal_oboyma_1, ideal_oboyma_2, korobk, sostoyanie):
        if self.health == 0:
            sostoyanie = 0
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -10

        if left:
            self.xvel = -5  # Лево = x- n
            self.start_ticks = pygame.time.get_ticks()
            seconds = (pygame.time.get_ticks() - self.start_ticks) / 100  # вычисляем сколько прошло секунд
            if seconds % 2 == 0:
                if self.q == 5:
                    self.q = 0
                self.image = self.left_shg[self.q]
                self.image = transform.scale(self.image, (32, 64))
                self.q += 1



        if right:
            self.xvel = 5  # Лево = x- n
            self.start_ticks1 = pygame.time.get_ticks()
            seconds = (pygame.time.get_ticks() - self.start_ticks1) / 100  # вычисляем сколько прошло секунд
            if seconds % 2  == 0:
                if self.rq == 5:
                    self.rq = 0
                self.image = self.prav_shg[self.rq]
                self.image = transform.scale(self.image, (32, 64))
                self.rq += 1


        if r:
            if veapon == 0:
                bullets_0 -= (ideal_oboyma_0 - oboyma_0)
                oboyma_0 += (ideal_oboyma_0 - oboyma_0)
            if veapon == 1:
                bullets_1 -= (ideal_oboyma_1 - oboyma_1)
                oboyma_1 += (ideal_oboyma_1 - oboyma_1)
            if veapon == 2:
                bullets_2 -= (ideal_oboyma_2 - oboyma_2)
                oboyma_2 += (ideal_oboyma_2 - oboyma_2)
        if f:
            if '1' in sp_orug:
                if '2' in sp_orug:
                    if veapon == 2:
                        veapon = 0
                    else:
                        veapon += 1
                else:
                    if veapon == 0:
                        veapon = 1
                    else:
                        veapon = 0
        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += GRAVITY
        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, puli_tur, zomba, korobk)
        self.rect.x += (self.xvel)  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, puli_tur, zomba, korobk)

    def collide(self, xvel, yvel, platforms, zomba, puli_tur, korobk):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0

        for o in korobk:
            if sprite.collide_rect(self, o):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = o.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = o.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = o.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = o.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
        for i in zomba:
            if sprite.collide_rect(self, i):
                self.start_ticksz = pygame.time.get_ticks()
                seconds = (pygame.time.get_ticks() - self.start_ticks1) / 1000  # вычисляем сколько прошло секунд
                if seconds % 1 == 0:
                    self.health -= 2
        for pula_t in puli_tur:
            if sprite.collide_rect(self, pula_t):
                self.health -= 1.5
