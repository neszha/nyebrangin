from asyncore import loop
from time import time
import pygame as pg
import src.state as state
from src.components.Audio import Audio

press_delay = 0.3 # Second.
temp_time = time()

class Button:
    
    def __init__(self, path, positions, command0=False, command1=False, command_data=False, data=None, index=1):
        self.__positions = positions
        self.__btn = pg.image.load(path).convert_alpha()
        self.__btn_rect = self.__btn.get_rect(center=self.__positions)
        self.__hovered = False
        self.__clicked = False
        self.__command0 = command0
        self.__command1 = command1
        self.__command_data = command_data
        self.__data = data
        self.__index = index
        self.__click_fx = Audio('assets/audios/effects/click.wav', 'sound_fx', 0.2)

    def __hover_detector(self):
        mouse_pos = pg.mouse.get_pos()
        if self.__btn_rect.collidepoint(mouse_pos): self.__hovered = True
        else: self.__hovered = False

    def __click_detector(self):
        global temp_time, press_delay
        if self.__hovered and pg.mouse.get_pressed()[0] and not self.__clicked:
            if (time() - temp_time) < press_delay: return False
            temp_time = time()
            self.__click_fx.play()
            self.__clicked = True
            if self.__command0: self.__command0()
            if self.__command1: self.__command1()
            if self.__command_data: self.__command_data(self.__data)
        if not pg.mouse.get_pressed()[0]: self.__clicked = False

    def render(self, screen):
        if self.__index == state.INDEX_LAYER:
            self.__hover_detector()
            self.__click_detector()
        screen.blit(self.__btn, self.__btn_rect)
        

