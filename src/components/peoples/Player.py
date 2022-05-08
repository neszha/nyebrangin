import pygame as pg
from src.components.People import People

class Player(People):

    def __init__(self, name, health, positions, speed, obstacles, cars, header):
        super().__init__(name, positions)
        self.__health = health
        self.__speed = speed
        self.__obstacles = obstacles
        self.__cars = cars
        self.__car_id = 0
        self.__header = header
        
        self.__header.health = self.__health

    def __input_controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.direction.y = -1
            self.direction_status = 'up'
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.direction_status = 'down'
        else: self.direction.y = 0
            
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.direction_status = 'right'
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.direction_status = 'left'
        else: self.direction.x = 0

    def __move(self):
        if self.direction.magnitude() != 0: self.direction = self.direction.normalize()
        self.shadow_rect.x += self.direction.x * self.__speed
        self.__collision_obstacles('x')
        self.shadow_rect.y += self.direction.y * self.__speed
        self.__collision_obstacles('y')
        self.positions = [self.shadow_rect.x - 17, self.shadow_rect.y - 50]
        self.__collision_cars()

    def __collision_obstacles(self, direction):
        for obstacle in self.__obstacles:
            if obstacle.rect.colliderect(self.shadow_rect):
                if direction == 'x':
                    if self.direction.x > 0: self.shadow_rect.right = obstacle.rect.left
                    if self.direction.x < 0: self.shadow_rect.left = obstacle.rect.right
                if direction == 'y':
                    if self.direction.y > 0: self.shadow_rect.bottom = obstacle.rect.top
                    if self.direction.y < 0: self.shadow_rect.top = obstacle.rect.bottom

    def __collision_cars(self):
        for car in self.__cars:
            if car.rect.colliderect(self.shadow_rect):
                if self.__car_id != id(car):
                    print(f'Ditabrak mobil {self.__car_id}')
                    self.__reduce_health()
                    self.__car_id = id(car)

    def __reduce_health(self):
        self.__health -= 1
        self.__header.health = self.__health
        if(self.__health < 1): print('GAME OVER', self.__health)

    def bring_civilian(self):
        pass

    def free_civilian(self):
        pass

    def update(self):
        self.__input_controls()
        self._animate()
        self.__move()

    def render(self, screen):
        screen.blit(self.shadow, self.shadow_rect)
        screen.blit(self.character, self.positions)