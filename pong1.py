import pygame
from pygame.locals import *
import random
from easygui import *



pygame.init()
pygame.font.init()
screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))

#colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
WHITE2 = ( 255, 255, 255,128)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
GREY = (105,105,105)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
Clock = pygame.time.Clock()
#game variabl3es
player_2_score = 0 #right side
player_1_score = 0 #left side

game_start = 0

with open("coincount.txt", "r") as c:
    coins = c.read()




def equipdata():
    global equip1, equip2, equip3, equip4, equip5, equip6, equip7, equip8, equip9, equip10

    with open("data/equipdata1", "r") as equi1:
        equip1 = int(equi1.read())
    with open("data/equipdata2", "r") as equi2:
        equip2 = int(equi2.read())
    with open("data/equipdata3", "r") as equi3:
        equip3 = int(equi3.read())
    with open("data/equipdata4", "r") as equi4:
        equip4 = int(equi4.read())
    with open("data/equipdata5", "r") as equi5:
        equip5 = int(equi5.read())
    with open("data/equipdata6", "r") as equi6:
        equip6 = int(equi6.read())
    with open("data/equipdata7", "r") as equi7:
        equip7 = int(equi7.read())
    with open("data/equipdata8", "r") as equi8:
        equip8 = int(equi8.read())
    with open("data/equipdata9", "r") as equi9:
        equip9 = int(equi9.read())
    with open("data/equipdata10", "r") as equi10:
        equip10 = int(equi10.read())

    return equip1, equip2, equip3, equip4, equip5, equip6, equip7, equip8, equip9, equip10



def buydata():
    global  bought1, bought2, bought3, bought4, bought5, bought6, bought7, bought8, bought9, bought10
    with open("data/buydata1","r") as buy1:
        bought1 = int(buy1.read())
    with open("data/buydata2","r") as buy2:
        bought2 = int(buy2.read())
    with open("data/buydata3","r") as buy3:
        bought3 = int(buy3.read())
    with open("data/buydata4","r") as buy4:
        bought4 = int(buy4.read())
    with open("data/buydata5","r") as buy5:
        bought5 = int(buy5.read())
    with open("data/buydata6","r") as buy6:
        bought6 = int(buy6.read())
    with open("data/buydata7","r") as buy7:
        bought7 = int(buy7.read())
    with open("data/buydata8","r") as buy8:
        bought8 = int(buy8.read())
    with open("data/buydata9","r") as buy9:
        bought9 = int(buy9.read())
    with open("data/buydata3","r") as buy10:
        bought10 = int(buy10.read())

    return bought1, bought2, bought3, bought4, bought5, bought6, bought7, bought8, bought9, bought10


buy_list = list(buydata())




def load_items(item,width = 20,height = 90):
    return pygame.transform.scale(pygame.image.load(item),(width,height))

def load_text(text, color,size = 30, fontt = "comicsans ms"):
    font = pygame.font.SysFont(fontt,size)
    return pygame.font.Font.render(font,text,True,color)

def load_image(img):
    return pygame.image.load(img).convert_alpha()

def popup():
    title = "Ponge"
    msg = "Not enough coins"
    msgbox(msg,title)

#music
music = 1

pygame.mixer.music.load("assets/music/8_bit_ice_cave_lofi.mp3")
pygame.mixer.music.play(-1, 0.0, 3000)
pop = pygame.mixer.Sound("assets/sound effects/Pop.ogg")

#img loading
#game items
#paddles

#solid padles
bg2 = pygame.transform.scale(pygame.image.load("h game/no dust bg.png"),(screen_width,screen_height)).convert_alpha()
pdle1 = "assets/img/paddles/solids/red_paddle(solid).png"
pdle2 = "assets/img/paddles/solids/orange_paddle.png"
pdle3 = "assets/img/paddles/solids/caramel_paddle.png"#prblm
pdle4 = "assets/img/paddles/solids/blush_paddle.png"
pdle5 = "assets/img/paddles/solids/salmonpink_paddle.png"#prblml
# pdle6 = "assets/img/paddles/solids/blush_paddle.png"
# pdle7 = "assets/img/paddles/solids/yellow_paddle(solid).png"#prnlm
# pdle8 = "assets/img/paddles/solids/darkred_paddle.png" #prbllm
# pdle9 = "assets/img/paddles/solids/salmonpink_paddle.png"
# pdle10 = "assets/img/paddles/solids/navy_paddle.png" #prblm

# pdle_list = [pdle1,pdle2,pdle3,pdle4,pdle5,pdle6,pdle7,pdle8,pdle9,pdle10]


#metals
pdle6 = "assets/img/paddles/metals/blue_paddle(polish metal).png"
pdle7 = "assets/img/paddles/metals/green_paddle(polish metal).png"
pdle8 = "assets/img/paddles/metals/red_paddle(polished metal).png"
pdle9 = "assets/img/paddles/metals/yellow _paddle(polish metal).png"

#misc
pdle10 = "assets/img/paddles/misc/glasspaddle2.png"
pdle16 = "assets/img/paddles/paddle.png"

#loading imgs
paddle_btn1 = pygame.transform.scale(pygame.image.load("h game/paddle_btn1.png"),(300,100))

paddle_btn2 = pygame.transform.scale(pygame.image.load("h game/paddle_btn2.png"),(300,100))
balls_btn1 = pygame.transform.scale(pygame.image.load("h game/balls_btn2.png"),(300,100))
balls_btn2 = pygame.transform.scale(pygame.image.load("h game/balls_btn1.png"),(300,100))

equipped_btn = load_items("h game/equipped.png",80,30)


#coordinates
pdle_x = 100
pdle_y = 20

#rects
paddle_btn1_rect = pygame.Rect(screen_width//2-150, 100,300,100)
balls_btn1_rect = pygame.Rect(screen_width//2-150, 300,300,100)
buy_btn_rect = pygame.Rect(pdle_x - 10, pdle_y + 100, 50, 30)
text1 = load_text("Not enough coins", WHITE, 50, "Sans")
text2 = load_text("Ok", WHITE, 20)
text2_rect = pygame.Rect(text1.get_width() + 200, screen_height // 2 - text1.get_height() + 80, 20, 20)



pressed_ok = 0
def fading_text():
    global  pressed_ok
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if text2_rect.collidepoint(pos):
                    if pygame.mouse.get_pressed(5)[0]:
                        print("1")
                        pressed_ok = 1

        if pressed_ok == 0:
            screen.blit(text1, (screen_width // 2 - text1.get_width() // 2, screen_height // 2 - text1.get_height()))
            screen.blit(text2, (text2_rect.x, text2_rect.y))
            pygame.draw.rect(screen, WHITE, text2_rect, 2)
        pygame.display.update()
        Clock.tick(60)




class Balls(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ball_width = 21
        ball_height = 21
        ball_img = pygame.image.load("assets/img/balls/red_Balloon.png").convert_alpha()
        ball_img2 = pygame.transform.scale(ball_img,(ball_width,ball_height)).convert_alpha()
        self.image = ball_img2
        self.image.set_colorkey(BLACK)
        self.rect = pygame.Rect(screen_width//2, screen_height//2,ball_width,ball_height)


        self.velocity = [random.randint(4,8), random.randint(-8,8)]

    def update(self):
        if game_start == 1 or game_start == 2 :
            # pygame.time.wait(3000)
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

            # collisions with walls/ bouncing from walls
            if self.rect.right >= screen_width:
                self.velocity[0] = -self.velocity[0]
            elif self.rect.left <= 0:
                self.velocity[0] = -self.velocity[0]
            elif self.rect.top < 0:
                self.velocity[1] = - self.velocity[1]
            elif self.rect.bottom > screen_height:
                self.velocity[1] = - self.velocity[1]
            elif player1.rect.colliderect(ball.rect):
                pop.play()
                ball.velocity[0] = - ball.velocity[0]
                self.velocity[1] = random.randint(-8, 8)
            if player2.rect.colliderect(ball.rect):
                pop.play()
                ball.velocity[0] = - ball.velocity[0]
                self.velocity[1] = random.randint(-8, 8)

        elif game_start == 0 : #start screen
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            if self.rect.right >= screen_width:
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = random.randint(-1, 1)
            elif self.rect.left <= 0:
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = random.randint(-1, 1)
            elif self.rect.top <= 0:
                self.velocity[1] = - self.velocity[1]
                self.velocity[1] = random.randint(-1, 1)
            elif self.rect.bottom >= screen_height+5:
                self.velocity[1] = - self.velocity[1]
                self.velocity[1] = random.randint(-1, 1)


class Paddle(pygame.sprite.Sprite):

    def __init__(self,x,y,image_name,paddle_width = 20, paddle_height = 100):
        super().__init__()
        self.imagename = image_name
        paddle_img = pygame.image.load(image_name)
        self.image = pygame.transform.scale(paddle_img,(paddle_width,paddle_height))
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self):
        dy = 0

        # player1_controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.rect.y > 0:
            dy -= speed
        if keys[pygame.K_s] and player1.rect.bottom < screen_height:
            dy += speed
        dy2 = 0
        if game_start == 1:
            if keys[pygame.K_UP] and player2.rect.top > 0:
                dy2 -= speed
            if keys[pygame.K_DOWN] and player2.rect.bottom < screen_height:
                dy2 += speed
        elif game_start == 2:
            dy2 = 0
            comp_speed = [2, 4]  # handicap 1
            if ball.rect.centery < player2.rect.centery and player2.rect.y > 0:  # ball is above the paddle and moving the paddle  up
                if ball.rect.x > screen_width // 2 + 50:  # handicap
                    # 2
                    dy2 -= random.choice(comp_speed)
            if ball.rect.centery > player2.rect.centery and player2.rect.bottom < screen_height:  # ball is below the paddle
                if ball.rect.x > screen_width // 2 + 50:
                    dy2 += random.choice(comp_speed)


        #update player coordinats
        player1.rect.y += dy
        player2.rect.y += dy2

#makingball
ball = Balls()
ball.rect.x = screen_width//2
ball.rect.y = screen_height//2



all_balls = pygame.sprite.Group()
all_balls.add(ball)



def restart():
    pygame.time.wait(1000)
    ball.rect.x = screen_width // 2
    ball.rect.y = screen_height // 2
    player1.rect.x , player1.rect.y = 25,250
    player2.rect.x, player2.rect.y = screen_width-45,250
    ball.velocity = [random.randint(4, 8), random.randint(-8, 8)]

    # pygame.time.wait(2000)


def add_paddles(pdle_no):
    with open("all_paddles.txt","w") as pdl:
        pdl.write(pdle_no)

def write_equipdata(file,str="1"):
    with open(file,"w+") as pdle:
        pdle.write(str)

def update_coins(coins,pricee):
    coins = str(int(coins) - pricee)
    with open("coincount.txt", "w+") as c:
        c.write(coins)




def score_inc():
    global player_1_score, player_2_score,player1, player2
    if game_start == 1 or game_start == 2:
        if ball.rect.left < player1.rect.right - 7:
            if player_2_score < 5:
                player_2_score += 1
                restart()
        elif ball.rect.right - 8 > player2.rect.left:
            if player_1_score < 5:
                player_1_score += 1
                restart()



def draw_paddles(pdlee,pdlee2,pdle_y = 20):
    global pdle_x
    screen.blit(load_items(pdlee), (pdle_x ,pdle_y))
    screen.blit(load_items(pdlee2), (pdle_x ,pdle_y+280))
    if pdle_x < screen_width:
        pdle_x += 150
    else:
        pdle_x = 100


coin_img = load_items("assets/img/coin.png",20,20)
coin_x = pdle_x - 20
price = 50
price_txt = load_text(str(price),WHITE,25)
price_txt2 = load_text(str(price+50),WHITE,25)


equip_btn1 = load_items("h game/equip_btn1.png",50,30)
equip_btn2 = load_items("h game/equip_btn1.png",50,30)
equip_btn3 = load_items("h game/equip_btn1.png",50,30)
equip_btn4 = load_items("h game/equip_btn1.png",50,30)
equip_btn5 = load_items("h game/equip_btn1.png",50,30)
equip_btn6 = load_items("h game/equip_btn1.png",50,30)
equip_btn7 = load_items("h game/equip_btn1.png",50,30)
equip_btn8 = load_items("h game/equip_btn1.png",50,30)
equip_btn9 = load_items("h game/equip_btn1.png",50,30)
equip_btn10 = load_items("h game/equip_btn1.png",50,30)


equip_btn_rect1 = pygame.Rect(pdle_x, pdle_y + 120, 50, 30)
equip_btn_rect2 = pygame.Rect(pdle_x+150, pdle_y + 120, 50, 30)
equip_btn_rect3 = pygame.Rect(pdle_x+300, pdle_y + 120, 50, 30)
equip_btn_rect4 = pygame.Rect(pdle_x+450, pdle_y + 120, 50, 30)
equip_btn_rect5 = pygame.Rect(pdle_x+600, pdle_y + 120, 50, 30)
equip_btn_rect6 = pygame.Rect(pdle_x, pdle_y + 120+300, 50, 30)
equip_btn_rect7 = pygame.Rect(pdle_x+150, pdle_y + 120+300, 50, 30)
equip_btn_rect8 = pygame.Rect(pdle_x+300, pdle_y + 120+300, 50, 30)
equip_btn_rect9 = pygame.Rect(pdle_x+450, pdle_y + 120+300, 50, 30)
equip_btn_rect10 = pygame.Rect(pdle_x+600, pdle_y + 120+300, 50, 30)








def display_price():
    global coin_x,equip_btn_rect1
    for i in range(coin_x,screen_width-coin_x,150):
        screen.blit(coin_img,(i+150,pdle_y+90))
        screen.blit(coin_img,(i,pdle_y+90+300))
        screen.blit(price_txt,(i+20+150,pdle_y+82))
        screen.blit(price_txt2,(i+20,pdle_y+82+300))
        # screen.blit(equip_btn,(i+20,pdle_y+120))
        # screen.blit(equip_btn,(i+20,pdle_y+120+300))
        pygame.display.update()

        pygame.draw.rect(screen,WHITE,equip_btn_rect1,2)






def shop_func():
    global coins,pressed_ok
    with open("coincount.txt", "r") as c:
        coins = c.read()
    runing = True
    while runing:
        global game_start

        if game_start == -2:
            screen.blit(bg2, (0, 0))
            pos = pygame.mouse.get_pos()
            # screen.fill(GREY)

            screen.blit(paddle_btn1, (screen_width // 2 - 150, 100))
            screen.blit(balls_btn2, (screen_width // 2 - 150, 300))
            # pygame.draw.rect(screen,WHITE,paddle_btn1_rect,2)
            if paddle_btn1_rect.collidepoint(pos):
                screen.blit(paddle_btn2, (screen_width // 2 - 150, 100))
            elif balls_btn1_rect.collidepoint(pos):
                screen.blit(balls_btn1, (screen_width // 2 - 150, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                runing = False
            if event.type == pygame. MOUSEBUTTONDOWN:
                global player1_pdle,pdle_x
                pos = pygame.mouse.get_pos()
                if paddle_btn1_rect.collidepoint(pos) and game_start == -2:

                    if pygame.mouse.get_pressed(3)[0]:
                        game_start = -3 #shop>padles
                        if game_start == -3:

                            with open("coincount.txt", "r") as c:
                                coins = c.read()
                            screen.blit(bg2, (0, 0))
                            display_price()

                            pdle_x = 100
                            draw_paddles(pdle1,pdle6)
                            draw_paddles(pdle2,pdle7)
                            draw_paddles(pdle3,pdle8)
                            draw_paddles(pdle4,pdle9)
                            draw_paddles(pdle5,pdle10)



                            global equip1, equip2, equip3, equip4, equip5, equip6, equip7, equip8, equip9, equip10,\
                                bought1, bought2, bought3, bought4, bought5, bought6, bought7, bought8, bought9, bought10
                            buydata()
                            equipdata()


                            if equip1 == 0 and bought1==1 :
                                screen.blit(equip_btn1, (equip_btn_rect1.x, equip_btn_rect1.y))
                            else:
                                screen.blit(equipped_btn, (equip_btn_rect1.x, equip_btn_rect1.y))

                            equipdata()
                            if equip2 == 0 and bought2 == 1:
                                screen.blit(equip_btn2, (equip_btn_rect2.x, equip_btn_rect2.y))
                            elif equip2 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect2.x, equip_btn_rect2.y))

                            equipdata()
                            if equip3 == 0 and bought3 == 1:
                                screen.blit(equip_btn3, (equip_btn_rect3.x, equip_btn_rect3.y))
                            elif equip3 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect3.x, equip_btn_rect3.y))

                            equipdata()
                            if equip4 == 0 and bought4 == 1:
                                screen.blit(equip_btn4, (equip_btn_rect4.x, equip_btn_rect4.y))
                            elif equip4 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect4.x, equip_btn_rect4.y))

                            equipdata()
                            if equip5 == 0 and bought5 == 1:
                                screen.blit(equip_btn6, (equip_btn_rect5.x, equip_btn_rect5.y))
                            elif equip5 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect5.x, equip_btn_rect5.y))

                            equipdata()
                            if equip6 == 0 and bought6 == 1:
                                screen.blit(equip_btn6, (equip_btn_rect6.x, equip_btn_rect6.y))
                            elif equip6 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect6.x, equip_btn_rect6.y))

                            equipdata()
                            if equip7 == 0 and bought7 == 1:
                                screen.blit(equip_btn7, (equip_btn_rect7.x, equip_btn_rect7.y))
                            elif equip7 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect7.x, equip_btn_rect7.y))
                            equipdata()
                            if equip8 == 0 and bought8 == 1:
                                screen.blit(equip_btn8, (equip_btn_rect8.x, equip_btn_rect8.y))
                            elif equip8 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect8.x, equip_btn_rect8.y))
                            equipdata()
                            if equip9 == 0:
                                screen.blit(equip_btn9, (equip_btn_rect9.x, equip_btn_rect9.y))
                            elif equip9 == 1 and bought9 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect9.x, equip_btn_rect9.y))
                            equipdata()
                            if equip10 == 0 and bought10 == 1:
                                screen.blit(equip_btn10, (equip_btn_rect10.x, equip_btn_rect10.y))
                            elif equip10 == 1:
                                screen.blit(equipped_btn, (equip_btn_rect10.x, equip_btn_rect10.y))


                if equip_btn_rect1.collidepoint(pos) and game_start == -3:
                    if pygame.mouse.get_pressed(5)[0]:
                        write_equipdata("data/equipdata2", "0")
                        write_equipdata("data/equipdata3", "0")
                        write_equipdata("data/equipdata4", "0")
                        write_equipdata("data/equipdata5", "0")
                        write_equipdata("data/equipdata6", "0")
                        write_equipdata("data/equipdata7", "0")
                        write_equipdata("data/equipdata8", "0")
                        write_equipdata("data/equipdata9", "0")
                        write_equipdata("data/equipdata10", "0")
                        print("1")
                        write_equipdata("equipdata1")
                        add_paddles(pdle1)
                        screen.blit(equipped_btn, (equip_btn_rect1.x, equip_btn_rect1.y))
                        game_start = 0
                        runing = False
                elif equip_btn_rect2.collidepoint(pos) and game_start == -3:
                    if pygame.mouse.get_pressed(5)[0]:
                        if int(coins) >= price:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata3", "0")
                            write_equipdata("data/equipdata4", "0")
                            write_equipdata("data/equipdata5", "0")
                            write_equipdata("data/equipdata6", "0")
                            write_equipdata("data/equipdata7", "0")
                            write_equipdata("data/equipdata8", "0")
                            write_equipdata("data/equipdata9", "0")
                            write_equipdata("data/equipdata10", "0")
                            write_equipdata("data/equipdata2")
                            add_paddles(pdle2)
                            screen.blit(equipped_btn, (equip_btn_rect2.x, equip_btn_rect2.y))
                            update_coins(coins,50)
                            game_start = 0
                            runing = False

                        else:
                            popup()




                elif equip_btn_rect3.collidepoint(pos) and game_start == -3:
                    if pygame.mouse.get_pressed(5)[0]:
                        if int(coins) >= price:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata2", "0")
                            write_equipdata("data/equipdata4", "0")
                            write_equipdata("data/equipdata5", "0")
                            write_equipdata("data/equipdata6", "0")
                            write_equipdata("data/equipdata7", "0")
                            write_equipdata("data/equipdata8", "0")
                            write_equipdata("data/equipdata9", "0")
                            write_equipdata("data/equipdata10", "0")

                            print("1")
                            write_equipdata("data/equipdata3")
                            add_paddles(pdle3)
                            screen.blit(equipped_btn, (equip_btn_rect3.x, equip_btn_rect3.y))
                            update_coins(coins,50)
                            game_start = 0
                            runing = False

                        else:
                            popup()

                if equip_btn_rect4.collidepoint(pos) and game_start == -3:
                    if int(coins) >= price:
                        if pygame.mouse.get_pressed(5)[0]:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata2", "0")
                            write_equipdata("data/equipdata3", "0")
                            write_equipdata("data/equipdata5", "0")
                            write_equipdata("data/equipdata6", "0")
                            write_equipdata("data/equipdata7", "0")
                            write_equipdata("data/equipdata8", "0")
                            write_equipdata("data/equipdata9", "0")
                            write_equipdata("data/equipdata10", "0")
                            print("1")
                            write_equipdata("data/equipdata4")
                            add_paddles(pdle4)
                            screen.blit(equipped_btn, (equip_btn_rect4.x, equip_btn_rect4.y))
                            update_coins(coins,50)
                            game_start = 0
                            runing = False
                        else:
                            fading_text()
                if equip_btn_rect5.collidepoint(pos) and game_start == -3:
                    if int(coins) >= price:
                        if pygame.mouse.get_pressed(5)[0]:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata2", "0")
                            write_equipdata("data/equipdata3", "0")
                            write_equipdata("data/equipdata4", "0")
                            write_equipdata("data/equipdata6", "0")
                            write_equipdata("data/equipdata7", "0")
                            write_equipdata("data/equipdata8", "0")
                            write_equipdata("data/equipdata9", "0")
                            write_equipdata("data/equipdata10", "0")
                            print("1")
                            write_equipdata("data/equipdata5")
                            add_paddles(pdle5)
                            screen.blit(equipped_btn, (equip_btn_rect5.x, equip_btn_rect5.y))
                            update_coins(coins, 50)
                            game_start = 0
                            runing = False
                        else:
                            popup()
                if equip_btn_rect6.collidepoint(pos) and game_start == -3:
                    if pygame.mouse.get_pressed(5)[0]:
                        if int(coins) >= price+50:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata2", "0")
                            write_equipdata("data/equipdata3", "0")
                            write_equipdata("data/equipdata4", "0")
                            write_equipdata("data/equipdata5", "0")
                            write_equipdata("data/equipdata7", "0")
                            write_equipdata("data/equipdata8", "0")
                            write_equipdata("data/equipdata9", "0")
                            write_equipdata("data/equipdata10", "0")
                            print("1")
                            write_equipdata("data/equipdata6")
                            add_paddles(pdle6)
                            screen.blit(equipped_btn, (equip_btn_rect6.x, equip_btn_rect6.y))
                            game_start = 0
                            runing = False
                        else:
                            popup()
                if equip_btn_rect7.collidepoint(pos) and game_start == -3:
                    if int(coins) >= price + 50 :
                        if pygame.mouse.get_pressed(5)[0]:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata2", "0")
                            write_equipdata("data/equipdata3", "0")
                            write_equipdata("data/equipdata4", "0")
                            write_equipdata("data/equipdata5", "0")
                            write_equipdata("data/equipdata6", "0")
                            write_equipdata("data/equipdata8", "0")
                            write_equipdata("data/equipdata9", "0")
                            write_equipdata("data/equipdata10", "0")
                            print("1")
                            write_equipdata("data/equipdata7")
                            add_paddles(pdle7)
                            screen.blit(equipped_btn, (equip_btn_rect7.x, equip_btn_rect7.y))
                            update_coins(coins, 100)
                            game_start = 0
                            runing = False
                        else:
                            popup()
                if equip_btn_rect8.collidepoint(pos) and game_start == -3:
                    if int(coins) >= price + 50:
                        if pygame.mouse.get_pressed(5)[0]:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata2", "0")
                            write_equipdata("data/equipdata3", "0")
                            write_equipdata("data/equipdata4", "0")
                            write_equipdata("data/equipdata5", "0")
                            write_equipdata("data/equipdata6", "0")
                            write_equipdata("data/equipdata7", "0")
                            write_equipdata("data/equipdata9", "0")
                            write_equipdata("data/equipdata10", "0")
                            print("1")
                            write_equipdata("data/equipdata8")
                            add_paddles(pdle8)
                            screen.blit(equipped_btn, (equip_btn_rect8.x, equip_btn_rect8.y))
                            update_coins(coins, 100)
                            game_start = 0
                            runing = False
                        else:
                            popup()
                if equip_btn_rect9.collidepoint(pos) and game_start == -3:
                    if int(coins) >= price + 50 :
                        if pygame.mouse.get_pressed(5)[0]:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata2", "0")
                            write_equipdata("data/equipdata3", "0")
                            write_equipdata("data/equipdata4", "0")
                            write_equipdata("data/equipdata5", "0")
                            write_equipdata("data/equipdata6", "0")
                            write_equipdata("data/equipdata7", "0")
                            write_equipdata("data/equipdata8", "0")
                            write_equipdata("data/equipdata10", "0")
                            print("1")
                            write_equipdata("data/equipdata9")
                            add_paddles(pdle9)
                            screen.blit(equipped_btn, (equip_btn_rect9.x, equip_btn_rect9.y))
                            update_coins(coins, 100)
                            game_start = 0
                            runing = False
                        else:
                            popup()
                if equip_btn_rect10.collidepoint(pos) and game_start == -3:
                    if int(coins) >= price+ 50:
                        if pygame.mouse.get_pressed(5)[0]:
                            write_equipdata("data/equipdata1", "0")
                            write_equipdata("data/equipdata2", "0")
                            write_equipdata("data/equipdata3", "0")
                            write_equipdata("data/equipdata4", "0")
                            write_equipdata("data/equipdata5", "0")
                            write_equipdata("data/equipdata6", "0")
                            write_equipdata("data/equipdata7", "0")
                            write_equipdata("data/equipdata8", "0")
                            write_equipdata("data/equipdata9", "0")
                            print("1")
                            write_equipdata("data/equipdata10")
                            add_paddles(pdle10)
                            screen.blit(equipped_btn, (equip_btn_rect10.x, equip_btn_rect10.y))
                            update_coins(coins, 100)
                            game_start = 0
                            runing = False
                        else:
                            popup()

        # pygame.draw.rect(screen,WHITE,buy_btn_rect,2)
        pygame.display.update()
        Clock.tick(60)
    return coins



def draw():
    global player_1_score, player_2_score, game_start, start_img, start_rect, exit_rect, restart_rect,player1,player2
    all_sprites = pygame.sprite.Group()

    all_sprites.add(player1)
    all_sprites.add(player2)



    if game_start == 1 or game_start ==2:
        score_font = pygame.font.SysFont("comicsans ms", 50)
        winner_font = pygame.font.SysFont("Algerian", 60)
        # screen.fill(GREY)
        screen.blit(bg2,(0,0))
        all_sprites.draw(screen)
        all_balls.draw(screen)
        all_sprites.update()
        all_balls.update()

        score_img = pygame.font.Font.render(score_font, str(player_1_score), True, WHITE).convert_alpha()
        score_img2 = pygame.font.Font.render(score_font, str(player_2_score), True, WHITE).convert_alpha()
        winner_img = pygame.font.Font.render(winner_font, "player 1 wins", True, RED).convert_alpha()
        winner_img2 = pygame.font.Font.render(winner_font, "player 2 wins", True, RED).convert_alpha()

        screen.blit(score_img, (10, 50))
        screen.blit(score_img2, (screen_width - 40, 50))

        if player_1_score == 5:
            screen.blit(winner_img, (screen_width // 2 - 230, screen_height // 2))
            pygame.display.update()
        elif player_2_score == 5:
            screen.blit(winner_img2, (screen_width // 2 - 230, screen_height // 2))
            pygame.display.update()

        if player_1_score == 5 or player_2_score == 5:
            pygame.time.wait(1000)
            restart()
            player_1_score, player_2_score = 0, 0
            game_start = -1
        # pygame.draw.rect(screen,WHITE,ball.rect,2)
        pygame.display.update()



def main():
    global speed,run,game_start, player_1_score, player_2_score, player1_pdle, player1, player2, pdle
    # main loop
    with open("all_paddles.txt", "r") as pdle :
        pdle = pdle.read()
    player1_pdle = pdle
    player2_pdle = pdle2

    player1 = Paddle(25, 250, player1_pdle)

    player2 = Paddle(screen_width - 45, 250, player2_pdle)
    run = True
    speed = 8
    all_balls.update()
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = 0
                run = False

        score_inc()
        draw()

        pygame.display.update()
        Clock.tick(60)



