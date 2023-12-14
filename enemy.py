import pygame
import entity
import random

class Enemy(entity.Entity):
    
    def __init__(self, game_map, area=None, dimension=(50, 50)):
        super().__init__(game_map, pygame.image.load('assets/images/morto-vivo.png'), area, dimension)
        self.direction = random.randint(0, 3)
        self.speed = 1
    
    def find_another_direction(self):
        sides = [self.area.closed_sides[0], self.area.closed_sides[1], self.area.closed_sides[2], self.area.closed_sides[3]]
        free_count = 0
        for side in sides:
            if not side:
                free_count += 1
        if free_count > 1:
            oposite = 0
            if self.direction == 0:
                oposite = 2
            elif self.direction == 2:
                oposite = 0
            elif self.direction == 1:
                oposite = 3
            elif self.direction == 3:
                oposite = 1 
            side_index = random.randint(0, len(sides) - 1)
            while sides[side_index] and side_index == oposite:
                side_index = random.randint(0, len(sides) - 1)
            return side_index
        else:
            side_index = random.randint(0, len(sides) - 1)
            while sides[side_index]:
                side_index = random.randint(0, len(sides) - 1)
            return side_index
    
    def walk(self):
        ar = self.area
        
        # left
        if self.direction == 3:
            if ar and ar.can_go_left(self):
                self.rect.y = ar.coordinate[1]
                self.rect.x -= self.speed
                self.direction = 3
                if self.rect.centerx < ar.coordinate[0] and ar.x > 0:
                    self.set_area(self.game_map.get_area(ar.x - 1, ar.y))
                if self.rect.x == ar.coordinate[0]:
                    self.direction = self.find_another_direction()
            else:
                self.direction = self.find_another_direction()
        if self.direction == 1:
            if ar and ar.can_go_right(self):
                self.rect.y = ar.coordinate[1]
                self.rect.x += self.speed
                self.direction = 1
                if self.rect.centerx > ar.coordinate[0] + ar.dimensions[0] and ar.x < 12:
                    self.set_area(self.game_map.get_area(ar.x + 1, ar.y))
                if self.rect.x == ar.coordinate[0]:
                    self.direction = self.find_another_direction()
            else:
                self.direction = self.find_another_direction()
        if self.direction == 0:
            if ar and ar.can_go_top(self):
                self.rect.x = ar.coordinate[0]
                self.rect.y -= self.speed
                self.direction = 0
                if self.rect.centery < ar.coordinate[1] and ar.y > 0:
                    self.set_area(self.game_map.get_area(ar.x, ar.y - 1))
                if self.rect.y == ar.coordinate[1]:
                    self.direction = self.find_another_direction()
            else:
                self.direction = self.find_another_direction()
        if self.direction == 2:
            if ar and ar.can_go_down(self):
                self.rect.x = ar.coordinate[0]
                self.rect.y += self.speed
                self.direction = 2
                if self.rect.centery > ar.coordinate[1] + ar.dimensions[1] and ar.y < 11:
                    self.set_area(self.game_map.get_area(ar.x, ar.y + 1))
                if self.rect.y == ar.coordinate[1]:
                    self.direction = self.find_another_direction()
            else:
                self.direction = self.find_another_direction()
                    


ticks_to_generate_enemy = random.randint(100, 200)

def should_generate():
    global ticks_to_generate_enemy
    ticks_to_generate_enemy -= 1
    if ticks_to_generate_enemy <= 0:
        ticks_to_generate_enemy = random.randint(300, 400)
        return True
    return False        