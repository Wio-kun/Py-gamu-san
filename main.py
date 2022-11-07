import pygame as pg

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GRØNN = (77,168,25)
MINT = (150,200,175)
PURPLE = (175,150,225)

screen = pg.display.set_mode((1000,1000))
player_img = pg.image.load("black_knight.png")
player_img = pg.transform.scale(player_img, (160,256))

fps_counter = 0
x = 0
y = 0

speed = 5
FPS = 120
clock = pg.time.Clock()

direction_x = + 1
direction_y = + 1

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    screen.fill(MINT)

    keys = pg.key.get_pressed()

    if keys [pg.K_w]:
        y -= speed
    if keys [pg.K_a]:
        x -= speed
    if keys [pg.K_s]:
        y += speed
    if keys [pg.K_d]:
        x += speed

    if x > 1160:
        x = 1160
    if x < -160:
        x = -160
    if y > 1256:
        y = 256
    if y < -744:
        y = -744

    screen.blit(player_img, (x,y))


    pg.display.update()