import pygame as pg

class Obstacle(pg.sprite.Sprite):
    
    def __init__(self, name, image, location):
        super().__init__()
        self.__name = name
        self.__image = image
        self.__location = location