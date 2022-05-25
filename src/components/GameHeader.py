import pygame as pg
from src.config import *
from src.components.Text import Text

# Handdle tampilan header game.
class GameHeader:
    
    def __init__(self):
        self.health = 0
        self.civilian = 0
        self.countdown = '0:00:00'
        self.__load_componenets()

    def __load_componenets(self):
        self.__civilian_counter = Text(self.civilian, [18, 10], 36)
        self.__civilian_counter.to_top_left()
        self.__coutdown_string = Text(self.countdown, (WIDTH/2, 34), 36)

    def __render_health(self, screen):
        position = [WIDTH - 60, 12]
        for i in range(self.health):
            image = pg.image.load('assets/images/heart.png').convert_alpha()
            rect = image.get_rect(topleft=position)
            screen.blit(image, rect)
            position[0] -= 54 

    def __render_countdown(self, screen):
        self.__coutdown_string.set_text(self.countdown)
        self.__coutdown_string.render(screen)

    def __render_civilian_len(self, screen):
        self.__civilian_counter.set_text(self.civilian)
        self.__civilian_counter.to_top_left()
        self.__civilian_counter.render(screen)

    def render(self, screen):
        self.__render_health(screen)
        self.__render_civilian_len(screen)
        self.__render_countdown(screen)