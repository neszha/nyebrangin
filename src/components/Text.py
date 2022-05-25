import pygame as pg

pg.font.init()
fonts = {
    'Galindo-Regular': 'assets/fonts/Galindo-Regular.ttf'
}

# Membuat karakter tulisan.
class Text:
    
    def __init__(self, text, position, size, color=(255, 255, 255), font='Galindo-Regular'):
        self.__color = color
        self.__position = position
        self.__size = size
        self.__string = str(text)
        self.__font_system = font
        self.update()

    def set_text(self, text):
        self.__string = str(text)
        self.update()

    def to_top_left(self):
        self.__text_rect = self.__text.get_rect(topleft=self.__position)

    def to_center(self):
         self.__text_rect = self.__text.get_rect(center=self.__position)

    def update(self):
        global fonts
        set_font = pg.font.Font(fonts[self.__font_system], self.__size)
        self.__text  = set_font.render(self.__string, True, self.__color)
        self.to_center()
        
    def render(self, screen):
        screen.blit(self.__text, self.__text_rect)