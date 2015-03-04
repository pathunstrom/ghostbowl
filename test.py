import ghosts
import pygame
from pygame.locals import QUIT
from random import randint


GRASS = (161, 199, 107)

pygame.init()

display = pygame.display.set_mode((500, 500))
play_field = display.get_rect()
clock = pygame.time.Clock()
running = True
spawn = 5
baddies = pygame.sprite.Group()
baddies.add(ghosts.Spirit(play_field.centerx,
                          play_field.centery))

while running:
    delta = clock.tick(60) / 1000.0
    spawn -= delta
    if spawn <= 0:
        baddies.add(ghosts.Spirit(randint(100, 400), randint(100, 400)))
        spawn = 5.0
    baddies.update(delta)
    for baddy in baddies.sprites():
        if not play_field.colliderect(baddy.rect):
            baddies.remove(baddy)
    display.fill(GRASS)
    baddies.draw(display)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False