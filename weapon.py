import pygame
import entity
import random

class Weapon(entity.Entity):
    
    def __init__(self, game_map, image, area=None, dimension=(50, 50)):
        super().__init__(game_map, image, area, dimension)
        self.ticks_to_disapear = 600
        self.ticks_to_disapear_in_player = 300
        self.direction = 0
    
    def count_tick(self):
        self.ticks_to_disapear -= 1
        if self.ticks_to_disapear <= 0:
            return False
        return True
    
    def player_count_tick(self):
        self.ticks_to_disapear_in_player -= 1
        if self.ticks_to_disapear_in_player <= 0:
            return False
        return True
    
    def set_holder(self, player):
        self.holder = player

ticks_to_generate = random.randint(100, 200)

def should_generate():
    global ticks_to_generate
    ticks_to_generate -= 1
    if ticks_to_generate <= 0:
        ticks_to_generate = random.randint(400, 700)
        return True
    return False