import datetime
from setting import *
import pygame
import random

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
        self.cost  = costOfPeaShooter
    
    def update(self, sc):
        self.time3 = datetime.datetime.now() - self.time1 
        self.time1 = datetime.datetime.now()
        for i in range(len(self.bullets)):
            if self.pos != [0, 0]:
                if (self.bullets[i][0] - marginLeftOfGrid) / widthOfGrid - (self.pos[0] - marginLeftOfGrid) / widthOfGrid >= self.shootLength:
                    del self.bullets[i]
                else:
                    self.bullets[i][0] += (self.time3 * self.speedOfBullet).total_seconds()
                    pygame.draw.circle(sc, self.colorOfBullet, self.bullets[i], 7)
            
        if self.time1 > self.time2:
            self.bullets.append((self.pos).copy())
            self.time2 = self.time1 + self.interval
        """
        shooting
        """
        
class sunFlower(plant):
    def __init__(self, color, interval:datetime.timedelta, interval2:datetime.timedelta, textureOfSun, pos:list):
        plant.__init__(self, color)
        
        self.sun                = []
        self.time1              = datetime.datetime.now()
        self.interval           = interval
        self.interval2          = interval2
        self.time2              = self.time1 + self.interval
        self.textureOfSun       = textureOfSun
        self.pos                = pos
    
    def update(self, sc):
        self.time1 = datetime.datetime.now()
        if self.sun != []:
            sc.blit(pygame.transform.scale(self.textureOfSun, (widthOfSun, heightOfSun)), i)
            if self.time1 > self.time3:
                self.sun = []
        
        if self.time1 > self.time2:
            self.sun = [self.pos[0] + (random.random() * 2 - 1) * (widthOfGrid/2) - widthOfGrid/2, self.pos[1] + (random.random()*7-2)*5 - marginTopOfGrid2]
            self.time2 = self.time1 + (self.interval + datetime.timedelta(seconds=(random.random() * 2 - 1) * 5))
            self.time3 = self.time1 + (self.interval2 + datetime.timedelta(seconds=(random.random() * 2 - 1) * 2))
            print(1)
        """
        giving some suns
        """