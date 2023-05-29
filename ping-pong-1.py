from pygame import *
window = display.set_mode((700, 500))
display.set_caption('ping-pong')
background = transform.scale(image.load('galaxy.png'), (700, 500))
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
        
        
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 495:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        
        
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.x < 495:
            self.rect.y += self.speed
racket1 = Player('racket.png', 20, 200,30,100 , 15)   
racket2 = Player('racket.png', 650, 200,30,100 , 15)   
game = True
FPS = 60
ball = GameSprite('tenis_ball.png', 300, 200, 50, 50, 20)
while game:
    window.blit(background, (0,0))
    racket1.reset()
    racket2.reset()
    ball.reset()
    racket1.update_l()
    racket2.update_r()
    
    for e in event.get():
            if e.type == QUIT:
                game = False
    clock.tick(FPS)
    
    display.update()
