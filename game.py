import pygame
import game_map
import player

pygame.init()

map = game_map.Map()
SCREEN_DIMENSION = map.get_map_dim()
screen = pygame.display.set_mode(SCREEN_DIMENSION)
pygame.display.set_caption("Trabalho final de Lab Games")

player = player.Player(map, map.get_area(0, 0))

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

    # update screen
    pygame.display.flip()

pygame.quit()