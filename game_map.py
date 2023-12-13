import pygame

class Area():

    def __init__(self, closed_sides):
        # closed sides boolean tuple
        self.closed_sides = closed_sides

        self.TOP_INDEX = 0
        self.RIGHT_INDEX = 0
        self.DOWN_INDEX = 0
        self.LEFT_INDEX = 0
    
    def set_coordinate(self, coordinate):
        self.coordinate = coordinate
    
    def set_dimensions(self, dimensions):
        self.dimensions = dimensions
        self.tolerance = dimensions[0] // 4

    def can_go_top(entity):
        is_possible = self.closed_sides[self.TOP_INDEX]
        x, = entity.rect
        return (is_possible and self.horizontal_tolerance(x))
    
    def can_go_right(entity):
        is_possible = self.closed_sides[self.RIGHT_INDEX]
        x, y = entity.rect
        return (is_possible and self.vertical_tolerance(y))

    def can_go_down(entity):
        is_possible = self.closed_sides[self.DOWN_INDEX]
        x, entity.rect
        return (is_possible and self.horizontal_tolerance(x))
    
    def can_go_left():
        is_possible = self.closed_sides[self.LEFT_INDEX]
        x, y = entity.rect
        return (is_possible and self.vertical_tolerance(y))
    
    def horizontal_tolerance(x):
        return (x > self.coordinate[0] - self.tolerance and x < self.coordinate[0] + self.tolerance)
    
    def vertical_tolerance(y):
        return (y > self.coordinate[1] - self.tolerance and y < self.coordinate[1] + self.tolerance)

class Map():

    def __init__(self, screen):

        # set map image
        background = pygame.image.load('assets/images/background.png')
        self.background = pygame.transform.scale(background, pygame.display.get_surface().get_size())

        # build areas
        self.areas = self.generate_areas()
        width, height = pygame.display.get_surface().get_size()
        for line_index, line in enumerate(self.areas):
            for row_index, area in enumerate(line):
                area_width = (width // len(line))
                area_height = (height // len(self.areas))
                x = area_width * row_index
                y = area_height * line_index
                area.set_coordinate((x, y))
                area.set_dimensions((area_width, area_height))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

    def get_area(width, height):
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
        