from pygame import *


back = (200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
window.fill(back)

clock = time.Clock()
FPS = 60
run = True 

while run:
    for e in event.get():
        if e.type == QUIT:
           run = False

    display.update()
    clock.tick(FPS)