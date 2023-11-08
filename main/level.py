class level:
    def __init__(self, waves:dict):
        self.waves = waves
        """
        waves = {<name(big/small)>:str : [<coins>:int, duration]}
        """
    
    def update(self):
        for i in self.waves.keys():
            if i == "big":
                pass # отрисуй флажок
            
    