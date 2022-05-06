import pygame as pg
from abc import ABC, abstractmethod

class People(pg.sprite.Sprite, ABC):
    
    def __init__(self, name, positions):
        super().__init__()
        self.positions = positions
        self.__load_character(name)

    def __load_character(self, name):
        self.shadow = pg.Surface([25, 10]).convert_alpha()
        self.shadow.fill(pg.Color(0, 0, 0, 100))
        self.shadow_rect = self.shadow.get_rect(midbottom=self.positions)
        self.characters = { 'front': [] }
        
        for i in range(3):
            character = pg.image.load(f'assets/peoples/{name}/front-1.png').convert_alpha()
            self.characters['front'].append(character)

    @abstractmethod
    def render(self, screen):
        pass