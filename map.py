import pygame

class Area():

    def __init__(self, closed_sides):
        # closed sides boolean tuple
        self.closed_sides = closed_sides
        self.TOP_INDEX = 0
        self.RIGHT_INDEX = 0
        self.DOWN_INDEX = 0
        self.LEFT_INDEX = 0
    
    def can_go_top():
        self.closed_sides[self.TOP_INDEX]        
    
    def can_go_right():
        self.closed_sides[self.RIGHT_INDEX]

    def can_go_down():
        self.closed_sides[self.DOWN_INDEX]
    
    def can_go_left():
        self.closed_sides[self.LEFT_INDEX]

class Map():

    def __init__(self):
        self.areas = self.generate_areas()
    
    def generate_areas():
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
            Area((True False, True, False)),
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

        return 12, 11, [
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
        