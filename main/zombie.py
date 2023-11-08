import datetime
from setting import *

class zombie:
    def __init__(self, health, damage, interval:datetime.timedelta, color, pos, speed):
        self.health     = health
        self.damage     = damage
        self.interval   = interval
        self.color      = color
        self.pos        = pos
        self.time1      = datetime.datetime.now()
        self.speed      = speed
    
    def update(self, grid, sc):
        j = (self.pos[0] - marginLeftOfGrid) / widthOfGrid
        i = (self.pos[1] - marginTopOfGrid) / (heightOfGrid+marginTopOfGrid2)
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
            if grid[int(i)][j] != 0:
                grid.hit(self.damage)
            else:
                self.pos[0] -= (self.time1 - datetime.datetime.now() * self.speed).total_seconds()
                pygame.draw.rect(sc, self.color, (self.pos[0] - widthOfZombie / 2, self.pos[1] - heightOfZombie / 2))
                self.time1 = datetime.datetime.now()

class defaultZombie(zombie):
    def __init__(self, health, damage, interval:datetime.timedelta, color, pos, speed):
        super().__init__(health, damage, interval, color, pos, speed)