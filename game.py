import pygame
import game_map

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trabalho final de Lab Games")

# build scenario


# background = pygame.image.load('assets/images/background.png')
# background = pygame.transform.scale(background, (WIDTH, HEIGHT))

map = game_map.Map(screen)

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