import pygame as pg

class Obstacle(pg.sprite.Sprite):
    
    def __init__(self, image, position, scale=1, rotation=0, danger=False, is_area=False):
        super().__init__()
        self.__danger = danger
        self.__load_componenets(image, position, scale, rotation, is_area)

    def __load_componenets(self, image, position, scale, rotation, is_area):
        self.image = image
        if not is_area: 
            self.image = pg.image.load(image).convert_alpha()
            self.image = pg.transform.rotate(self.image, rotation)
            [size_x, size_y] = self.image.get_size()
            self.image = pg.transform.scale(self.image, (size_x * scale, size_y * scale))
        self.rect = self.image.get_rect(topleft=position)

    def is_danger(self):
        return self.__danger   