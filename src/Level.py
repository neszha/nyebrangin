import pygame as pg
import src.state as state
from src.config import *
from src.levels.list import levels
from src.components.Car import Car
from random import randrange, choice
from src.components.Audio import Audio
from src.components.Obstacle import Obstacle
from src.components.popups.Finish import Finish
from src.components.GameHeader import GameHeader
from src.components.peoples.Player import Player
from src.components.popups.GameOver import GameOver
from src.components.peoples.Civilian import Civilian
from src.components.popups.WaitingPlay import WaitingPlay
from src.components.obstacles.ForbiddenArea import ForbiddenArea

# class Data: pass
class Level:
    
    def __init__(self):
        self.__done = False
        self.__status = 'waiting'
        self.__screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.__background = pg.Surface((WIDTH, HEIGTH))
        self.__waiting_play = WaitingPlay(start_command=self.__start)
        self.__game_finish = Finish()
        self.__game_over = GameOver()
        self.__header = GameHeader()
        self.__obstacles = pg.sprite.Group()
        self.__cars = pg.sprite.Group()
        self.__civilians = pg.sprite.Group()

        self.__setup_level()
        self.__load_map()
        self.__load_obstacles()
        self.__load_cars(begin=True)
        self.__load_civilians()
        self.__load_player()
    
    def __setup_level(self):
        self.backsong = Audio('assets/audios/backsongs/bs-play0.mp3', 'music')
        self.backsong.play(loops=-1)

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

        obstacles = self.__level.obstacle.list
        for data in obstacles:
            obstacle = Obstacle(data['image_path'], data['position'], data['scale'], data['rotation'], data['danger'])
            self.__obstacles.add(obstacle)

    def __load_cars(self, begin=False):
        car = self.__level.car
        [min_car, max_car] = car.traffic_density
        if len(self.__cars) <= max_car - 1:
            path = choice(car.use)
            position = [-120, 0]
            direction = choice(list(car.direction))
            position_index = randrange(0, len(car.direction[direction]))
            position[1] = randrange(car.direction[direction][position_index][0], car.direction[direction][position_index][1])
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
            self.__header, self.__obstacles, self.__cars, self.__civilians
        )
        self.__player.update()

    def __load_civilians(self):
        civilians = self.__level.civilian.list
        for data in civilians:
            civilian = Civilian(
                data['name'], data['position'], data['destination'], 
                self.__header, self.__cars, self.__obstacles
            )
            self.__civilians.add(civilian)
        self.__civilians.update()
        self.__header.civilian = len(civilians)
    
    def __start(self):
        self.__status = 'running'

    def __pause(self):
        self.__status = 'pause'
        self.__waiting_play.open()

    def __game_finish_handdle(self):
        state.SHOW_POPUP = False
        self.__game_finish.set_item('00:00', 3)
        self.__game_finish.open()
        self.__done = True
        self.__status = 'game_finish'

    def __game_over_handdle(self): 
        state.SHOW_POPUP = False
        self.__game_over.open()
        self.__done = True
        self.__status = 'game_over'

    def __watch_level(self):
        if self.__done: return True
        if self.__header.civilian <= 0: self.__game_finish_handdle()
        elif self.__player.health <= 0: self.__game_over_handdle()

    def __input_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]: self.__pause()

    def render(self):
        self.backsong.watch_setting()
        self.__input_keys()
        self.__watch_level()
        self.__screen.blit(self.__background, (0, 0))
        self.__screen.blit(self.__map, (0, 0))
        self.__obstacles.draw(self.__screen)
        self.__cars.draw(self.__screen)
        for civilian in self.__civilians: civilian.render(self.__screen)
        self.__player.render(self.__screen)
        self.__header.render(self.__screen)
        self.__game_finish.render(self.__screen)
        self.__game_over.render(self.__screen)
        
        if self.__status == 'running':
            self.__load_cars()
            self.__cars.update()
            self.__civilians.update()
            self.__player.update()
        elif self.__status == 'waiting' or self.__status == 'pause':    
            self.__waiting_play.render(self.__screen)