class Level:
    
    def __init__(self, index_level):
        self.__index_level = index_level
        self.__status = 'running'
        self.player = None

    def __load_map(self):
        pass

    def __load_cars(self):
        pass
    
    def __load_obstacles(self):
        pass
    
    def __load_civilians(self):
        pass
    
    def start(self):
        pass

    def pause(self):
        pass

    def render(self):
        pass