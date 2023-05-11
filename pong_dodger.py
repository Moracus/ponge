import random

import pygame.display

import pong1
from pong1 import *
pygame.init()
screen = pong1.screen

#sound
coin_sound = pygame.mixer.Sound("coin.wav")

#game variables
coin_count = 0
coin_font = pygame.font.SysFont("comicsans ms", 20,True)




class Dodge_paddle(pygame.sprite.Sprite):
    def __init__(self,img_name,x,y,width = 40,height = 10,paddle_speed=5):
        super().__init__()
        # global paddle_speed
        # paddle_speed = 5
        self.image = pygame.transform.scale(pygame.image.load(img_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = paddle_speed

    def update(self):
        self.rect.x -= self.speed
    @staticmethod
    def paddle_collsion():
        global run

        if pygame.sprite.spritecollideany(player,all_coming_paddle):
            run = False



all_sprites = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
player = Dodge_paddle(pdle1, 15,screen_height//2,100,15)
paddle1 = Dodge_paddle("items/blush_rect.png", 800,0)
paddle2 = Dodge_paddle("items/caramel_rect.png", 800,100)
paddle3 = Dodge_paddle("items/light salmon pink_rect.png", 850,150)
paddle4 = Dodge_paddle("items/purple navy_rect.png", 900,200)
paddle5 = Dodge_paddle("items/rose_rect.png", random.randint(801,900),250)
paddle6 = Dodge_paddle("items/Darkred_rect.png", random.randint(801,900),300)
paddle7 = Dodge_paddle("items/purple navy_rect.png", random.randint(801,900),350)
paddle8 = Dodge_paddle("items/light salmon pink_rect.png", random.randint(801,900),400)
paddle9 = Dodge_paddle("items/orange_rect.png", random.randint(801,900),450)
paddle10 = Dodge_paddle("items/caramel_rect.png", random.randint(801,900),480)
coin = Dodge_paddle("assets/img/coin.png", random.randint(801,900),random.randint(10,480),16,16)
coin1 = Dodge_paddle("assets/img/coin.png", random.randint(801,900),random.randint(10,480),16,16)
coin2 = Dodge_paddle("assets/img/coin.png", random.randint(801,900),random.randint(10,480),16,16)
coin3 = Dodge_paddle("assets/img/coin.png", random.randint(801,900),random.randint(10,480),16,16)
# coin4 = Dodge_paddle("coin.png", random.randint(801,900),random.randint(10,480),21,21)
# coin5 = Dodge_paddle("coin.png", random.randint(801,900),random.randint(10,480),21,21)


all_sprites.add(player)

all_coming_paddle = pygame.sprite.Group()
all_coming_paddle.add(paddle1)
all_coming_paddle.add(paddle2)
all_coming_paddle.add(paddle3)
all_coming_paddle.add(paddle4)
all_coming_paddle.add(paddle5)
all_coming_paddle.add(paddle6)
all_coming_paddle.add(paddle7)
all_coming_paddle.add(paddle8)
all_coming_paddle.add(paddle9)
all_coming_paddle.add(paddle10)
# all_coming_paddle.add(coin)

all_sprites.add(player)
coin_group.add(coin)
coin_group.add(coin1)
coin_group.add(coin2)
coin_group.add(coin3)
# coin_group.add(coin4)
# coin_group.add(coin5)


def check_coins():
    global coin_count,coins, coins_new
    for co in coin_group:
        if player.rect.colliderect(co):
            coin_sound.play()
            coin_count += 1
            pong1.coins = str(int(coins) + 1)
            co.rect.x = random.randrange(screen_width,screen_width+200)
            co.rect.y = random.randrange(10,screen_height-15)
        if co.rect.right < 0:
            co.rect.x = random.randrange(screen_width, screen_width + 200)
            co.rect.y = random.randrange(10, screen_height - 15)
    with open("coincount.txt","w") as f:
        f.write(pong1.coins)



    pygame.display.update()

dummy_coin = pygame.transform.scale(pygame.image.load("assets/img/coin.png"), (18, 18))


def draw():
    global coin_font

    dummy_coin = pygame.transform.scale(pygame.image.load("coin.png"), (18, 18))
    count_img = pygame.font.Font.render(coin_font, "X" + str(coin_count), True, WHITE)
    bg_img = pygame.transform.scale(pygame.image.load("items/bg/bg1.png").convert(),(screen_width,screen_height))
    screen.blit(bg2,(0,0))
    # screen.fill(GREY)
    all_sprites.draw(screen)
    all_coming_paddle.draw(screen)
    coin_group.draw(screen)
    all_coming_paddle.update()
    coin_group.update()
    Dodge_paddle.paddle_collsion()
    screen.blit(dummy_coin, (10, 20))
    screen.blit(count_img, (30, 15))

    pygame.display.update()
    # all_sprites.update()






def main():
    global run

    run = True
    while run:

        Clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        player_vel = 6
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player.rect.top>0:
            player.rect.y -= player_vel
        if keys[pygame.K_s] and player.rect.bottom <= screen_height:
            player.rect.y += player_vel
        #game logic
        for pad in all_coming_paddle:
            if pad.rect.right < 0:
                pad.rect.x = random.randint(800,950)
                pad.rect.y = random.randint(5,screen_height-20)

                pad.speed = random.randint(4,8)

        draw()
        check_coins()
        pygame.display.flip()

