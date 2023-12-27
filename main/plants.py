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
    def __init__(self, damage:int, color, shootLength:int, interval:datetime.timedelta, textureOfBullet:tuple, pos:list, speedOfBullet, colorAlpha, cost, health):
        self.bullets = []
        super().__init__(color, colorAlpha, pos, cost, health)
        
        self.damage          = damage
        self.tmpTime         = datetime.datetime.now()
        self.interval        = interval
        self.timePlusInterval= self.tmpTime + self.interval
        self.shootLength     = shootLength
        self.textureOfBullet = textureOfBullet
        self.speedOfBullet   = speedOfBullet
    
    def update(self, sc, zombies):
        self.timeUpdate()
        
        self.bulletsMove(sc, zombies)
        
        self.shooting(zombies)
                    
        """
        shooting
        """
    
    def timeUpdate(self):
        self.time3 = datetime.datetime.now() - self.tmpTime
        self.tmpTime = datetime.datetime.now()    
    
    def bulletsMove(self, sc, zombies):
        for i in range(len(self.bullets)):
            if self.pos != [0, 0]:
                try:
                    for j in range(len(zombies)):
                        if self.bullets[i][0] >= zombies[j].pos[0] and self.bullets[i][1] >= zombies[j].pos[1] and self.bullets[i][0] < zombies[j].pos[0] + widthOfZombie and self.bullets[i][1] < zombies[j].pos[1] - heightOfGrid + heightOfZombie:
                            zombies[i].hit(self.damage)
                            del self.bullets[i]
                    if (self.bullets[i][0] - marginLeftOfGrid) / widthOfGrid - (self.pos[0] - marginLeftOfGrid) / widthOfGrid >= self.shootLength:
                        del self.bullets[i]
                    else:
                        self.bullets[i][0] += (self.time3 * self.speedOfBullet).total_seconds()
                        if self.bullets[i][0] < width and self.bullets[i][0] >= 0 and self.bullets[i][1] < height and self.bullets[i][1] >= 0:
                            pygame.draw.circle(sc, self.textureOfBullet, self.bullets[i], 7)
                except IndexError:
                    pass
        
    def timeReset(self, tmpTime):
        self.tmpTime = datetime.datetime.now()
        self.timePlusInterval += datetime.datetime.now() - tmpTime
        self.time3 += datetime.datetime.now() - tmpTime
    
    def shooting(self, zombies):
        if self.pos != [0, 0]:
            for j in range(len(zombies)):
                for i in range(len(self.bullets)):
                    if self.bullets[i][0] >= zombies[j].pos[0] and self.bullets[i][1] >= zombies[j].pos[1] and self.bullets[i][0] < zombies[j].pos[0] + widthOfZombie and self.bullets[i][1] < zombies[j].pos[1] - heightOfGrid + heightOfZombie:
                        zombies[i].hit(self.damage)
                        del self.bullets[i]
                        break
                if self.firstTime > self.timePlusInterval:
                    if self.pos[1] >= zombies[j].pos[1] and self.pos[1] < zombies[j].pos[1] - heightOfGrid + heightOfZombie and zombies[j].pos[0] > self.pos[0]:
                        self.bullets.append((self.pos).copy())
                        self.timePlusInterval = self.firstTime + self.interval
        
class sunFlower(plant):
    def __init__(self, color, intervalSpawn:datetime.timedelta, intervalDead:datetime.timedelta, textureOfSun, pos:list, colorAlpha, cost, produces, health):
        super().__init__(color, colorAlpha, pos, cost, health)
        
        self.sun                = []
        self.intervalSpawn      = intervalSpawn
        self.intervalDead       = intervalDead
        self.timeSpawn          = datetime.datetime.now() + (self.intervalSpawn + datetime.timedelta(seconds=(random.random() * 2 - 1) * 5))
        self.timeDead           = datetime.datetime.now() + (self.intervalDead + datetime.timedelta(seconds=(random.random() * 2 - 1) * 2))
        self.textureOfSun       = textureOfSun
        self.produces           = produces
    
    def update(self, sc, zombies):
        self.timeUpdate()
        self.drawSun()
        
        """
        giving some suns
        """
    
    def timeUpdate(self):
        if datetime.datetime.now() > self.timeSpawn:
            self.sun = [self.pos[0] + (random.random() * 2 - 1) * (widthOfGrid/2) - widthOfGrid/2, self.pos[1] + (random.random()*7-2)*5 - marginTopOfGrid2]
            self.timeSpawn = datetime.datetime.now() + (self.intervalSpawn + datetime.timedelta(seconds=(random.random() * 2 - 1) * 5))
            self.timeDead = datetime.datetime.now() + (self.intervalDead + datetime.timedelta(seconds=(random.random() * 2 - 1) * 2))
        
    def drawSun(self):
        if self.sun != []:
            sc.blit(pygame.transform.scale(self.textureOfSun, (widthOfSun, heightOfSun)), self.sun)
            self.sunDelete()
            
    def sunDelete(self):
        if datetime.datetime.now() > self.timeDead:
            self.sun = []
    
    def timeReset(self, tmpTime):
        self.timeSpawn += datetime.datetime.now() - tmpTime
        self.timeDead += datetime.datetime.now() - tmpTime