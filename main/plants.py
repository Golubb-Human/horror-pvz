import datetime

class plant:
    def __init__(self, color:tuple):
        self.color = color
        
class peeShoter(plant):
    def __init__(self, damage:int, color:tuple, shootLength:int, interval:datetime.timedelta, textureOfPlant, textureOfBullet):
        plant.__init__(self, color)
        self.damage = damage
        self.time1 = datetime.datetime.now()
        self.time2 = self.time1.replace(hour=0, minute=0, second=1.425, microsecond=0)
    
    def update(self, grid):
        self.time1 = datetime.datetime.now()
        if self.time1 > self.time2:
            self.shooting()
        """
        shooting
        """
p = peeShoter(1, (1, 2)).update()