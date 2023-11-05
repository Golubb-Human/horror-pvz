import datetime
from setting import *
import pygame

class plant:
    def __init__(self, color):
        self.color = color
        
class peeShoter(plant):
    def __init__(self, damage:int, color, shootLength:int, interval:datetime.timedelta, colorOfBullet:tuple, pos:list, speedOfBullet):
        self.bullets = []
        plant.__init__(self, color)
        self.damage         = damage
        self.time1          = datetime.datetime.now()
        self.interval       = interval
        self.time2          = self.time1 + self.interval
        self.shootLength    = shootLength
        self.colorOfBullet  = colorOfBullet
        self.pos            = pos
        self.speedOfBullet  = speedOfBullet
    
    def update(self, sc):
        self.time3 = datetime.datetime.now() - self.time1 
        self.time1 = datetime.datetime.now()
        for i in range(len(self.bullets)):
            if self.pos != [0, 0]:
                if (self.bullets[i][0] - marginLeftOfGrid) / widthOfGrid - (self.pos[0] - marginLeftOfGrid) / widthOfGrid >= self.shootLength:
                    del self.bullets[i]
                else:
                    self.bullets[i][0] += (self.time3 * self.speedOfBullet).total_seconds()
                    pygame.draw.circle(sc, self.colorOfBullet, self.bullets[i], 5)
            
        if self.time1 > self.time2:
            self.bullets.append((self.pos).copy())
            self.time2 = self.time1 + self.interval
        """
        shooting
        """