import pygame as pg
vec = pg.math.Vector2

player_img = pg.image.load("knight.png")
player_img = pg.transform.scale(player_img, (76,148))
boss1_image = pg.image.load("black_knight.png")
boss1_image = pg.transform.scale(boss1_image, (120, 208))
player_img_180 = pg.transform.flip(player_img, True, False)
boss1_image_180 = pg.transform.flip(boss1_image, True, False)

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = player_img
        self.rect = self.image.get_rect()
        self.image_180 = player_img_180
        self.pos = vec(608, 619)
        self.rect.center = self.pos
        self.speed = 4
        self.hp = 1000
        self.immune = False


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

        if self.pos.x <38:
            self.pos.x = 38
        if self.pos.x >1178:
            self.pos.x = 1178
        if self.pos.y <150:
            self.pos.y = 150
        if self.pos.y >1140:
            self.pos.y = 1140

class Boss(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = boss1_image
        self.rect = self.image.get_rect()
        self.pos = vec(608, 155)
        self.rect.center = self.pos
        self.speed = 2
        self.direction_x = 0
        self.direction_y = 2
        self.hp = 10000
    
    def update(self):
        self.rect.center = self.pos

        self.pos.x += self.direction_x
        self.pos.y += self.direction_y

        if self.pos.x < self.game.knight.pos.x:
            self.direction_x = 2
            self.image = boss1_image_180
        if self.pos.x > self.game.knight.pos.x:
            self.direction_x = -2
            self.image = boss1_image
        if self.pos.y < self.game.knight.pos.y:
            self.direction_y = 2
        if self.pos.y > self.game.knight.pos.y:
            self.direction_y = -2
