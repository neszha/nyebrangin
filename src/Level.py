import pygame as pg
from src.config import *
import src.state as state
from src.levels.list import levels

class Data: pass
class Level:
    
    def __init__(self):
        self.__status = 'running'
        self.__screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.__background = pg.Surface((WIDTH, HEIGTH))

        self.__setup_level()
        self.__load_map()
    
    def __setup_level(self):
        self.__background.fill(pg.Color(255, 255, 255))
        self.player = None
        self.__level = levels[state.LEVEL_RUNNING-1]

    def __load_map(self):
        map = self.__level.map
        self.__map = pg.image.load(map.image_path).convert()
        self.__forbidden_area = []
        for forbidden in map.forbidden_area:
            area = Data()
            area.surface = pg.Surface(forbidden[0]).convert_alpha()
            area.location = forbidden[1]
            if map.forbidden_area_color:
                area.surface.fill(pg.Color(map.forbidden_area_color))
            self.__forbidden_area.append(area)
            
    def __load_obstacles(self):
        pass
    
    def __load_cars(self):
        pass
    
    def __load_civilians(self):
        pass
    
    def start(self):
        pass

    def pause(self):
        pass

    def render(self):
        self.__screen.blit(self.__background, (0, 0))
        self.__screen.blit(self.__map, (0, 0))
        for forbidden in self.__forbidden_area:
            self.__screen.blit(forbidden.surface, forbidden.location)