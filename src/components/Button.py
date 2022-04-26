import pygame as pg

class Button:
    
    def __init__(self, path, positions, command0, command1 = False):
        self.__positions = positions
        self.__btn = pg.image.load(path).convert_alpha()
        self.__btn_rect = self.__btn.get_rect(center = self.__positions)
        self.__hovered = False
        self.__clicked = False
        self.__command0 = command0
        self.__command1 = command1

    def render(self, screen):
        self.__hover_detector()
        self.__click_detector()
        screen.blit(self.__btn, self.__btn_rect)

    def __hover_detector(self):
        mouse_pos = pg.mouse.get_pos()
        if self.__btn_rect.collidepoint(mouse_pos):
            self.__hovered = True
        else:
            self.__hovered = False

    def __click_detector(self):
        if self.__hovered and pg.mouse.get_pressed()[0] and not self.__clicked:
            self.__clicked = True
            self.__command0()
            if self.__command1: self.__command1()
        if not pg.mouse.get_pressed()[0]: self.__clicked = False
        

