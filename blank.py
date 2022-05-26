import pygame as pg
from src.config import *
  
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGTH))  
clock = pg.time.Clock()
run = True
  
while run:  
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            run = False  
    pg.display.update()
    clock.tick(FPS)