import pygame
import random


class Player:
    pass


class Meteor:
    pass


pygame.init()
size = width, height = 1200, 675
sc = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()

player_icon = pygame.image.load("player.png")
player_x = 650
player_y = 450

platform_icon = pygame.image.load("platform.png")
list_platforms = [
    platform_icon
]
platform_x = 200
platform_y = 375

meteor_icon = pygame.image.load("meteor.png")
meteor_x = 500
meteor_y = 0

gravity = 5
speed = 13
BLACK = (0, 0, 0)

background_image = pygame.image.load("volcanoes.jpg")

isJump = False
jumpCount = 10
flag_space = True
running = True
flag_meteor = False
count = 0
score = 0


def kill_meteor():
    sc.blit(platform_icon, (platform_x, platform_y))
    sc.blit(player_icon, (player_x, player_y))
    pygame.display.update()

# TODO: пересмотри уроки создания игры:
#   1) создание классов игровых объектов: герой, метеор
#   2) сделай блок инициализации, где ты создаешь все объекты и координаты
#   3) важно - метеоры нужно создавать как список метеоров, их же может быть много!


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_rect = player_icon.get_rect(topleft=(player_x, player_y))
    meteor_rect = meteor_icon.get_rect(topleft=(meteor_x, meteor_y))

    #
    if player_rect.colliderect(meteor_rect):
        score += 10
        print(score)

    meteor_y += gravity
    if meteor_y >= 563:
        kill_meteor()
        count -= 1
        meteor_y = 0

    sc.blit(background_image, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_d]:
        player_x += speed
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            player_y -= (jumpCount * abs(jumpCount)) * 0.7
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    if player_x < 0:
        player_x = 0
    elif player_x > width - player_icon.get_width():
        player_x = width - player_icon.get_width()

    if count == 0:
        count += 1
        pos_meteor_for_x = random.randint(0, 1100)

    sc.blit(platform_icon, (platform_x, platform_y))
    sc.blit(player_icon, (player_x, player_y))
    sc.blit(meteor_icon, (pos_meteor_for_x, meteor_y))

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
