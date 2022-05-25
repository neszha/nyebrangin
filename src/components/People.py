import pygame as pg
from src.components.Audio import Audio
from abc import ABC, abstractmethod

# Membuat karakter player atau civilian.
class People(pg.sprite.Sprite, ABC):
    
    def __init__(self, name, position, cars, obstacles, header):
        super().__init__()
        self.__frame_index = 0
        self.__last_position = [0, 0]
        self._object_id = { 'car': 0, 'civilian': 0}
        self._cars = cars
        self._obstacles = obstacles
        self._header = header
        self._car_hit_fx = Audio('assets/audios/effects/hit-car.mp3', 'sound_fx', 0.3)
        self.position = position
        self.direction = pg.math.Vector2()
        self.direction_status = 'down'
        self.image = None
        self.__load_characters(name)

    def __load_characters(self, name):
        self.shadow = pg.Surface([25, 10]).convert_alpha()
        self.shadow.fill(pg.Color(0, 0, 0, 0))
        self.rect = self.shadow.get_rect(midbottom=self.position)
        self.__images = { 'up': [], 'down': [], 'left': [], 'right': [] }
        
        for direction in ['up', 'down', 'left']:
            for i in range(30):
                character = pg.image.load(f'assets/images/peoples/{name}/{direction}/{i}.png').convert_alpha()
                self.__images[direction].append(character)
                
        for character in self.__images['left']:
            character_flip = pg.transform.flip(character, True, False)
            self.__images['right'].append(character_flip)

    def _animate(self):
        images = self.__images[self.direction_status]
        self.image = images[int(self.__frame_index)]
        if self.__last_position != self.position: self.__frame_index += 1
        if self.__frame_index >= len(images): self.__frame_index = 0
        self.__last_position = self.position

    @abstractmethod
    def _collision_cars(self): pass

    @abstractmethod
    def _collision_obstacles(self): pass

    @abstractmethod
    def _move(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def render(self): pass