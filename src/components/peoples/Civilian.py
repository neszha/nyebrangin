import pygame as pg
from src.components.Audio import Audio
from src.components.People import People

# Membuat karakter civilian.
class Civilian(People):

    def __init__(self, name, position, destionation, header, cars, obstacles):
        super().__init__(name, position, cars, obstacles, header)
        self.show_destination = False
        self.bring_player = False
        self.__position = position
        self.__destination = destionation
        self.__load_componenets()

    def __load_componenets(self):
        self.__des_surf = pg.image.load('assets/images/civilian-destination.png').convert_alpha()
        self.__des_rect = self.__des_surf.get_rect(center=self.__destination)
        self.__des_fx = Audio('assets/audios/effects/click.wav', 'sound_fx', 0.2)

    def _collision_cars(self):
        for car in self._cars:
            if car.rect.colliderect(self.rect):
                if self._object_id['car'] != id(car):
                    self.show_destination = False
                    self.bring_player = False
                    self.__reset_position()
                    self._object_id['car'] = id(car)
                    self._car_hit_fx.play()

    def _collision_obstacles(self):
        for obstacle in self._obstacles:
            if obstacle.rect.colliderect(self.rect) and obstacle.is_danger():
                self.show_destination = False
                self.bring_player = False
                self.__reset_position()

    def __collotion_destination(self):
        if self.rect.colliderect(self.__des_rect):
            self._header.civilian -= 1
            self.__des_fx.play()
            self.kill()

    def __reset_position(self): 
        [x, y] = self.__position
        self.rect.x = x
        self.rect.y = y

    def _move(self):
        self.position = [self.rect.x - 17, self.rect.y - 50]

    def update(self):
        self._animate()
        self._move()
        self._collision_cars()
        self.__collotion_destination()
        self._collision_obstacles()

    def render(self, screen):
        if self.bring_player:
            self.shadow.fill(pg.Color(255, 0, 0, 200))
            screen.blit(self.shadow, self.rect)
            screen.blit(self.__des_surf, self.__des_rect)
        elif self.show_destination:
            screen.blit(self.__des_surf, self.__des_rect)
            screen.blit(self.shadow, self.rect)
        screen.blit(self.image, self.position)