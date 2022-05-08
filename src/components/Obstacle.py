import pygame as pg

class Obstacle(pg.sprite.Sprite):
    
    def __init__(self, image, location):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(topleft=location)