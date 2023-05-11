import random

import pygame
import pong1
import pong_dodger
from pong_dodger import *
from pong1 import *

pygame.init()
ic = pygame.image.load("h game/icon2.ico")
screen_width = pong1.screen_width
screen_height = pong1.screen_height
icon = pygame.display.set_icon(ic)
pygame.display.set_caption("ponge","PONGE")

screen = pong1.screen

fps = 60
#colors
TURQUOISE = (0,168,243)
BLACK = (0,0,0)

#vars
pong1.game_start = 0
price = 50
#game_start = 0 is startscreen
#game_start = 1 is double player
#game_start = 2 is single player
#game_start = -2 is shop
# game_start = -3 #shop>padles

#images
def load_image(img):
    return pygame.image.load(img).convert_alpha()
btn_width = 325
btn_height = 65

bg = pygame.transform.scale(pygame.image.load("h game/no dust bg.png"),(screen_width,screen_height)).convert_alpha()
singleplayer_btn = pygame.transform.scale(pygame.image.load("h game/single_player__1_-removebg-preview.png"), (btn_width, btn_height)).convert_alpha()
singleplayer_btn2 = pygame.transform.scale(pygame.image.load("h game/single_player-removebg-preview.png"), (btn_width, btn_height)).convert_alpha()
doubleplayer_btn = pygame.transform.scale(load_image("h game/double_player__1_-removebg-preview.png"), (btn_width, btn_height)).convert_alpha()
doubleplayer_btn2 = pygame.transform.scale(load_image("h game/double_player-removebg-preview.png"), (btn_width, btn_height)).convert_alpha()
earncoins_btn = pygame.transform.scale(load_image("h game/earn_coins__1_-removebg-preview.png"), (btn_width-50, btn_height-10)).convert_alpha()
earncoins_btn2 = pygame.transform.scale(load_image("h game/earn_coins-removebg-preview.png"), (btn_width-50, btn_height-10)).convert_alpha()
credits_btn2 = pygame.transform.scale(load_image("h game/credits__1_-removebg-preview.png"),(btn_width-60,btn_height-10)).convert_alpha()
credits_btn = pygame.transform.scale(load_image("h game/credits-removebg-preview.png"),(btn_width-60,btn_height-10)).convert_alpha()
music_btn = pygame.transform.scale(load_image("h game/music2.png"),(40,40))
music_btn2 = pygame.transform.scale(load_image("h game/music no2.png"),(40,40))
shop_btn = pygame.transform.scale(load_image("h game/shop (1).png"),(80,80))
shop_btn2 = pygame.transform.scale(load_image("h game/shop.png"),(80,80))

game_name = load_image("h game/Ponge.png").convert_alpha()
game_name2 = pygame.transform.scale(game_name,(400,100)).convert_alpha()
coin_box = pygame.transform.scale(load_image("assets/img/paddles/solids/blue_rect.png"),(100,25)).convert_alpha()

#rects
singleplayer_btn_rect = pygame.Rect(screen_width // 2 - btn_width // 2, 200,btn_width,btn_height)
doubleplayer_btn_rect = pygame.Rect(screen_width // 2 - btn_width // 2, 280,btn_width,btn_height)
earncoins_btn_rect = pygame.Rect(20+screen_width // 2 - btn_width // 2, 360,earncoins_btn.get_width(),earncoins_btn.get_height())
credits_btn_rect = pygame.Rect(30+screen_width // 2 - btn_width // 2, 430,credits_btn.get_width(),credits_btn.get_height())
shop_btn_rect = pygame.Rect(screen_width-100,screen_height-100,80,80)

music_btn_rect = pygame.Rect(screen_width - 50, 50, 50, 40)
music_btn2_rect = pygame.Rect(screen_width - 50, 50, 50, 40)







class Screen_balls(Balls):
    def __init__(self, ball_name,diameter):
        super().__init__()
        ball_image= pygame.image.load("items/" + ball_name).convert()
        self.diameter = diameter
        self.image = pygame.transform.scale(ball_image,(diameter,diameter)).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.velocity = [1,1]
        self.rect = pygame.Rect(screen_width // 2, screen_height // 2, self.diameter,self.diameter)






screen_balls = pygame.sprite.Group()
ball1 = Screen_balls("blue_Balloon.png",20)
ball2 = Screen_balls("red_Balloon.png",20)
ball2.rect.x = screen_width
ball2.rect.y = 100
ball3 = Screen_balls("pink_Balloon.png",20)
ball3.rect.x = 0
ball3.rect.y = 0
ball4 = Screen_balls("blue_Balloon.png",random.randint(20,30))
ball4.rect.x = random.randrange(15,screen_width-10)
ball4.rect.y = random.randrange(15,screen_height-10)
ball5 = Screen_balls("pink_Balloon.png",30)
ball5.rect.x = random.randrange(15,screen_width-10)
ball5.rect.y = random.randrange(15,screen_height-10)
ball6 = Screen_balls("blue_Balloon.png",random.randint(30,40))
ball6.rect.x = random.randrange(15,screen_width-10)
ball6.rect.y = random.randrange(15,screen_height-10)
ball7 = Screen_balls("red_Balloon.png",random.randint(20,50))
ball7.rect.x = random.randrange(15,screen_width-10)
ball7.rect.y = random.randrange(15,screen_height-10)
ball8 = Screen_balls("red_Balloon.png",random.randint(10,50))
ball8.rect.x = random.randrange(15,screen_width-10)
ball8.rect.y = random.randrange(15,screen_height-10)
ball9 = Screen_balls("red_Balloon.png",random.randint(10,20))
ball9.rect.x = random.randrange(15,screen_width-10)
ball9.rect.y = random.randrange(15,screen_height-10)
ball10 = Screen_balls("blue_Balloon.png",random.randint(20,30))
ball10.rect.x = random.randrange(15,screen_width-10)
ball10.rect.y = random.randrange(15,screen_height-10)
ball11 = Screen_balls("pink_Balloon.png",random.randint(10,20))
ball11.rect.x = random.randrange(15,screen_width-10)
ball11.rect.y = random.randrange(15,screen_height-10)
ball12 = Screen_balls("pink_Balloon.png",random.randint(30,50))
#game variables
pong1.game_start = 0



screen_balls.add(ball2)
screen_balls.add(ball1)
screen_balls.add(ball3)
screen_balls.add(ball4)
screen_balls.add(ball5)
screen_balls.add(ball6)
screen_balls.add(ball7)
screen_balls.add(ball8)
screen_balls.add(ball9)
screen_balls.add(ball10)
screen_balls.add(ball11)
screen_balls.add(ball12)

print(pong1.coins)
def draw():
    global pdle_x, pdle_y,buy_btn_rect
    if pong1.game_start == 0:
        coin_box_img = pygame.font.Font.render(coin_font,pong1.coins, True, WHITE)
        music_btn.set_colorkey(WHITE)
        music_btn2.set_colorkey(WHITE)

        screen.blit(bg, (0, 0))
        screen_balls.draw(screen)
        screen_balls.update()
        screen.blit(game_name2, (screen_width // 2 - 200, 50))

        screen.blit(coin_box, (screen_width - 110, 2))
        screen.blit(coin_box_img, (screen_width - 87, -5))
        screen.blit(dummy_coin, (screen_width - 105, 3))

        screen.blit(singleplayer_btn, (screen_width // 2 - btn_width // 2, 200))
        screen.blit(doubleplayer_btn, (screen_width // 2 - btn_width // 2, 280))
        screen.blit(earncoins_btn, (20 + screen_width // 2 - btn_width // 2, 360))
        screen.blit(credits_btn, (30 + screen_width // 2 - btn_width // 2, 430))
        screen.blit(shop_btn, (screen_width - 100, screen_height - 100))

        screen.blit(music_btn, (screen_width - 50, 50))

    if pong1.music == 0:
        screen.blit(music_btn2, (screen_width - 50, 50))




def check_mouse():
    global  pos
    if pong1.game_start == 0:
        pos = pygame.mouse.get_pos()
        if singleplayer_btn_rect.collidepoint(pos):
            screen.blit(singleplayer_btn2, (screen_width // 2 - btn_width // 2, 200))

        elif doubleplayer_btn_rect.collidepoint(pos):
            screen.blit(doubleplayer_btn2, (screen_width // 2 - btn_width // 2, 280))
        elif earncoins_btn_rect.collidepoint(pos):
            screen.blit(earncoins_btn2, (20 + screen_width // 2 - btn_width // 2, 360))
        elif credits_btn_rect.collidepoint(pos):
            screen.blit(credits_btn2, (30 + screen_width // 2 - btn_width // 2, 430))
        elif shop_btn_rect.collidepoint(pos):
            screen.blit(shop_btn2, (screen_width - 100, screen_height - 100))












def main():
    global game_start
    run = True

    while run:
        with open("coincount.txt", "r") as c:
            pong1.coins = c.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.K_ESCAPE:
                run = False

            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if singleplayer_btn_rect.collidepoint(pos) and pong1.game_start == 0:
                    if pygame.mouse.get_pressed(3)[0] == 1:
                        pong1.game_start = 2
                        pong1.main()
                elif doubleplayer_btn_rect.collidepoint(pos) and pong1.game_start == 0:
                    if pygame.mouse.get_pressed(3)[0] == 1:
                        pong1.game_start = 1
                        pong1.main()
                elif earncoins_btn_rect.collidepoint(pos) and pong1.game_start == 0:
                    if pygame.mouse.get_pressed(3)[0] == 1:
                        pong_dodger.main()
                    #music control
                elif music_btn_rect.collidepoint(pos) and pong1.game_start == 0:
                    if pygame.mouse.get_pressed(5)[0]:
                        if pong1.music:
                            pong1.music = 0
                            pygame.mixer.music.pause()
                        else:
                            pong1.music = 1
                            pygame.mixer.music.unpause()
                #shop
                if shop_btn_rect.collidepoint(pos) and pong1.game_start == 0:
                    if pygame.mouse.get_pressed(3)[0]:

                        pong1.game_start = -2 #shop
                        shop_func()








        draw()

        check_mouse()
        # check_paddles()
        # print(player1.imagename)
        pygame.display.update()
        Clock.tick(fps)


    pygame.quit()


main()