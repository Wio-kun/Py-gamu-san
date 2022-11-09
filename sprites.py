import pygame as pg
vec = pg.math.Vector2

player_img = pg.image.load("knight.png")
player_img = pg.transform.scale(player_img, (120,165))

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100, 100)
        self.rect.center = self.pos
        self.speed = 3

    def update(self):
        self.rect.center = self.pos

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= 3
        if keys[pg.K_s]:
            self.pos.y += 3
        if keys[pg.K_a]:
            self.pos.x -= 3
        if keys[pg.K_d]:
            self.pos.x += 3