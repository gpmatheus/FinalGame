import pygame
import game_map

pygame.init()

map = game_map.Map()
SCREEN_DIMENSION = map.get_map_dim()
screen = pygame.display.set_mode(SCREEN_DIMENSION)
pygame.display.set_caption("Trabalho final de Lab Games")

clock = pygame.time.Clock()
running = True
while running:

    # limits the clock
    clock.tick(60)

    # check if player quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # clear screen
    # screen.fill((80, 80, 80))

    # draw map
    map.draw(screen)

    # update screen
    pygame.display.flip()

pygame.quit()