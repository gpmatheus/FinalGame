import pygame
import entity

class Orb(entity.Entity):
    
    def __init__(self, direction, game_map, area=None, dimension=(50, 50)):
        super().__init__(game_map, pygame.image.load('assets/images/orbe.png'), area, dimension)
        self.direction = direction
        self.speed = 3
    
    def walk(self):
        ar = self.area
        
        # left
        if self.direction == 3:
            if ar and ar.can_go_left(self):
                self.rect.y = ar.coordinate[1]
                self.rect.x -= self.speed
                if self.rect.centerx < ar.coordinate[0] and ar.x > 0:
                    self.set_area(self.game_map.get_area(ar.x - 1, ar.y))
            # else:
            #     self.kill()
        
        # right
        if self.direction == 1:
            if ar and ar.can_go_right(self):
                self.rect.y = ar.coordinate[1]
                self.rect.x += self.speed
                if self.rect.centerx > ar.coordinate[0] + ar.dimensions[0] and ar.x < 12:
                    self.set_area(self.game_map.get_area(ar.x + 1, ar.y))
            # else:
            #     self.kill()
        # top
        if self.direction == 0:
            if ar and ar.can_go_top(self):
                self.rect.x = ar.coordinate[0]
                self.rect.y -= self.speed
                if self.rect.centery < ar.coordinate[1] and ar.y > 0:
                    self.set_area(self.game_map.get_area(ar.x, ar.y - 1))
            # else:
            #     self.kill()
                    
        if self.direction == 2:
            if ar and ar.can_go_down(self):
                self.rect.x = ar.coordinate[0]
                self.rect.y += self.speed
                if self.rect.centery > ar.coordinate[1] + ar.dimensions[1] and ar.y < 11:
                    self.set_area(self.game_map.get_area(ar.x, ar.y + 1))
            # else:
            #     self.kill()
