import src.Level as Level

class Level1(Level):
    
    def __init__(self, name, index_level, countdown, cars, obstacles, environments, poin, player):
        self.__name  = name
        self.__index_level = index_level
        self.__countdown = countdown
        self.cars = cars
        self.obstacles = obstacles
        self.environments = environments
        self.point = poin
        self._player = player

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