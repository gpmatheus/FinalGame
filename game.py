import pygame
import game_map
import player
import dagger
import weapon
import random

pygame.init()

map = game_map.Map()
SCREEN_DIMENSION = map.get_map_dim()
screen = pygame.display.set_mode(SCREEN_DIMENSION)
pygame.display.set_caption("Trabalho final de Lab Games")

player = player.Player(map, pygame.image.load('assets/images/personagem-jogavel.png'), map.get_area(0, 0))

weapons = pygame.sprite.Group()

def generate_weapon():
    i = random.randint(0, 3)
    if i == 0:
        x = random.randint(0, 11)
        y = random.randint(0, 10)
        weapons.add(dagger.Dagger(map, pygame.image.load('assets/images/adaga.png'), map.get_area(x, y)))

clock = pygame.time.Clock()
running = True
while running:

    # limits the clock
    clock.tick(60)

    # check if player quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.check_pressed_keys(pygame.key.get_pressed())
    
    # clear screen
    screen.fill((0, 0, 0))

    # draw map
    map.draw(screen)
    
    # draw player
    player.draw(screen)
    
    # add weapon
    if weapon.should_generate():
        generate_weapon()
    
    for wp in weapons.sprites():
        if wp.count_tick():
            wp.draw(screen)
        else:
            wp.kill()

    # update screen
    pygame.display.flip()

pygame.quit()