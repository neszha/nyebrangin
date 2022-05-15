import pygame as pg
from src.components.People import People

class Civilian(People):

    def __init__(self, name, position, destionation, header, cars):
        super().__init__(name, position)
        self.show_destination = False
        self.bring_player = False
        self.__position = position
        self.__destination = destionation
        self.__header = header
        self.__cars = cars
        self.__object_id = { 'car': 0}

        self.__load_componenets()

    def __load_componenets(self):
        self.__des_surf = pg.image.load('assets/images/civilian-destination.png').convert_alpha()
        self.__des_rect = self.__des_surf.get_rect(center=self.__destination)
    
    def __move(self):
        self.position = [self.rect.x - 17, self.rect.y - 50]

    def __collision_cars(self):
        for car in self.__cars:
            if car.rect.colliderect(self.rect):
                if self.__object_id['car'] != id(car):
                    print(f'Civilian ditabrak mobil {id(car)}')
                    self.show_destination = False
                    self.bring_player = False
                    self.__reset_position()
                    self.__object_id['car'] = id(car)

    def __collotion_destination(self):
        if self.rect.colliderect(self.__des_rect):
            self.__header.civilian -= 1
            self.kill()

    def __reset_position(self): 
        [x, y] = self.__position
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self._animate()
        self.__move()
        self.__collision_cars()
        self.__collotion_destination()

    def render(self, screen):
        if self.bring_player:
            self.shadow.fill(pg.Color(255, 0, 0, 200))
            screen.blit(self.shadow, self.rect)
            screen.blit(self.__des_surf, self.__des_rect)
        elif self.show_destination:
            screen.blit(self.__des_surf, self.__des_rect)
            screen.blit(self.shadow, self.rect)
        screen.blit(self.image, self.position)