import pygame as pg
from abc import ABC, abstractmethod

class People(pg.sprite.Sprite, ABC):
    
    def __init__(self, name, positions):
        super().__init__()
        self.positions = positions
        self.last_positions = [0, 0]
        self.direction = pg.math.Vector2()
        self.direction_status = 'down'
        self.frame_index = 0
        self.character = None

        self.__load_characters(name)

    def __load_characters(self, name):
        self.shadow = pg.Surface([25, 10]).convert_alpha()
        self.shadow.fill(pg.Color(0, 0, 0, 20))
        self.shadow_rect = self.shadow.get_rect(midbottom=self.positions)
        self.characters = { 'up': [], 'down': [], 'left': [], 'right': [] }
        
        for direction in ['up', 'down', 'left']:
            for i in range(30):
                character = pg.image.load(f'assets/peoples/{name}/{direction}/{i}.png').convert_alpha()
                self.characters[direction].append(character)

        for character in self.characters['left']:
            character_flip = pg.transform.flip(character, True, False)
            self.characters['right'].append(character_flip)

    def _animate(self):
        characters = self.characters[self.direction_status]
        self.character = characters[int(self.frame_index)]
        if self.last_positions != self.positions: self.frame_index += 1
        if self.frame_index >= len(characters): self.frame_index = 0
        self.last_positions = self.positions
        # print(self.last_positions, self.positions, self.frame_index)

    @abstractmethod
    def render(self, screen):
        pass