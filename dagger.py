import pygame
import weapon

class Dagger(weapon.Weapon):
    
    def __init__(self, game_map, area=None, dimension=(50, 50)):
        
        super().__init__(game_map, pygame.image.load('assets/images/adaga.png'), area, dimension)
    
    def attack(self):
        print('attack')
    
    def update(self, screen):
        pass