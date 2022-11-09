import pygame as pg
from sprites import *

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GRØNN = (77,168,25)
MINT = (150,200,175)
PURPLE = (175,150,225)

all_sprites = pg.sprite.Group()

Knight = Player()
all_sprites.add(Knight)

screen = pg.display.set_mode((1000,1000))

FPS = 120
clock = pg.time.Clock()

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    screen.fill(MINT)

    all_sprites.update()

    all_sprites.draw(screen)

    pg.display.update()