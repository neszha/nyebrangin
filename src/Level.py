import pygame as pg
from src.config import *
import src.state as state
from src.levels.list import levels
from src.components.Car import Car
from random import randrange, choice
from src.components.peoples.Player import Player
from src.components.obstacles.ForbiddenArea import ForbiddenArea

# class Data: pass
class Level:
    
    def __init__(self):
        self.__status = 'waiting'
        self.__screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.__background = pg.Surface((WIDTH, HEIGTH))
        self.__obstacles = pg.sprite.Group()
        self.__cars = pg.sprite.Group()

        self.__setup_level()
        self.__load_map()
        self.__load_obstacles()
        self.__load_cars(True)

        self.__player = Player('tony', [200, 300], 4, self.__obstacles, self.__cars)
    
    def __setup_level(self):
        self.__background.fill(pg.Color(255, 255, 255))
        self.__level = levels[state.LEVEL_RUNNING - 1]

    def __load_map(self):
        map = self.__level.map
        self.__map = pg.image.load(map.image_path).convert()
            
    def __load_obstacles(self):
        map = self.__level.map
        for [size, location] in map.forbidden_area:
            forbidden_area = ForbiddenArea(size, location, map.forbidden_area_color)
            self.__obstacles.add(forbidden_area)

    def __load_cars(self, begin=False):
        car = self.__level.car
        [min_car, max_car] = car.traffic_density
        if len(self.__cars) <= max_car - 1:
            path = choice(car.use)
            position = [-120, 0]
            direction = choice(list(car.direction))
            position[1] = randrange(car.direction[direction][0], car.direction[direction][1])
            speed = randrange(car.speed_range[0], car.speed_range[1]) / 4
            if direction == 'right': position[0] = randrange(WIDTH + 120, WIDTH + 1000)
            else: position[0] = randrange(-1000, -50)
            if begin: position[0] = randrange(-400, WIDTH + 120)
            self.__cars.add(Car(path, position, direction, speed))
        if len(self.__cars) < min_car: self.__load_cars()
    
    def __load_civilians(self):
        pass
    
    def start(self):
        self.__status = 'running'

    def pause(self):
        self.__status = 'pause'

    def render(self):
        self.__screen.blit(self.__background, (0, 0))
        self.__screen.blit(self.__map, (0, 0))
        if self.__status == 'running':
            self.__load_cars()
            self.__cars.update()
            self.__cars.draw(self.__screen)
            self.__obstacles.draw(self.__screen)
            self.__player.render(self.__screen)