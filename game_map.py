import pygame

class Area():

    def __init__(self, closed_sides):
        # closed sides boolean tuple
        self.closed_sides = closed_sides

        self.TOP_INDEX = 0
        self.RIGHT_INDEX = 1
        self.DOWN_INDEX = 2
        self.LEFT_INDEX = 3
    
    # def get_closed_sides(self):
    #     return self.closed_sides

    # def get_coordinate(self):
    #     return self.coordinate
    
    # def get_dimensions(self):
    #     return self.dimensions

    def set_index(self, x, y):
        self.x = x
        self.y = y

    def draw_walls(self, screen, line_color=(0, 0, 0)):
        if self.closed_sides[self.TOP_INDEX]:
            line_end = (self.coordinate[0] + self.dimensions[0] - 1, self.coordinate[1])
            pygame.draw.line(screen, line_color, (self.coordinate[0], self.coordinate[1]), line_end)
        if self.closed_sides[self.RIGHT_INDEX]:
            line_end = (self.coordinate[0] + self.dimensions[0] - 1, self.coordinate[1] + self.dimensions[1] - 1)
            pygame.draw.line(screen, line_color, (self.coordinate[0] + self.dimensions[0] - 1, self.coordinate[1]), line_end)
        if self.closed_sides[self.DOWN_INDEX]:
            line_end = (self.coordinate[0], self.coordinate[1] + self.dimensions[1] - 1)
            pygame.draw.line(screen, line_color, (self.coordinate[0] + self.dimensions[0] - 1, self.coordinate[1] + self.dimensions[1] - 1), line_end)
        if self.closed_sides[self.LEFT_INDEX]:
            line_end = (self.coordinate[0], self.coordinate[1])
            pygame.draw.line(screen, line_color, (self.coordinate[0], self.coordinate[1] + self.dimensions[1] - 1), line_end)

    def get_closed_sides(self):
        return self.closed_sides

    def set_coordinate(self, coordinate):
        self.coordinate = coordinate
    
    def set_dimensions(self, dimensions):
        self.dimensions = dimensions
        self.tolerance = dimensions[0] // 4
    
    def can_go_top(self, entity):
        is_possible = not self.closed_sides[self.TOP_INDEX]
        return ((is_possible or entity.rect.y > self.coordinate[1]) and self.horizontal_tolerance(entity.rect.x))
    
    def can_go_right(self, entity):
        is_possible = not self.closed_sides[self.RIGHT_INDEX]
        return ((is_possible or entity.rect.x + entity.rect.w - 1 < self.coordinate[0] + self.dimensions[0] - 1) and self.vertical_tolerance(entity.rect.y))
    
    def can_go_down(self, entity):
        is_possible = not self.closed_sides[self.DOWN_INDEX]
        return ((is_possible or entity.rect.y + entity.rect.h - 1 < self.coordinate[1] + self.dimensions[1] - 1) and self.horizontal_tolerance(entity.rect.x))
    
    def can_go_left(self, entity):
        is_possible = not self.closed_sides[self.LEFT_INDEX]
        return ((is_possible or entity.rect.x > self.coordinate[0]) and self.vertical_tolerance(entity.rect.y))
    
    def horizontal_tolerance(self, x):
        return (x > self.coordinate[0] - self.tolerance and x < self.coordinate[0] + self.tolerance)
    
    def vertical_tolerance(self, y):
        return (y > self.coordinate[1] - self.tolerance and y < self.coordinate[1] + self.tolerance)

class Map():

    def __init__(self, area_dim=(50, 50)):

        # set area dimension
        self.map_dim = (area_dim[0] * 12, area_dim[1] * 11)

        # build areas
        self.areas = self.generate_areas()

        for line_index, line in enumerate(self.areas):
            for column_index, area in enumerate(line):
                area.set_coordinate((area_dim[0] * column_index, area_dim[1] * line_index))
                area.set_dimensions(area_dim)
                area.set_index(column_index, line_index)
        
        # set map image
        background = pygame.image.load('assets/images/background.png')
        self.background = pygame.transform.scale(background, self.map_dim)

    def get_map_dim(self):
        return self.map_dim

    def draw(self, screen):
        # draw background
        # screen.blit(self.background, (0, 0))

        # draw walls
        for line in self.areas:
            for area in line:
                area.draw_walls(screen, line_color=(255, 255, 255))

    def get_area(self, width, height):
        return self.areas[height][width]

    def generate_areas(self):
        line_1 = [
            Area((True, False, False, True)),
            Area((True, False, True, False)),
            Area((True, False, False, False)),
            Area((True, True, False, False)),
            Area((True, True, False, True)),
            Area((True, False, False, True)),
            Area((True, True, True, False)),
            Area((True, False, False, True)),
            Area((True, True, False, False)),
            Area((True, False, False, True)),
            Area((True, False, False, False)),
            Area((True, True, True, False))
        ]

        line_2 = [
            Area((False, True, False, True)),
            Area((True, False, False, True)),
            Area((False, True, False, False)),
            Area((False, False, False, True)),
            Area((False, True, True, False)),
            Area((False, False, False, True)),
            Area((True, False, True, False)),
            Area((False, True, False, False)),
            Area((False, False, False, True)),
            Area((False, True, True, False)),
            Area((False, True, False, True)),
            Area((True, True, False, True))
        ]

        line_3 = [
            Area((False, True, False, True)),
            Area((False, True, False, True)),
            Area((False, True, False, True)),
            Area((False, False, False, True)),
            Area((True, False, True, False)),
            Area((False, False, True, False)),
            Area((True, True, False, False)),
            Area((False, False, True, True)),
            Area((False, False, True, False)),
            Area((True, False, False, False)),
            Area((False, False, False, False)),
            Area((False, True, True, False))
        ]

        line_4 = [
            Area((False, True, False, True)),
            Area((False, True, False, True)),
            Area((False, False, False, True)),
            Area((False, False, True, False)),
            Area((True, False, True, False)),
            Area((True, False, False, False)),
            Area((False, False, True, False)),
            Area((True, False, False, False)),
            Area((True, False, True, False)),
            Area((False, True, False, False)),
            Area((False, False, False, True)),
            Area((True, True, False, False))
        ]

        line_5 = [
            Area((False, True, False, True)),
            Area((False, False, False, True)),
            Area((False, False, True, False)),
            Area((True, False, False, False)),
            Area((True, False, False, False)),
            Area((False, False, True, False)),
            Area((True, False, True, False)),
            Area((False, False, False, False)),
            Area((True, False, False, False)),
            Area((False, True, True, False)),
            Area((False, True, False, True)),
            Area((False, True, False, True))
        ]

        line_6 = [
            Area((False, False, True, True)),
            Area((False, False, True, False)),
            Area((True, False, False, False)),
            Area((False, True, True, False)),
            Area((False, False, False, True)),
            Area((True, False, True, False)),
            Area((True, False, True, False)),
            Area((False, True, False, False)),
            Area((False, False, True, True)),
            Area((True, True, False, False)),
            Area((False, True, False, True)),
            Area((False, True, False, True))
        ]

        line_7 = [
            Area((True, False, False, True)),
            Area((True, False, True, False)),
            Area((False, False, True, False)),
            Area((True, True, False, False)),
            Area((False, True, False, True)),
            Area((True, False, True, True)),
            Area((True, True, True, False)),
            Area((False, False, False, True)),
            Area((True, False, False, False)),
            Area((False, False, False, False)),
            Area((False, False, True, False)),
            Area((False, True, False, False))
        ]

        line_8 = [
            Area((False, False, False, True)),
            Area((True, False, False, False)),
            Area((True, False, True, False)),
            Area((False, False, True, False)),
            Area((False, True, False, False)),
            Area((True, False, False, True)),
            Area((True, False, True, False)),
            Area((False, True, True, False)),
            Area((False, True, False, True)),
            Area((False, False, False, True)),
            Area((True, True, False, False)),
            Area((False, True, False, True))
        ]

        line_9 = [
            Area((False, True, True, True)),
            Area((False, False, False, True)),
            Area((True, False, True, False)),
            Area((True, False, False, False)),
            Area((False, False, True, False)),
            Area((False, False, True, False)),
            Area((True, False, False, False)),
            Area((True, False, False, False)),
            Area((False, True, False, False)),
            Area((False, True, False, True)),
            Area((False, False, True, True)),
            Area((False, True, False, False))
        ]

        line_10 = [
            Area((True, False, True, True)),
            Area((False, True, False, False)),
            Area((True, False, False, True)),
            Area((False, True, False, False)),
            Area((True, False, False, True)),
            Area((True, False, True, False)),
            Area((False, True, False, False)),
            Area((False, True, False, True)),
            Area((False, False, True, True)),
            Area((False, False, True, False)),
            Area((True, False, False, False)),
            Area((False, True, False, False))
        ]

        line_11 = [
            Area((True, False, True, True)),
            Area((False, False, True, False)),
            Area((False, True, True, False)),
            Area((False, False, True, True)),
            Area((False, True, True, False)),
            Area((True, False, True, True)),
            Area((False, True, True, False)),
            Area((False, False, True, True)),
            Area((True, False, True, False)),
            Area((True, False, True, False)),
            Area((False, True, True, False)),
            Area((False, True, True, True))
        ]

        return [
            line_1,
            line_2,
            line_3,
            line_4,
            line_5,
            line_6,
            line_7,
            line_8,
            line_9,
            line_10,
            line_11,
        ]
        