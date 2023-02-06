#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
from pygame import *

import sama_igra
from mob import *
from korob import *
from drop import *
from sama_igra import *
from strelba import *
from tochka_prg import *
from pula_t import *
from platform import *
from turel import *
import os
from zagruzka import *
import math

# Объявляем переменные
sostoyanie = 0
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
ICON_DIR = os.path.dirname(__file__)
veapon = 0
sp_orug = [0]
oboyma_0 = 22
all_bullets = []
oboyma_1 = 30
oboyma_2 = 6
bullets_0 = 31
bullets_1 = 30
bullets_2 = 12
ideal_oboyma_0 = 22
ideal_oboyma_1 = 30
ideal_oboyma_2 = 6
coords = sama_igra.coords
zrenie = 75
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_1 = ('%s/py_files/lvl1.png' % ICON_DIR)

BACKGROUND_2 = ('%s/py_files/lvl2.png' % ICON_DIR)


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    def reverse(self, pos):
        return (pos[0] - self.state.left, pos[1] -self.state.top)
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)

def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg = image.load(BACKGROUND_1)  # Заливаем поверхность сплошным цветом
    bg = transform.scale(bg, (800, 640))
    '''
    if sostoyanie == 0:
        entities = pygame.sprite.Group()
        bg.fill((51, 153, 51))
        bg = transform.scale(bg, (700, 700))
        click = False
        pygame.draw.polygon(screen, (255, 255, 255), [[150, 10], [648, 631], [411, 600]], 4)
        q = pygame.image.load('C:/Users/root/Downloads/pixil-frame-0 (13).png')
        q = pygame.transform.scale(q, (500, 500))
        screen.blit(q, (0, 400))
        knopk1 = knop1(click, mouse.get_pos())
        knopk2 = knop2(click, mouse.get_pos())
        entities.add(knopk2, knopk1)
        timer = pygame.time.Clock()
        while 1:  # Основной цикл программы
            timer.tick(60)
            for e in pygame.event.get():  # Обрабатываем события
                if e.type == QUIT:
                    exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    click = True
        screen.blit(bg, (0, 0))'''



    hero = Player()  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию - стоим
    r = f = False
    up = False
    entities = pygame.sprite.Group()  # Все объекты
    pulli = pygame.sprite.Group()
    platforms = []  # то, во что мы будем врезаться или опираться
    zomba = []
    TURELI = []
    korobk = []
    tochki = []
    dropi = []
    sp_puli = []
    puli_tur = []

    entities.add(hero)

    level = [
        "--------------------------------------------------------------------",
        "-                                                                  -",
        "-                                                                  -",
        "-       -     --  --                                               -",
        "-                                                                  -",
        "-                     -         #                       ---        -",
        "-                            ----                                  -",
        "-       ----    --       --                        -               -",
        "-             z   z                     # #     z z    z           -",
        "--------------------------------------------------------------------"]

    level1 = [
        "--------------------------------------------------------------------",
        "-                                                                  -",
        "-                                                                  -",
        "-       -     --  --                                               -",
        "-                     z            #                               -",
        "-                     -            -                    ---        -",
        "-                                                                  -",
        "-       ----    --       --                  #      ---------      -",
        "-      #    z zz           z     ##       z   z zz              #  -",
        "--------------------------------------------------------------------"]

    timer = pygame.time.Clock()
    cor_z = []
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
                if y < 96:
                    tch = Plat_(x, y)
                    entities.add(tch)
                    tochki.append(tch)
            if col == "z":
                ms = Monster(x, y, (hero.rect.x, hero.rect.y))
                entities.add(ms)
                cor_z.append((x, y))
                zomba.append(ms)
            if col == "&":
                turel_comp = TUREL(x, y)
                entities.add(turel_comp)
                TURELI.append(turel_comp)
                if zrenie + x > coords[0] or coords[0] > x - zrenie:
                    pulat_t = TUREL_p(x, y, (hero.rect.x, hero.rect.y))
                    entities.add(pulat_t)
                    puli_tur.append(pulat_t)
                TURELI.append(turel_comp)
            if col == "#":
                korobc = korob(x, y)
                entities.add(korobc)
                korobk.append(korobc)
                if random.randint(1, 40) in [7, 9, 17, 31, 25, 3, 18]:
                    droping = drop(x, y)
                    entities.add(droping)
                    dropi.append(droping)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while 1:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                exit()
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == pygame.MOUSEBUTTONDOWN:
                click = True
                pula = buttonin(camera.reverse(mouse.get_pos()), hero)
                sp_puli.append(pula)
                pulli.add(pula)
            if e.type == KEYDOWN and e.key == K_r:
                r = True
            if e.type == KEYDOWN and e.key == K_f:
                f = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_r:
                r = False
            if e.type == KEYUP and e.key == K_f:
                f = False

        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, sp_orug, r, f, puli_tur, zomba, veapon, oboyma_0, oboyma_1, oboyma_2,
                    bullets_0, bullets_1, bullets_2, ideal_oboyma_0, ideal_oboyma_1, ideal_oboyma_2, korobk, sostoyanie
                    )  # передвижение
        for z in zomba:
            for c in cor_z:
                z.update(platforms, sp_puli, tochki, hero, korobk, zomba)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        for bullet in pulli:
            bullet.update(screen, coords)
            for i in zomba:
                if Rect.colliderect(bullet.rect, i):
                    pulli.remove(bullet)
            for j in korobk:
                if Rect.colliderect(bullet.rect, j):
                    pulli.remove(bullet)
            for p in platforms:
                if Rect.colliderect(bullet.rect, p):
                    pulli.remove(bullet)

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
