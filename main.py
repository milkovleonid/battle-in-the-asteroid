import pygame
import pygame.mixer, pygame.time
import random
from pygame import *
import os.path, sys

WIDTH = 1200
HEIGHT = 700

level = 1
lives = 100
score = 0

step = 5
flag = 1
temp = 100
background = image.load('data/fon1.jpg')
screen.blit(background, (0,0))
key.set_repeat(1,1)
enemies = []
bullets = []
bombs = []
def sound_zagruzki():
	# звук выстрела
    file = os.path.join('data', 'vistrel.wav')
    sound = mixer.Sound(file)
    channel = sound.play()


class Sprite_player:
    # Этот класс я стащил у Майкла Сондерса из его Pilvanders
    def __init__(self, xpos, ypos, filename):
        # инициализация j,]trnf
        self.x = xpos
        self.y = ypos
        pik = pygame.image.load(filename)
        pik = pik.convert()
        self.bitmap = pik
        self.bitmap.set_colorkey((0, 0, 0))

    def set(self, xpos, ypos):
        # установить спрайт по координатам
        self.x = xpos
        self.y = ypos

    def render(self):
        # отрисовать спрайт
        screen.blit(self.bitmap, (self.x, self.y))


pstr1 = Sprite_player(zx, zy, 'data/pstr01.png')
pstr2 = Sprite_player(zx, zy, 'data/pstr02.png')
pstr3 = Sprite_player(zx, zy, 'data/pstr03.png')
pstl1 = Sprite_player(zx, zy, 'data/pstl01.png')
pstl2 = Sprite_player(zx, zy, 'data/pstl02.png')
pstl3 = Sprite_player(zx, zy, 'data/pstl03.png')


# это спрайты пистолета

# --------------------------------------------------------------

class Pistol(Sprite_player):
    def __init__(self, xpos, ypos, naprav):
        global pst1, pst2, pst3
        self.x = xpos
        self.y = ypos
        if naprav == 'right':
            # Дуло смотрит вправо
            pst1 = pstr1
            pst2 = pstr2
            pst3 = pstr3
            pst1 = Sprite_player.__init__(self, xpos, ypos, 'data/pstr01.png')
        else:
            # Дуло смотрит влево
            pst1 = pstl1
            pst2 = pstl2
            pst3 = pstl3
            pst1 = Sprite_player.__init__(self, xpos, ypos, 'data/pstl01.png')
        # в зависимости от 'naprav

    def put(self, xpos, ypos):
        # установить по координатам
        self.x = xpos
        self.y = ypos
        self.render()


# ----------------------------------------------------------------
class Vrag(Sprite_player):
    def __init__(self, xpos, ypos, naprav):
        global vrg
        self.x = xpos
        self.y = ypos
        if naprav == 'left':
            vrg = Sprite_player.__init__(self, xpos, ypos, 'data/botr1.bmp')
        else:

            vrg = Sprite_player.__init__(self, xpos, ypos, 'data/botl1.bmp')

    def put(self, xpos, ypos):
        # отрисовываем ботинок
        global flag
        if 0 < xpos < pr + 1:
            # проверка на границы окна,если ботинок в пределах границ он отрисовывается.
            self.x = xpos
            self.y = ypos
            self.render()
            # Проверка достижения середины
            if (flag > 0) and (182 < xpos < 500):
                flag = 0


# -------------------------------------------------------------------
def bah(xpos, ypos):
    # процедура выстрела
    global vlx, vly, score
    pst2.set(xpos, ypos)
    pst2.render()
    for i in range(6):
        vlx[i] = vlx[i] + 1
        vrx[i] = vrx[i] - 1
        vrgl[i].put(vlx[i], vly[i])
        vrgr[i].put(vrx[i], vry[i])
        if 0 < vlx[i]:
            if (dulo == 'left') and ((vly[i] - 20) < ypos < (vly[i] + 60)):
                score = score + 1
                vlx[i] = - random.randrange(50, 300, 25)
        if vrx[i] < pr:
            if (dulo == 'right') and ((vry[i] - 20) < ypos < (vry[i] + 60)):
                score = score + 1
                vrx[i] = pr + random.randrange(50, 300, 25)
    # проверка поподания в ботинок в цикле если дуло влево проверяются правые/ вправо левые
    # при выстреле все ботинки все равно смещаются на пиксел к центру
    # это защита от постоянно нажатого пробела
    # вместо убитого ботинка за пределами экрана генерируется новый по случайному X.
    display.update()
    pst3.set(xpos, ypos)
    pst3.render()
    boom()
    # звук выстрела
    display.update()


# -------------------------------------------------------------------
while 1:
    # основной цикл программы
    score = 0
    # счет
    level = 1
    # уровень
    xpos = zx
    ypos = zy
    flag = 1
    # эта переменная предназначена для выхода из циклов при flag=0
    speed = 1
    temp = 100
    # задержка в микросекундах
    dulo = 'left'

    zx = 312
    zy = 300
    # Координаты пистолета
    # -----------------------------------------------
    vlx = [0, -200, 0, -400, -150, 0]
    vly = vry = [100, 200, 300, 400, 500, 600]
    pr = xscr - 118
    vrx = [pr + 100, pr, pr + 300, pr, pr + 200, pr]
    # начальные координаты 6-ти ботинок
    vrgl = []
    vrgr = []
    # создаем 2  списка для ботинков справа и слева
    flag = 1
    for i in range(6):
        # заполняем списки в цикле
        vrgl.append(Vrag(vlx[i], vly[i], 'left'))
        vrgr.append(Vrag(vrx[i], vry[i], 'right'))

    pest = Pistol(zx, zy, dulo)
    # определяем пистолет(дуло вправо/влево)
    pygame.screen.blit(background, (0, 0))
    pest.put(zx, zy)
    display.flip()
    # заливаем экран обоями, ставим пистолет по координатам и отрисовываем все это на дисплее
    # -----------------------------------------------------------------
    while 1:
        # основной цикл игры
        for i in range(6):
            # смещение всех ботинок на пиксел к центру и их отрисовка
            vlx[i] = vlx[i] + 1
            vrx[i] = vrx[i] - 1
            vrgl[i].put(vlx[i], vly[i])
            vrgr[i].put(vrx[i], vry[i])
        pest.put(zx, zy)
        # устанавливаем пистолет
        display.flip()
        screen.blit(background, (0, 0))
        Font = font.Font(None, 32)
        rez = score // 100
        # rez  = счет нацело поделить на сто
        level = 1 + rez
        # уровень до 100 очков 1-ый, дальше за каждые 100 добавляется 1
        if temp > 19:
            temp = 100 - rez * 20
        # определяем задержку,здесь по if защита от ухода в минус
        # печатаем счет(кол-во убитых ботинок)
        pygame.time.wait(temp)
        # задержка,чем выше уровень тем она меньше
        if flag == 0:
            break
        # выход из основного игрового цикла
        for event in pygame.event.get():
            # опрос клавиатуры, мыши
            if event.type == QUIT:
                sys.exit()
            # выход по нажатию креста на рамке окна
            if event.type == KEYDOWN:
                # если нажата клавиша то

                if event.key == K_ESCAPE:
                    flag = 0
                # по esc выход из игрового цикла через установку flag в  0
                if event.key == K_DOWN:
                    zy = zy + step
                    if zy >= (yscr - 100):
                        zy = zy - step
                # перемещение пистолета вниз если не достигнута нижняя граница
                if event.key == K_UP:
                    zy = zy - step
                    if zy <= 0:
                        zy = zy + step
                    # перемещение пистолета вверх если не достигнута верхняя граница
                if event.key == K_LEFT:
                    dulo = 'left'
                    pest.__init__(zx, zy, 'left')
                    # дуло влево
                if event.key == K_RIGHT:
                    dulo = 'right'
                    pest.__init__(zx, zy, dulo)
                # дуло вправо
                if event.key == K_SPACE:
                    bah(zx, zy)
                # выстрел
    # -------------------конец основного цикла-------------------------
    flag = 1
    '''
    # большой бум символизирующий конец игры !
    Font = font.Font(None, 72)
    # определяем фонт
    textimg = Font.render('                               ', 1, (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 250))
    textimg = Font.render('  GAME  OVER  !!! ', 1, (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 300))
    textimg = Font.render('                               ', 1, (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 350))
    Font = font.Font(None, 36)
    textimg = Font.render('-----------------------------------------------------', 1, (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 575))

    textimg = Font.render('    Space - New Game     Esc - Exit    ', 1, (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 600))
    textimg = Font.render('-----------------------------------------------------', 1, (0, 255, 255), (255, 0, 0))
    screen.blit(textimg, (180, 625))
    display.flip()
    '''
    # пишем на экране Game Over и прочую инфу
    while 1:
        # этот цикл на окончание программы
        for event in pygame.event.get():

            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    flag = 0
                # по Space выход из внутреннего цикла через break
                if event.key == K_ESCAPE:
                    sys.exit()
                # по Esc выходим из программы
        if flag == 0:
            break


'''
class mob(pygame.sprite.Sprite):
    pass
class korob(pygame.sprite.Sprite):
    pass
class platforma(pygame.sprite.Sprite):
    pass
class patron(pygame.sprite.Sprite):
    pass
class special_mob(pygame.sprite.Sprite):
    pass
class plus_mob(pygame.sprite.Sprite):
    pass
class pol(pygame.sprite.Sprite):
    pass
class potolok(pygame.sprite.Sprite):
    pass
class veapon(pygame.sprite.Sprite):
    pass
class bochka(pygame.sprite.Sprite):
    pass
'''

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("My Game")
pygame.image.load('')
pygame.draw.rect()
clock = pygame.time.Clock()
"""
def draw():
    screen.clear()
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()
# Цикл игры"""
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(30)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    #all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
'''
WIDTH = 480
HEIGHT = 600
FPS = 30

# Задаем цвета


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("player")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        fullname = os.path.join('data', 'creature.png')
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        self.image = pygame.image.load(fullname)
        self.rect = self.image.get_rect()

    def update(self):
        ev = pygame.key.get_pressed()
        if ev[pygame.K_LEFT]:
            self.rect.x += -10
        if ev[pygame.K_RIGHT]:
            self.rect.x += 10
        if ev[pygame.K_DOWN]:
            self.rect.y += 10
        if ev[pygame.K_UP]:
            self.rect.y += -10


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
'''
