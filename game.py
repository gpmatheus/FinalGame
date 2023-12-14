import pygame
import game_map
import player
import dagger
import weapon
import random
import staff
import enemy

pygame.init()

map = game_map.Map()
SCREEN_DIMENSION = map.get_map_dim()
screen = pygame.display.set_mode(SCREEN_DIMENSION)
pygame.display.set_caption("Trabalho final de Lab Games")

player1 = player.Player(map, pygame.image.load('assets/images/personagem-jogavel.png'), map.get_area(0, 6))
player2 = player.Player(map, pygame.image.load('assets/images/personagem-jogavel-2.png'), map.get_area(11, 6), keys=(pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE))

weapons = pygame.sprite.Group()
def generate_weapon():
    i = random.randint(0, 1)
    x = random.randint(0, 11)
    y = random.randint(0, 10)
    if i == 0:
        weapons.add(staff.Staff(map, map.get_area(x, y)))
    if i == 1:
        weapons.add(dagger.Dagger(map, map.get_area(x, y)))


enemies = pygame.sprite.Group()
def spawn_enemy():
    x = random.randint(0, 11)
    y = random.randint(0, 10)
    enemies.add(enemy.Enemy(map, map.get_area(x, y)))

clock = pygame.time.Clock()
running = True
while running:

    # limits the clock
    clock.tick(60)

    # check if player quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player1.check_pressed_keys(pygame.key.get_pressed())
    player2.check_pressed_keys(pygame.key.get_pressed())
    
    # clear screen
    screen.fill((0, 0, 0))

    # draw map
    map.draw(screen)
    
    # draw player
    player1.draw(screen)
    player2.draw(screen)
    
    # add weapon
    if weapon.should_generate():
        generate_weapon()
    
    # draw or delete weapon
    for wp in weapons.sprites():
        if wp.count_tick():
            wp.draw(screen)
        else:
            wp.kill()
    
    # add enemy
    if enemy.should_generate():
        spawn_enemy()
    
    # draw enemies
    for en in enemies.sprites():
        en.draw(screen)
    
    # check player 1 weapon colisions
    p1_weapon_colisions = pygame.sprite.spritecollide(player1, weapons, True)
    if p1_weapon_colisions:
        player1.take_weapon(p1_weapon_colisions[0])

    # check player 2 weapon colision
    p2_weapon_colisions = pygame.sprite.spritecollide(player2, weapons, True)
    if p2_weapon_colisions:
        player2.take_weapon(p2_weapon_colisions[0])
    
    # check player 1 enemy colision
    p1_enemy_colision = pygame.sprite.spritecollide(player1, enemies, False)
    if p1_enemy_colision:
        if player1.weapon:
            p1_enemy_colision[0].kill()
        else:
            print("player 2 ganhou")
            break
    
    # check player 2 enemy colision
    p2_enemy_colision = pygame.sprite.spritecollide(player2, enemies, False)
    if p2_enemy_colision:
        if player2.weapon:
            p2_enemy_colision[0].kill()
        else:
            print("player 1 ganhou")
            break
        
    # check players colition
    group = pygame.sprite.Group()
    group.add(player2)
    players_colision = pygame.sprite.spritecollide(player1, group, False)
    if players_colision and player1.weapon and players_colision[0].weapon:
        print("empate")
        break
    if players_colision and players_colision[0].weapon:
        print("player 2 ganhou")
        break
    if players_colision and player1.weapon:
        print("player 1 ganhou")
        break

    # update enamies
    for en in enemies:
        en.walk()
        en.draw(screen)

    # update screen
    pygame.display.flip()

pygame.quit()