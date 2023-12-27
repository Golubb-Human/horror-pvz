import setting
import datetime
import random

class zombie:
    def __init__(self, health, damage, interval:datetime.timedelta, color, pos, speed):
        self.health     = health
        self.damage     = damage
        self.interval   = interval
        self.color      = color
        self.pos        = pos
        self.time1      = datetime.datetime.now()
        self.speed      = speed
        self.speed     += speed * (random.random() * 2 - 1) / 5
        self.go         = True
        self.life       = True
    
    def update(self, grid):
        self.go = True
        j = (self.pos[0] - setting.marginLeftOfGrid) / setting.widthOfGrid
        i = (self.pos[1] - setting.marginTopOfGrid) / (setting.heightOfGrid+setting.marginTopOfGrid2)
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
            if grid[int(i)][int(j)] != 0:
                grid[int(i)][int(j)].hit(self.damage)
                self.go = False
                self.time1 = datetime.datetime.now()
        if self.go:
            self.time1 
            self.pos[0] -= ((datetime.datetime.now() - self.time1)).total_seconds() * self.speed
            # pygame.draw.rect(sc, self.color, (self.pos[0] - setting.widthOfZombie / 2, self.pos[1] - setting.heightOfZombie / 2))
            self.time1 = datetime.datetime.now()
    
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead()
    
    def dead(self):
        self.life = False
    
    def timeReset(self, tmpTime):
        self.time1 = datetime.datetime.now()
        self.time2 += datetime.datetime.now() - tmpTime
        self.time3 += datetime.datetime.now() - tmpTime
        

class defaultZombie(zombie):
    def __init__(self, health, damage, interval:datetime.timedelta, color, pos, speed):
        super().__init__(health, damage, interval, color, pos, speed)