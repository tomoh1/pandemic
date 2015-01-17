ACTIVE = 0
CURED = 1
ERADICATED = 2

NUM_CUBES = 24

class Disease(object):
    def __init__(self, color):
        self.color = color
        self.status = ACTIVE
        self.cubes_available = NUM_CUBES

    def cure(self):
        if self.status == ACTIVE:
            self.status = CURED
        else:
            raise RuntimeError('%s disease is already cured' %
                               self.color)

    def deployCubes(self, num):
        self.cubes_available -= num
        return self.cubes_available >= 0

    def returnCubes(self, num):
        self.cubes_available += num
        if self.status == CURED:
            if self.cubes_available == NUM_CUBES:
                self.status = ERADICATED

BLUE_COLOR = 'blue'
RED_COLOR = 'red'
YELLOW_COLOR = 'yellow'
BLACK_COLOR = 'black'

BLUE = Disease(BLUE)
RED = Disease(RED)
YELLOW = Disease(YELLOW_COLOR)
BLACK = Disease(BLACK_COLOR)


COLORMAP = {BLUE_COLOR: BLUE,
            RED_COLOR: RED,
            YELLOW_COLOR: YELLOW,
            BLACK_COLOR: BLACK}

