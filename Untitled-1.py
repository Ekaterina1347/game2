from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    

back = (200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
window.fill(back)

speed_x =2
speed_y = 2

clock = time.Clock()
FPS = 60
run = True 
finish = False

sprite1 = Player('png-clipart-football-ball-sport-monochrome.png',200,200,65,40,40)
sprite2 = Player('racket.png',30,200,15,100,10)
sprite3 = Player('racket.png',520,200,15,100,10)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))



while run:
    for e in event.get():
        if e.type == QUIT:
           run = False

    if finish !=True:
        window.fill(back)

        sprite1.update()
        sprite2.update_l()
        sprite3.update_r()

        sprite1.rect.x += speed_x
        sprite1.rect.y += speed_y

        if sprite.collide_rect(sprite2, sprite1) or sprite.collide_rect(sprite3, sprite1):
            speed_x *=-1
            speed_y *= 1
            
        if sprite1.rect.x<0:
            finish=True
            window.blit(lose1, (200, 200))
            game_over = True

        if sprite1.rect.x > win_width:
           finish = True
           window.blit(lose2, (200, 200))
           game_over = True



        sprite1.reset()
        sprite2.reset()
        sprite3.reset()
    display.update()
    clock.tick(FPS)
