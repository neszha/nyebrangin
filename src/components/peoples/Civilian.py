import pygame as pg
from src.components.People import People

class Civilian(People):

    def __init__(self, name, position, destionation):
        super().__init__(name, position)
        self.show_destination = False
        self.bring_player = False
        self.__position = position
        self.__destination = destionation

        self.__load_componenets()

    def __load_componenets(self):
        self.__des_surf = pg.image.load('assets/images/civilian-destination.png').convert_alpha()
        self.__des_rect = self.__des_surf.get_rect(center=self.__destination)
    
    def __move(self):
        self.position = [self.rect.x - 17, self.rect.y - 50]

    def update(self):
        self._animate()
        self.__move()

    def render(self, screen):
        if self.bring_player:
            self.shadow.fill(pg.Color(255, 0, 0, 200))
            screen.blit(self.shadow, self.rect)
            screen.blit(self.__des_surf, self.__des_rect)
        if self.show_destination:
            screen.blit(self.__des_surf, self.__des_rect)
            screen.blit(self.shadow, self.rect)
        screen.blit(self.image, self.position)