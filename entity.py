import pygame

class Entity(pygame.sprite.Sprite):
    
    def __init__(self, game_map, image, area=None, dimension=(50, 50)):
        super().__init__()
        self.game_map = game_map
        self.image = pygame.transform.scale(image, dimension)
        self.rect = self.image.get_rect()
        self.area = area
        self.rect.x = area.coordinate[0]
        self.rect.y = area.coordinate[1]
    
    def set_area(self, area):
        self.area = area
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    