import pygame as pg
from src.components.People import People

class Player(People):

    def __init__(self, name, positions, speed):
        super().__init__(name, positions)
        self.__speed = speed

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
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.shadow_rect.x += self.direction.x * self.__speed
        # self.collision('horizontal')
        self.shadow_rect.y += self.direction.y * self.__speed
        # self.collision('vertical')
        self.positions = [self.shadow_rect.x - 17, self.shadow_rect.y - 50]

    # def collision(self, direction):
    #     if direction == 'horizontal':
	# 		for sprite in self.obstacle_sprites:
	# 			if sprite.rect.colliderect(self.rect):
	# 				if self.direction.x > 0: # moving right
	# 					self.rect.right = sprite.rect.left
	# 				if self.direction.x < 0: # moving left
	# 					self.rect.left = sprite.rect.right

	# 	if direction == 'vertical':
	# 		for sprite in self.obstacle_sprites:
	# 			if sprite.rect.colliderect(self.rect):
	# 				if self.direction.y > 0: # moving down
	# 					self.rect.bottom = sprite.rect.top
	# 				if self.direction.y < 0: # moving up
	# 					self.rect.top = sprite.rect.bottom

    def __right(self):
        pass

    def __left(self):
        pass

    def __up(self):
        pass

    def __down(self):
        pass

    def __right(self):
        pass

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