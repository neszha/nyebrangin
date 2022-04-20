import src.Level as Level

class Level1(Level):
    
    def __init__(self):
        self.__name  = None
        self.__index_level = 1
        self.__countdown = 0
        self.cars = []
        self.obstacles = []
        self.environments = []
        self.point = 0
        self._player = None

    def __set_environments(self):
        pass

    def __load_cars(self):
        pass
    
    def __load_obstacles(self):
        pass
    
    def __load_npc(self):
        pass
    
    def __load_civilians(self):
        pass
    
    def start(self):
        pass