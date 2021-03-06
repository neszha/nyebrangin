import pygame as pg
from time import time
from src.components.People import People
from src.components.Audio import Audio

# Membuat karakter player.
class Player(People):

    def __init__(self, name, health, position, speed, header, obstacles, cars, civilians):
        super().__init__(name, position, cars, obstacles, header)
        self.health = health
        self.__ghost = False
        self.__show_character = True
        self.__speed = speed
        self.__civilians = civilians
        self.__key_pressed = { 'space': time() }
        self.__temp = {'speed': speed, 'ghost_delay': 0, 'ghost_blit': 0, 'footstep_fx': time()}

        self.__footstep_fx = Audio('assets/audios/effects/footsteps.mp3', 'sound_fx', 0.4)
        self._header.health = self.health
        self.shadow.fill(pg.Color(0, 0, 0, 50))

    def __input_controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.direction.y = -1
            self.direction_status = 'up'
            self.__footstep()
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.direction_status = 'down'
            self.__footstep()
        else: self.direction.y = 0
            
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.direction_status = 'right'
            self.__footstep()
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.direction_status = 'left'
            self.__footstep()
        else: self.direction.x = 0

        if keys[pg.K_SPACE]: self.__bring_civilian_collapse()

        # Manipulasi kecepatan player.
        walk_speed = 2
        if keys[pg.K_w]: self.__speed = walk_speed
        else: self.__speed = self.__temp['speed']

    def __footstep(self):
        if  time() - self.__temp['footstep_fx'] > 0.8:
            self.__footstep_fx.play()
            self.__temp['footstep_fx'] = time()
        
    def _collision_obstacles(self, direction):
        for obstacle in self._obstacles:
            if obstacle.rect.colliderect(self.rect) and not obstacle.is_danger():
                if direction == 'x':
                    if self.direction.x > 0: self.rect.right = obstacle.rect.left
                    if self.direction.x < 0: self.rect.left = obstacle.rect.right
                if direction == 'y':
                    if self.direction.y > 0: self.rect.bottom = obstacle.rect.top
                    if self.direction.y < 0: self.rect.top = obstacle.rect.bottom
            elif obstacle.rect.colliderect(self.rect) and obstacle.is_danger():
                self.__reduce_health()

    def _collision_cars(self):
        for car in self._cars:
            if car.rect.colliderect(self.rect):
                if self._object_id['car'] != id(car):
                    self._car_hit_fx.play()
                    self.__reduce_health()
                    self._object_id['car'] = id(car)

    def __collistion_civilians(self):
        for civilian in self.__civilians:
            if civilian.rect.colliderect(self.rect):
                civilian.show_destination = True
                civilian.shadow.fill(pg.Color(102, 255, 51, 150))
                self._object_id['civilian'] = id(civilian)
            else:
                civilian.show_destination = False

    def __follow_me(self):
        direction = self.direction_status
        x, y = self.rect.x, self.rect.y
        for civilian in self.__civilians:
            if civilian.bring_player:
                if direction == 'down': y -= 24
                elif direction == 'up': y += 24
                elif direction == 'left': x += 24
                elif direction == 'right': x -= 24
                civilian.direction_status = direction
                civilian.rect.x = x
                civilian.rect.y = y
                civilian._animate()

    def __reduce_health(self):
        if self.__ghost: return False
        self.__ghost = True
        self.__temp['ghost_delay'] = time() + 2
        self.health -= 1
        self._header.health = self.health

    def __bring_civilian_collapse(self):
        bring_delay = 0.2
        if (time() - self.__key_pressed['space']) < bring_delay: return False
        for civilian in self.__civilians:
            bring = civilian.bring_player
            if civilian.rect.colliderect(self.rect): civilian.bring_player = not bring
        self.__key_pressed['space'] = time()

    def __ghost_watch(self):
        if self.__ghost:
            delay = self.__temp['ghost_delay'] - time()
            self.__show_character = False
            if delay <= 0: 
                self.__ghost = False
                self.__show_character = True
            self.__temp['ghost_blit'] += 1
            if self.__temp['ghost_blit'] >= 3: self.__show_character = True
            if self.__temp['ghost_blit'] >= 6: self.__temp['ghost_blit'] = 0

    def _move(self):
        if self.direction.magnitude() != 0: self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * self.__speed
        self._collision_obstacles('x')
        self.rect.y += self.direction.y * self.__speed
        self._collision_obstacles('y')
        self.position = [self.rect.x - 17, self.rect.y - 50]

    def update(self):
        self.__input_controls()
        self._animate()
        self._move()
        self._collision_cars()
        self.__collistion_civilians()
        self.__follow_me()

    def render(self, screen):
        self.__ghost_watch()
        if self.__show_character:
            screen.blit(self.shadow, self.rect)
            screen.blit(self.image, self.position)