import datetime
import zombie
from setting import *
import random

class level:
    def __init__(self, waves:dict):
        self.waves = waves
        self.wave  = 0
        self.coins = self.waves[self.wave][0]
        self.timeStartWave = datetime.datetime.now()
        self.timeEndWave = datetime.datetime.now() + self.waves[self.wave][1]
        self.end   = False
        
        self.zombies = []
        
        """
        waves = {<index>:int : [<coins>:int, <duration>, <name(big/small)>]}
        """
    
    def update(self, zombieCosts):
        ret = []
        self.timeStartWave = datetime.datetime.now()
        if self.timeStartWave > self.timeEndWave:
            while True:
                if self.coins <= 0:
                    if self.wave + 1 == len(self.waves):
                        self.end = True
                    else:
                        self.wave += 1
                        self.timeEndWave = datetime.datetime.now() + self.waves[self.wave][1]
                    self.coins = self.waves[self.wave][0]
                    break
                randomZombieCost = random.choice(zombieCosts)
                if self.coins >= randomZombieCost[1]:
                    ret.append(randomZombieCost[0])
                    self.coins -= randomZombieCost[1]
            
        for i in self.waves.keys():
            if self.waves[i][2] == "big":
                pass # отрисуй флажок
            
        if ret != 0:
            return ret
    