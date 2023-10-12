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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -20)
        bullets.add(bullet)

back = (200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
window.fill(back)

clock = time.Clock()
FPS = 60
run = True 

finish = False

sprite1 = Player('png-clipart-football-ball-sport-monochrome.png',200,200,65,40,40)
sprite2 = Player('racket.png',30,200,15,100,150)
sprite3 = Player('racket.png',520,200,15,100,150)


while run:
    for e in event.get():
        if e.type == QUIT:
           run = False

    if finish !=True:
        window.fill(back)

        sprite1.update()
        sprite1.reset()

        sprite2.update()
        sprite2.reset()

        sprite3.update()
        sprite3.reset()
    
    display.update()
    clock.tick(FPS)
