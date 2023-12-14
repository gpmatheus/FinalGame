import pygame
import weapon
import orb

class Staff(weapon.Weapon):
    
    def __init__(self, game_map, area=None, dimension=(50, 50)):
        super().__init__(game_map, pygame.image.load('assets/images/cajado.png'), area, dimension)
        self.o = None
    
    def attack(self, direction):
        self.o = orb.Orb(direction, self.game_map, self.area)
    
    def update(self, screen):
        if self.o:
            self.o.walk()
            self.o.draw(screen)