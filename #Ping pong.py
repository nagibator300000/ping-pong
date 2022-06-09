#Ping pong
from pygame import *
win_width=700
window = display.set_mode((700,500))
clock = time.Clock()
run = True
display.set_caption('ping pong')
background = transform.scale(image.load('field.jpg'),(700,550))
font.init()
score=0
font1 = font.Font(None,36)
def p1loose(score):
    lose = font1.render('P1 LOSE',False,(255,0,0)) 
    window.fill((255,255,255))
    window.blit(lose,(300,100))
    text_score = font1.render('Ударов ракетки: '+str(score),False,(0,0,0)) 
    window.blit(text_score,(250,250))
def p2loose(score):
    lose = font1.render('P2 LOSE',False,(255,0,0)) 
    window.fill((255,255,255))
    window.blit(lose,(300,100))
    text_score = font1.render('Ударов ракетки: '+str(score),False,(0,0,0))
    window.blit(text_score,(250,250))
class Player(sprite.Sprite):
    def __init__(self,player_image,player_x,player_speed,player_y,a,b):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(a,b))
        self.speed = player_speed
        self.rect =self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

        
class Ball(sprite.Sprite):
    def __init__(self,player_image,player_x,player_speed_y,player_speed_x,player_y,a,b):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(a,b))
        self.speed_y = player_speed_y
        self.speed_x = player_speed_x
        self.rect =self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        global score
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y <= 0:
            self.speed_y *=-1
        if self.rect.y >=450:
            self.speed_y*=-1
        if self.rect.x <=0:
            p1loose(score)
        if self.rect.x >=700:
            p2loose(score)
        if sprite.spritecollide(self,players,False):
            self.speed_x*=-1
            self.speed_y+=1 if self.speed_y>0 else -1
            self.speed_x+=1 if self.speed_x>0 else -1
            p1.speed +=1
            p2.speed +=1
            score+=1
p1=Player('rocket.png',20,5,250,50,100)
p2=Player('rocket.png',630,5,250,50,100)
players=sprite.Group()
players.add(p1)
players.add(p2)
b=Ball('ball.png',350,3,3,250,50,50)
while run:
    for e in event.get():
        if e.type == QUIT:
            run =False
    window.blit(background,(0,0))
    p1.reset()
    p2.reset()
    b.reset()
    b.update()
    keys=key.get_pressed()
    if keys[K_s]  and p1.rect.y < 395:
        p1.rect.y+=p1.speed
    if keys[K_w] and p1.rect.y > 5:
        p1.rect.y-=p1.speed
    if keys[K_DOWN]  and p2.rect.y < 395:
        p2.rect.y+=p2.speed
    if keys[K_UP] and p2.rect.y > 5:
        p2.rect.y-=p2.speed
    display.update()
    clock.tick(60)