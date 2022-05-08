import pygame as pg
from src.config import *

class GameHeader:
    
    def __init__(self):
        self.health = 0

    def __render_health(self, screen):
        position = [WIDTH - 60, 12]
        for i in range(self.health):
            image = pg.image.load('assets/images/heart.png').convert_alpha()
            rect = image.get_rect(topleft=position)
            screen.blit(image, rect)
            position[0] -= 54

    def render(self, screen):
        self.__render_health(screen)