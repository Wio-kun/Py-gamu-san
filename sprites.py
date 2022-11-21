import pygame as pg
vec = pg.math.Vector2

player_img = pg.image.load("knight.png")
player_img = pg.transform.scale(player_img, (120,165))
boss_image = pg.image.load("black_knight.png")
boss_image = pg.transform.scale(boss_image, (148, 220))
bg_image = pg.image.load("background.png")
bg_image = pg.transform.scale(bg_image, (1440, 720))

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
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
        if keys[pg.K_d]:
            self.pos.x += self.speed

class Boss(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = boss_image
        self.rect = self.image.get_rect()
        self.pos = vec(1325, 610)
        self.rect.center = self.pos
        self.speed = 2
        self.direction_x = -5
        self.direction_y = 0
    
    def update(self):
        self.rect.center = self.pos

        self.pos.x += self.direction_x
        self.pos.y += self.direction_y

        if self.pos.x < 75:
            self.direction_x = 0
            self.direction_y = -5
            self.pos.x = 75

        if self.pos == vec(75, 605):
            self.image = pg.transform.flip(self.image, True, False)

        if self.pos.y < 115:
            self.direction_x = 5
            self.direction_y = 0
            self.pos.y = 115

        if self.pos == vec(1325, 120):
            self.image = pg.transform.flip(self.image, True, False)

        if self.pos.x > 1325:
            self.direction_x = 0
            self.direction_y = 5
            self.pos.x = 1325

        if self.pos.y > 610:
            self.direction_x = -5
            self.direction_y = 0
            self.pos.y = 610

class Background(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)  #call Sprite initializer
        
        
