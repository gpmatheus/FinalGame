import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game_map, area=None, dimension=(50, 50), keys=(pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)):
        super().__init__()
        self.game_map = game_map
        self.LEFT_INDEX = 0
        self.UP_INDEX = 1
        self.DOWN_INDEX = 2
        self.RIGHT_INDEX = 3
        self.image = pygame.Surface(dimension)
        self.image.fill((0, 0, 200))
        self.rect = self.image.get_rect()
        self.speed = 2
        self.area = area
        self.set_keys(keys)

    def set_keys(self, keys):
        self.keys = keys
    
    def set_area(self, area):
        self.area = area
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def check_pressed_keys(self, pressed_keys):
    
        ar = self.area
        if pressed_keys[self.keys[self.LEFT_INDEX]]:
            if ar and ar.can_go_left(self):
                self.rect.y = ar.coordinate[1]
                self.rect.x -= self.speed
                if self.rect.centerx < ar.coordinate[0] and ar.x > 0:
                    self.set_area(self.game_map.get_area(ar.x - 1, ar.y))
        if pressed_keys[self.keys[self.RIGHT_INDEX]]:
            if ar and ar.can_go_right(self):
                self.rect.y = ar.coordinate[1]
                self.rect.x += self.speed
                if self.rect.centerx > ar.coordinate[0] + ar.dimensions[0] and ar.x < 12:
                    self.set_area(self.game_map.get_area(ar.x + 1, ar.y))
        if pressed_keys[self.keys[self.UP_INDEX]]:
            if ar and ar.can_go_top(self):
                self.rect.x = ar.coordinate[0]
                self.rect.y -= self.speed
                if self.rect.centery < ar.coordinate[1] and ar.y > 0:
                    self.set_area(self.game_map.get_area(ar.x, ar.y - 1))
        if pressed_keys[self.keys[self.DOWN_INDEX]]:
            if ar and ar.can_go_down(self):
                self.rect.x = ar.coordinate[0]
                self.rect.y += self.speed
                if self.rect.centery > ar.coordinate[1] + ar.dimensions[1] and ar.y < 11:
                    self.set_area(self.game_map.get_area(ar.x, ar.y + 1))

