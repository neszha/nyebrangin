import pygame as pg
from src.components.Obstacle import Obstacle

class ForbiddenArea(Obstacle):
    
    def __init__(self, size, location, rgba):
        self.area = pg.Surface(size).convert_alpha()
        self.area.fill(pg.Color(rgba))
        super().__init__(self.area, location, is_area=True)

    