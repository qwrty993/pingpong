from random import *
from pygame import *
import time as t

st = t.time()
shop_st = t.time()

#class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed)
    def move_P2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >=0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.bottom <= win_height:
            self.rect.y += self.speed
        self.reset()
    def move_P1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >=0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.bottom <= win_height:
            self.rect.y += self.speed
        self.reset()
    
"""class Enemy(GameSprite):
    #движение врага
    def update(self):
            self.rect.y += self.speed
            self.rect.x += self.speed

            if self.rect.y <= 0:
                self.speed *= -1
            elif self.rect.bottom >= win_height:
                self"""

win_width = 1000
win_height = 750
win_backround = (100, 100, 255)
window = display.set_mode((win_width, win_height))
game = True

clock = time.Clock()
FPS = 60
#mode - dodelat

font.init()
win_text_color = (255, 0, 0)
win_font = font.Font(None, 80)
lose_P1 = win_font.render("P2 победил", True, win_text_color)
lose_P2 = win_font.render("P1 победил", True, win_text_color)

rocket_size = (30, 150)
rocket_P1 = Player("rocket.png",60, (win_height //2) - (rocket_size[1] //2), rocket_size[0], rocket_size[1], 7)
rocket_P2 = Player("rocket.png",win_width - 120, (win_height //2) - (rocket_size[1] //2), rocket_size[0], rocket_size[1], 7)
rocket_P1_collided = False
rocket_P2_collided = False

ball_speed_x = randint(-1, 1)
ball_speed_y = randint(-1, 1)
while ball_speed_x == 0 or ball_speed_y == 0:
    if ball_speed_x == 0:
        ball_speed_x = randint(-1, 1)
    else:
        ball_speed_y = randint(-1, 1)
ball_speed_x *= 3; ball_speed_y *= 3

ball_wight = 85
ball_height = 85
ball_x = (win_width //2) - (ball_wight//2)
ball_y = win_height // 2
Ball = GameSprite("ping-pong-ball.png", ball_x, ball_y, ball_wight, ball_height, 3)

while game:
    for e in event.get():
        if e.type == QUIT:
            exit()
    window.fill(win_backround)
    rocket_P1.move_P1()
    rocket_P2.move_P2()
    if Ball.rect.colliderect(rocket_P1.rect) and rocket_P1_collided == False:
        ball_speed_x +=1
        ball_speed_x *= -1
        rocket_P1_collided = True
        rocket_P2_collided = False
    elif Ball.rect.colliderect(rocket_P2.rect) and rocket_P2_collided == False:
        ball_speed_x += 1
        ball_speed_x *= -1
        rocket_P1_collided = False
        rocket_P2_collided = True
    if Ball.rect.y <=0:
        ball_speed_y += 1
        ball_speed_y *= -1
    elif Ball.rect.y >= win_height - ball_height:
        ball_speed_y += 1
        ball_speed_y *= -1
    
    Ball.rect.x += ball_speed_x
    Ball.rect.y += ball_speed_y
    Ball.reset()
    display.update()
    clock.tick(FPS)