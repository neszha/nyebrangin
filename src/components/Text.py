import pygame as pg

pg.font.init()

class Text:
    
    def __init__(self, text, positions, size, color=(255, 255, 255)):
        self.font = pg.font.Font('assets/fonts/Galindo-Regular.ttf', size)
        self.text  = self.font.render(text, True, color)
        self.text_rect = self.text.get_rect(center=positions)
        
    def render(self, screen):
        screen.blit(self.text, self.text_rect)