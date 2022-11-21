import pygame as pg
vec = pg.math.Vector2

player_img = pg.image.load("knight.png")
player_img = pg.transform.scale(player_img, (76,148))
boss_image = pg.image.load("black_knight.png")
boss_image = pg.transform.scale(boss_image, (120, 208))
player_img_180 = pg.transform.flip(player_img, True, False)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.image_180 = player_img_180
        self.pos = vec(500, 500)
        self.rect.center = self.pos
        self.speed = 3


    def update(self):
        self.rect.center = self.pos

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.image = player_img_180
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = player_img

class Boss(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = boss_image
        self.rect = self.image.get_rect()
        self.pos = vec(1156, 155)
        self.rect.center = self.pos
        self.speed = 2
        self.direction_x = 0
        self.direction_y = 5
        self.image = pg.transform.flip(self.image, True, False)
    
    def update(self):
        self.rect.center = self.pos

        self.pos.x += self.direction_x
        self.pos.y += self.direction_y

        if self.pos.x < 60:
            self.direction_x = 0
            self.direction_y = -5
            self.pos.x = 60

        if self.pos == vec(60, 1095):
            self.image = pg.transform.flip(self.image, True, False)

        if self.pos.y < 155:
            self.direction_x = 5
            self.direction_y = 0
            self.pos.y = 155

        if self.pos == vec(1156, 160):
            self.image = pg.transform.flip(self.image, True, False)

        if self.pos.x > 1156:
            self.direction_x = 0
            self.direction_y = 5
            self.pos.x = 1156

        if self.pos.y > 1100:
            self.direction_x = -5
            self.direction_y = 0
            self.pos.y = 1100

