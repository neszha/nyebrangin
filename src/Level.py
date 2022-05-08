import pygame as pg
import src.state as state
from src.config import *
from src.levels.list import levels
from src.components.Car import Car
from random import randrange, choice
from src.components.peoples.Player import Player
from src.components.GameHeader import GameHeader
from src.components.popups.WaitingPlay import WaitingPlay
from src.components.obstacles.ForbiddenArea import ForbiddenArea

# class Data: pass
class Level:
    
    def __init__(self):
        self.__status = 'waiting'
        self.__screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.__background = pg.Surface((WIDTH, HEIGTH))
        self.__waiting_play = WaitingPlay(start_command=self.__start)
        self.__header = GameHeader()
        self.__obstacles = pg.sprite.Group()
        self.__cars = pg.sprite.Group()

        self.__setup_level()
        self.__load_map()
        self.__load_obstacles()
        self.__load_cars(begin=True)
        self.__load_player()
    
    def __setup_level(self):
        self.__background.fill(pg.Color(255, 255, 255))
        self.__level = levels[state.LEVEL_RUNNING - 1]
        state.SHOW_POPUP = False
        self.__waiting_play.open()

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
            if begin: position[0] = randrange(-400, WIDTH + 120)
            else:
                if direction == 'right': position[0] = randrange(WIDTH + 120, WIDTH + 1000)
                else: position[0] = randrange(-1000, -50)
            self.__cars.add(Car(path, position, direction, speed))
        if len(self.__cars) < min_car: self.__load_cars()
    
    def __load_player(self):
        player = self.__level.player
        self.__player = Player(
            player.name, player.health, player.position, player.speed, 
            self.__obstacles, self.__cars, self.__header
        )
        self.__player.update()

    def __load_civilians(self):
        pass
    
    def __start(self):
        self.__status = 'running'

    def __pause(self):
        self.__status = 'pause'
        self.__waiting_play.open()

    def __input_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]: self.__pause()

    def render(self):
        self.__input_keys()
        self.__screen.blit(self.__background, (0, 0))
        self.__screen.blit(self.__map, (0, 0))
        self.__obstacles.draw(self.__screen)
        self.__cars.draw(self.__screen)
        self.__player.render(self.__screen)
        self.__header.render(self.__screen)
        
        if self.__status == 'running':
            self.__load_cars()
            self.__cars.update()
            self.__player.update()
        else:    
            self.__waiting_play.render(self.__screen)