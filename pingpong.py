from pygame import *
font.init()

font1 =  font.Font(None,50)

lose_l = font1.render('Player 2 Win!', True,(0,0,0))
lose_r = font1.render('Player 1 Win!', True,(0,0,0))

color1 = (60, 176, 155)
window = display.set_mode((700,500))
window.fill(color1)
display.set_caption('Ping-Pong')
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,image_l,x,y,speed,height,width):
        super().__init__()
        self.image = transform.scale(image.load(image_l),(width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Racket(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5 :
            self.rect.y -= self.speed
        if keys[K_s]and self.rect.y < 395:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5 :
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.rect.y < 395:
            self.rect.y += self.speed

left_r = Racket('racket.png',20,350,7,100,20)
right_r = Racket('racket.png',660,350,7,100,20)
ball = Racket('tenis_ball.png',325,200,0,50,50)   
speed_x = 5
speed_y = 5
finish = False




game = True
while game == True:
    if finish != True:
        window.fill(color1)
        left_r.update_l()
        right_r.update_r()
        left_r.reset()
        right_r.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <= 0 or ball.rect.y >= 450:
            speed_y*= -1
        ball.reset()
        if sprite.collide_rect(ball,left_r) or sprite.collide_rect(ball,right_r):
            speed_x*=-1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_l,(260,250))
        
        if ball.rect.x > 650:
            finish = True
            window.blit(lose_r,(260,250))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
