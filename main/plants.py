import datetime
from setting import *
import pygame
import random

class plant:
    def __init__(self, color, colorAlpha, pos, cost, health):
        self.color          = color
        self.colorAlpha     = colorAlpha
        self.pos            = pos
        self.cost           = cost
        self.health         = health
        self.life           = True
    
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead()
    
    def dead(self):
        self.life = False
        
class peeShoter(plant):
    def __init__(self, damage:int, color, shootLength:int, interval:datetime.timedelta, colorOfBullet:tuple, pos:list, speedOfBullet, colorAlpha, cost, health):
        self.bullets = []
        super().__init__(color, colorAlpha, pos, cost, health)
        
        self.damage         = damage
        self.time1          = datetime.datetime.now()
        self.interval       = interval
        self.time2          = self.time1 + self.interval
        self.shootLength    = shootLength
        self.colorOfBullet  = colorOfBullet
        self.speedOfBullet  = speedOfBullet
    
    def update(self, sc):
        self.time3 = datetime.datetime.now() - self.time1 
        self.time1 = datetime.datetime.now()
        for i in range(len(self.bullets)):
            if self.pos != [0, 0]:
                try:
                    if (self.bullets[i][0] - marginLeftOfGrid) / widthOfGrid - (self.pos[0] - marginLeftOfGrid) / widthOfGrid >= self.shootLength:
                        del self.bullets[i]
                    else:
                        self.bullets[i][0] += (self.time3 * self.speedOfBullet).total_seconds()
                        if self.bullets[i][0] < width and self.bullets[i][0] >= 0 and self.bullets[i][1] < height and self.bullets[i][1] >= 0:
                            pygame.draw.circle(sc, self.colorOfBullet, self.bullets[i], 7)
                except IndexError:
                    pass
            
        if self.time1 > self.time2:
            self.bullets.append((self.pos).copy())
            self.time2 = self.time1 + self.interval
        """
        shooting
        """
        
class sunFlower(plant):
    def __init__(self, color, interval:datetime.timedelta, interval2:datetime.timedelta, textureOfSun, pos:list, colorAlpha, cost, produces, health):
        super().__init__(color, colorAlpha, pos, cost, health)
        
        self.sun                = []
        self.time1              = datetime.datetime.now()
        self.interval           = interval
        self.interval2          = interval2
        self.time2              = self.time1 + (self.interval + datetime.timedelta(seconds=(random.random() * 2 - 1) * 5))
        self.textureOfSun       = textureOfSun
        self.time3              = self.time1 + (self.interval2 + datetime.timedelta(seconds=(random.random() * 2 - 1) * 2))
        self.produces           = produces
    
    def update(self, sc):
        self.time1 = datetime.datetime.now()
        if self.sun != []:
            sc.blit(pygame.transform.scale(self.textureOfSun, (widthOfSun, heightOfSun)), self.sun)
            if self.time1 > self.time3:
                self.sun = []
        
        if self.time1 > self.time2:
            self.sun = [self.pos[0] + (random.random() * 2 - 1) * (widthOfGrid/2) - widthOfGrid/2, self.pos[1] + (random.random()*7-2)*5 - marginTopOfGrid2]
            self.time2 = self.time1 + (self.interval + datetime.timedelta(seconds=(random.random() * 2 - 1) * 5))
            self.time3 = self.time1 + (self.interval2 + datetime.timedelta(seconds=(random.random() * 2 - 1) * 2))
        """
        giving some suns
        """