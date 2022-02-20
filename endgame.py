import pygame, sys
import main
from icons import Icon
from main import Game
import random
from settings import *

class End:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((0,0,0))
        self.death = pygame.image.load('images2/blueScreen.png')
        self.death = pygame.transform.scale(self.screen, (WIDTH, HEIGHT))

        while True:

            self.screen.blit(self.death, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game = Game()
                    game.main_menu()
            pygame.display.update()
if __name__ == '__main__':
    End = End()
