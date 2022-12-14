import pygame as pg
from random import randint
vec = pg.math.Vector2

player_img = pg.image.load("knight_fight.png")
player_img = pg.transform.scale(player_img, (108,108))
boss_image = pg.image.load("king.png")
boss_image = pg.transform.scale(boss_image, (81, 141))
guard_image = pg.image.load("black_knight_fight.png")
guard_image = pg.transform.scale(guard_image, (111, 135))
player_img_180 = pg.transform.flip(player_img, True, False)
boss_image_180 = pg.transform.flip(boss_image, True, False)
guard_image_180 = pg.transform.flip(guard_image, True, False)

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
        self.hp = 1200
        self.immune = False
        self.attack_cooldown = False
        self.last_attack = 0

        self.energy = 100


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
            if keys[pg.K_SPACE] and self.energy >= 100:
                self.attack_left()
                self.energy = 0
                
                
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = player_img
            if keys[pg.K_SPACE] and self.energy >= 100:
                self.energy = 0
                self.attack_right()

        if self.energy < 100:
            self.energy += 1.5

        if self.pos.x <54:
            self.pos.x = 54
        if self.pos.x >1162:
            self.pos.x = 1162
        if self.pos.y <175:
            self.pos.y = 175
        if self.pos.y >1158:
            self.pos.y = 1158


    def attack_left(self):
        Sword(self.game, self.pos.x - 150, self.pos.y)
    def attack_right(self):
        Sword(self.game, self.pos.x + 150, self.pos.y)


class Sword(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.sword_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface([115, 115])
        self.image.fill ((255,255,255))
        #self.image.set_colorkey((255,255,255))
        self.pos = vec(x, y)
        self.rect = self.image.get_rect()
        self.swing_timer = pg.time.get_ticks()
        self.spawn_tick = pg.time.get_ticks()
        self.rect.center = self.pos
        self.passive_king = False
        self.passive_black_knight = False
        self.last_attack = 0

    def update(self):
        self.rect.center = self.pos
        now = pg.time.get_ticks()

        self.strike_king = pg.sprite.spritecollide(self.game.king, self.game.sword_group, False, False)
        if self.strike_king:
            if not self.passive_king:
                self.game.king.hp-=500
                self.passive_king = True
                            
                if self.game.king.hp <= 0:
                    self.game.king.kill()
        
        self.strike_guard = pg.sprite.groupcollide(self.game.black_knight_group, self.game.sword_group, False, False)
        if self.strike_guard:
            if not self.passive_black_knight:
                self.game.black_knight.hp-=500
                self.passive_black_knight = True
                            
                if self.game.black_knight.hp <= 0:
                    self.game.black_knight.kill()
        
        if now - self.spawn_tick > 100:
            self.kill()


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



        if self.pos.x < self.game.knight.pos.x + 10:
            self.direction_x = 2
        if self.pos.x > self.game.knight.pos.x - 10:
            self.direction_x = -2
        if self.pos.y < self.game.knight.pos.y:
            self.direction_y = 2
        if self.pos.y > self.game.knight.pos.y:
            self.direction_y = -2


class Guard(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemy_group, game.black_knight_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = guard_image
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.speed = 2
        self.direction_x = 0
        self.direction_y = 2
        self.hp = 1000

    def update(self):
        self.rect.center = self.pos

        self.pos.x += self.direction_x
        self.pos.y += self.direction_y


        if self.pos.x < self.game.knight.pos.x + 10:
            self.direction_x = 2
            self.image = guard_image_180
        if self.pos.x > self.game.knight.pos.x - 10:
            self.direction_x = -2
            self.image = guard_image
        if self.pos.y < self.game.knight.pos.y:
            self.direction_y = 2
        if self.pos.y > self.game.knight.pos.y:
            self.direction_y = -2