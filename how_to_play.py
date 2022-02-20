import pygame, sys
import main
from icons import Icon
from main import Game
import random
from settings import *

class HowToPlay:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen = pygame.image.load('images2/howtoplay.png')
        self.screen = pygame.transform.scale(self.screen, (WIDTH, HEIGHT))

        while True:

            self.screen.blit(self.screen, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    exec(open('main.py').read())
                    game = Game()
                    game.main_menu()

if __name__ == '__main__':
    End = End()