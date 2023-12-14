import pygame
import weapon

class Dagger(weapon.Weapon):
    
    def __init__(self, game_map, image, area=None, dimension=(50, 50)):
        super().__init__(game_map, image, area, dimension)
    
    def attack(self):
        print('attack')