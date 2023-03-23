import pygame 
from random import randrange
size = 400
radius,step = 25,20
x, y = randrange(0, size, radius), randrange(0, size, radius)

pygame.init()
screen = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=step
    if pressed[pygame.K_DOWN]: y+=step
    if pressed[pygame.K_LEFT]: x-=step
    if pressed[pygame.K_RIGHT]: x+=step

    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen, pygame.Color('red'), (x,y), radius)

    if x < 15 : x+=step
    elif x > size - 10: x -= step
    elif y < 15: y += step
    elif y > size - 10: y -= step

    pygame.display.flip()
    clock.tick(60)