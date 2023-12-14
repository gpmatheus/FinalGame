import pygame
import weapon

class Staff(weapon.Weapon):
    
    def __init__(self, game_map, area=None, dimension=(50, 50)):
        super().__init__(game_map, pygame.image.load('assets/images/cajado.png'), area, dimension)
    
    def attack(self):
        print('attack')