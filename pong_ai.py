import pygame
from pygame.locals import *
import random
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

#fps
Clock = pygame.time.Clock()
#game variabl3es
player_2_score = 0 #right side
player_1_score = 0 #left side
game_start = 0

#music
pygame.mixer.music.load("8_bit_ice_cave_lofi.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1,0.0,3000)
pop = pygame.mixer.Sound("Pop.ogg")
pop.set_volume(0.6)




class Balls(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ball_width = 21
        ball_height = 21
        ball_img = pygame.image.load("red_Balloon.png").convert_alpha()
        ball_img2 = pygame.transform.scale(ball_img,(ball_width,ball_height))
        self.image = ball_img2
        self.image.set_colorkey(BLACK)
        self.rect = pygame.Rect(screen_width//2, screen_height//2,ball_width,ball_height)


        self.velocity = [random.randint(4,6), random.randint(-8,8)]

    def update(self):
        if game_start == 1 or game_start ==2:
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





class Paddle(pygame.sprite.Sprite):

    def __init__(self,x,y,image_name):
        super().__init__()
        paddle_img = pygame.image.load(image_name)
        self.image = pygame.transform.scale(paddle_img,(15,100)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        global speed
        dy = 0
        comp_speed = [2,4] #handicap 1
        # player1_controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.rect.y > 0:
            dy -= speed
        if keys[pygame.K_s] and player1.rect.y + player1.image.get_height() < screen_height:
            dy += speed
        dy2 = 0
        if ball.rect.centery < player2.rect.centery and player2.rect.y > 0: #ball is above the paddle and moving the paddle  up
            if ball.rect.x > screen_width//2 + 50: #handicap
                # 2
                dy2 -= random.choice(comp_speed)
        if ball.rect.centery > player2.rect.centery and player2.rect.bottom < screen_height: #ball is below the paddle
            if ball.rect.x > screen_width // 2 + 50:
                dy2 += random.choice(comp_speed)



        #update player coordinats
        player1.rect.y += dy
        player2.rect.y += dy2






#making objects/sprites

player1 = Paddle(25,250,'paddle.png')
player2 = Paddle(screen_width-45,250,'glasspaddle2.png')

#makingball
ball = Balls()
ball.rect.x = screen_width//2
ball.rect.y = screen_height//2

all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

all_balls = pygame.sprite.Group()
all_balls.add(ball)



def restart():
    pygame.time.wait(1000)
    ball.rect.x = screen_width // 2
    ball.rect.y = screen_height // 2
    player1.rect.x , player1.rect.y = 25,250
    player2.rect.x, player2.rect.y = screen_width-45,250
    ball.velocity = [random.randint(4, 6), random.randint(-8, 8)]

    # pygame.time.wait(2000)







def score_inc():
    global player_1_score, player_2_score
    if game_start == 1 or game_start == 2:
        if ball.rect.left < player1.rect.right - 7:
            if player_2_score < 5:
                player_2_score += 1
                restart()
        elif ball.rect.right - 8 > player2.rect.left:
            if player_1_score < 5:
                player_1_score += 1
                restart()





def draw():
    global player_1_score, player_2_score, game_start, start_img, start_rect, exit_rect, restart_rect



    if game_start == 1 or game_start == 2:
        score_font = pygame.font.SysFont("comicsans ms", 50)
        winner_font = pygame.font.SysFont("Algerian", 60)
        screen.fill(GREY)
        all_sprites.draw(screen)
        all_balls.draw(screen)
        all_sprites.update()
        all_balls.update()

        score_img = pygame.font.Font.render(score_font, str(player_1_score), True, WHITE).convert_alpha()
        score_img2 = pygame.font.Font.render(score_font, str(player_2_score), True, WHITE).convert_alpha()
        winner_img = pygame.font.Font.render(winner_font, "player 1 wins", True, RED).convert_alpha()
        winner_img2 = pygame.font.Font.render(winner_font, "CPU WINS", True, RED).convert_alpha()

        screen.blit(score_img, (10, 50))
        screen.blit(score_img2, (screen_width - 40, 50))
        pygame.draw.rect(screen,WHITE,player1.rect,2)
        pygame.draw.rect(screen,WHITE,player2.rect,2)

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

    elif game_start == -1:
        screen.fill(GREY)
        restart_img = pygame.transform.scale(pygame.image.load("restart_btn.png"), (150,45))
        restart_rect = pygame.Rect(300,300, 150,45)
        # pygame.draw.rect(screen,WHITE,restart_rect,2)
        screen.blit(restart_img,(300,300))


def main():
    global speed,run,game_start, player_1_score, player_2_score, speed
    # main loop
    run = True
    speed = 6
    all_balls.update()
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN: #checking for mouse click
                pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(pos) and game_start == 0:
                    if pygame.mouse.get_pressed(3)[0] == 1:
                        game_start = 1
                elif exit_rect.collidepoint(pos) and game_start == 0:
                    if pygame.mouse.get_pressed(5)[0] == 1:
                        run = False
                elif restart_rect.collidepoint(pos) and game_start == -1:
                    if pygame.mouse.get_pressed(3)[0] == 1:
                        player_1_score = 0
                        player_2_score = 0
                        game_start = 1
                        restart()


        score_inc()
        draw()

        pygame.display.update()
        Clock.tick(80)
    pygame.quit()

if __name__ == '__main__':
    main()