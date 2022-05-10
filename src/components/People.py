import pygame as pg
from abc import ABC, abstractmethod

class People(pg.sprite.Sprite, ABC):
    
    def __init__(self, name, position):
        super().__init__()
        self.position = position
        self.last_position = [0, 0]
        self.direction = pg.math.Vector2()
        self.direction_status = 'down'
        self.frame_index = 0
        self.image = None

        self.__load_characters(name)

    def __load_characters(self, name):
        self.shadow = pg.Surface([25, 10]).convert_alpha()
        self.shadow.fill(pg.Color(0, 0, 0, 0))
        self.rect = self.shadow.get_rect(midbottom=self.position)
        self.images = { 'up': [], 'down': [], 'left': [], 'right': [] }
        
        for direction in ['up', 'down', 'left']:
            for i in range(30):
                character = pg.image.load(f'assets/images/peoples/{name}/{direction}/{i}.png').convert_alpha()
                self.images[direction].append(character)
                
        for character in self.images['left']:
            character_flip = pg.transform.flip(character, True, False)
            self.images['right'].append(character_flip)

    def _animate(self):
        images = self.images[self.direction_status]
        self.image = images[int(self.frame_index)]
        if self.last_position != self.position: self.frame_index += 1
        if self.frame_index >= len(images): self.frame_index = 0
        self.last_position = self.position
        # print(self.last_position, self.position, self.frame_index)

    # @abstractmethod
    # def update(self):
    #     pass
    
    # @abstractmethod
    # def render(self, screen):
    #     pass