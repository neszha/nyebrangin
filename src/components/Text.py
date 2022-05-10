import pygame as pg

pg.font.init()
fonts = {
    'Galindo-Regular': 'assets/fonts/Galindo-Regular.ttf'
}

class Text:
    
    def __init__(self, text, position, size, color=(255, 255, 255), font='Galindo-Regular'):
        self.color = color
        self.position = position
        self.size = size
        self.string = str(text)
        self.fontSystem = font
        self.update()

    def set_text(self, text):
        self.string = str(text)
        self.update()

    def to_top_left(self):
        self.text_rect = self.text.get_rect(topleft=self.position)

    def to_center(self):
         self.text_rect = self.text.get_rect(center=self.position)

    def update(self):
        global fonts
        self.font = pg.font.Font(fonts[self.fontSystem], self.size)
        self.text  = self.font.render(self.string, True, self.color)
        self.to_center()
        
    def render(self, screen):
        screen.blit(self.text, self.text_rect)