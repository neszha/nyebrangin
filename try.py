import pygame
from src.config import *

class Main:

    def __init__(self, game_name):
        self.__game_name = game_name
        pygame.init()
        pygame.display.set_caption(self.__game_name)
        bs = pygame.mixer.Sound('assets/audios/backsongs/bs-menu.mp3')
        bs.set_volume(0.5)
        bs.play()
        self.clock = pygame.time.Clock()

    def __game_loop(self):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.__background = pygame.Surface((WIDTH, HEIGTH))
        self.__background.fill(pygame.Color(175, 208, 233))

        ## Custom code.

        self.__screen.blit(self.__background, (0, 0))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu.exit()
                if event.type == pygame.MOUSEMOTION:
                    print(pygame.mouse.get_pos())
            
            self.__game_loop()
            pygame.display.update()
            self.clock.tick(FPS)

game = Main('Pygame - TRY')
game.run()