import pygame as pg
from src.config import *
import src.state as state
from src.levels.list import levels
from src.components.peoples.Player import Player
from src.components.obstacles.ForbiddenArea import ForbiddenArea

class Level:
    
    def __init__(self):
        self.__status = 'running'
        self.__screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.__background = pg.Surface((WIDTH, HEIGTH))
        self.__obstacles = pg.sprite.Group()

        self.__setup_level()
        self.__load_map()

        self.__player = Player('tony', [200, 300], 4, self.__obstacles)
    
    def __setup_level(self):
        self.__background.fill(pg.Color(255, 255, 255))
        self.__level = levels[state.LEVEL_RUNNING - 1]

    def __load_map(self):
        map = self.__level.map
        self.__map = pg.image.load(map.image_path).convert()
        for [size, location] in map.forbidden_area:
            forbidden_area = ForbiddenArea(size, location, map.forbidden_area_color)
            self.__obstacles.add(forbidden_area)
            
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
        self.__obstacles.draw(self.__screen)
        self.__player.render(self.__screen)