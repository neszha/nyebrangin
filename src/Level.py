from abc import ABC, abstractmethod

class Level(ABC):
    
    @abstractmethod
    def __set_environments(self):
        pass

    @abstractmethod
    def __load_cars(self):
        pass
    
    @abstractmethod
    def __load_obstacles(self):
        pass
    
    @abstractmethod
    def __load_npc(self):
        pass
    
    @abstractmethod
    def __load_civilians(self):
        pass
    
    @abstractmethod
    def start(self):
        pass