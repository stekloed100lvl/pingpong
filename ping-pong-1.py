from pygame import *
import sys
window = display.set_mode((900, 500))
display.set_caption('ping-pong')
background = transform.scale(image.load('Fon.jpg'), (900, 500))
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, widh, hidh,  speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (widh, hidh))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        
        
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s]  and self.rect.x < 495:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        
        
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed
racket1 = Player('racket.png', 30, 200,20,60 , 15)   
racket2 = Player('racket.png', 850, 200,20,60 , 15)   
game = True
FPS = 60
ball = GameSprite('tenis_ball.png', 300, 200, 40, 40, 60)
speed1 = 3
speed2 = 3
finish = False
font.init()
font1 = font.SysFont('arial', 50)
point1 = 0
point2 = 0
lose1 = font1.render( "PLAYER 1 LOSE", True, (180, 0, 0))
lose2 = font1.render( "PLAYER 2 LOSE", True, (0, 0, 180))
ping = font1.render("PIngPong", True, (180, 180, 180))
while game:
    
    
    for e in event.get():
            if e.type == QUIT:
                game = False
    
    if finish != True:
        window.blit(background, (0,0))
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x+=speed1
        ball.rect.y+= speed2
        
        if finish == False:
            window.blit(ping, (354, 10))
        if ball.rect.y >= 330 or ball.rect.y < 120:
            speed2 *= -1
        if ball.rect.x >= 880 or ball.rect.x < 0:
            speed1 *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed1 *= -1
        point1 = int(point1)
        point2 = int(point2) 
        if ball.rect.x < 0:
            point1 +=1

        if ball.rect.x > 880:
            point2+= 1
           
        if point1 >= 10:
            
            window.blit(lose1, (300, 55))
            finish == True
        elif point2>= 10:
            
            window.blit(lose2, (300, 55))
            finish == True
        point1 = str(point1)
        point2 = str(point2)
        right = font1.render(point1, True, (0, 0, 0))
        left= font1.render(point2, True, (0, 0, 0))
        window.blit(right, (20,20))
        window.blit(left, (850,20))
    clock.tick(FPS)
    display.update()
