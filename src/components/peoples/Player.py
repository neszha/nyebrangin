import pygame as pg
from src.components.People import People

class Player(People):

    def __init__(self, name, positions, speed, obstacles):
        super().__init__(name, positions)
        self.__speed = speed
        self.__obstacles = obstacles

    def __input_controls(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_UP]:
            self.direction.y = -1
            self.direction_status = 'up'
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.direction_status = 'down'
        else:
            self.direction.y = 0
            
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.direction_status = 'right'
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.direction_status = 'left'
        else:
            self.direction.x = 0

    def __move(self):
        if self.direction.magnitude() != 0: self.direction = self.direction.normalize()
        self.shadow_rect.x += self.direction.x * self.__speed
        self.__collision_obstacles('x')
        self.shadow_rect.y += self.direction.y * self.__speed
        self.__collision_obstacles('y')
        self.positions = [self.shadow_rect.x - 17, self.shadow_rect.y - 50]

    def __collision_obstacles(self, direction):
        for sprite in self.__obstacles:
            if sprite.rect.colliderect(self.shadow_rect):
                if direction == 'x':
                    if self.direction.x > 0: self.shadow_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.shadow_rect.left = sprite.rect.right
                if direction == 'y':
                    if self.direction.y > 0: self.shadow_rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.shadow_rect.top = sprite.rect.bottom

    def bring_civilian(self):
        pass

    def free_civilian(self):
        pass

    def render(self, screen):
        self.__input_controls()
        self._animate()
        self.__move()
        screen.blit(self.shadow, self.shadow_rect)
        screen.blit(self.character, self.positions)