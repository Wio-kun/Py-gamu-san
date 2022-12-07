import pygame as pg
from random import randint
vec = pg.math.Vector2

player_img = pg.image.load("knight_fight.png")
player_img = pg.transform.scale(player_img, (144,144))
boss_image = pg.image.load("king.png")
boss_image = pg.transform.scale(boss_image, (135, 235))
guard_image = pg.image.load("black_knight_fight")
guard_image = pg.transform.scale(guard_image, (185, 225))
player_img_180 = pg.transform.flip(player_img, True, False)
boss_image_180 = pg.transform.flip(boss_image, True, False)
guard_image_180 = pg.transform.flip(boss_image, True, False)

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.knight_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = player_img
        self.rect = self.image.get_rect()
        self.image_180 = player_img_180
        self.pos = vec(608, 619)
        self.rect.center = self.pos
        self.speed = 4
        self.hp = 1000
        self.immune = False
        self.attack_cooldown = False


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
            if keys[pg.K_SPACE] and self.attack_cooldown == False:
                self.attack_right()
                
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = player_img
            if keys[pg.K_SPACE] and self.attack_cooldown == False:
                self.attack_left()


        if self.pos.x <72:
            self.pos.x = 72
        if self.pos.x >1144:
            self.pos.x = 1144
        if self.pos.y <150:
            self.pos.y = 150
        if self.pos.y >1140:
            self.pos.y = 1140


    def attack_left(self):
        Sword(self.game, self.pos.x - 50, self.pos.y)
    def attack_right(self):
        Sword(self.game, self.pos.x + 50, self.pos.y)


class Sword(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.sword_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface([120, 208])
        self.image.fill ((255,255,255))
        self.pos = vec(x, y)
        self.rect = self.image.get_rect()
     
        self.rect.center = self.pos

    def update(self):
        self.rect.center = self.pos
     



class Boss(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.enemy_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = boss_image
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
            self.image = boss_image_180
        if self.pos.x > self.game.knight.pos.x:
            self.direction_x = -2
            self.image = boss_image
        if self.pos.y < self.game.knight.pos.y:
            self.direction_y = 2
        if self.pos.y > self.game.knight.pos.y:
            self.direction_y = -2

class Guard(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.enemy_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = guard_image
        self.rect = self.image.get_rect()
        self.pos = vec(608, 155)
        self.rect.center = self.pos
        self.speed = 2
        self.direction_x = 0
        self.direction_y = 2
        self.hp = 1000

    def update(self):
        self.rect.center = self.pos

        self.pos.x += self.direction_x
        self.pos.y += self.direction_y

        if self.pos.x < self.game.knight.pos.x:
            self.direction_x = 2
            self.image = boss_image_180
        if self.pos.x > self.game.knight.pos.x:
            self.direction_x = -2
            self.image = boss_image
        if self.pos.y < self.game.knight.pos.y:
            self.direction_y = 2
        if self.pos.y > self.game.knight.pos.y:
            self.direction_y = -2