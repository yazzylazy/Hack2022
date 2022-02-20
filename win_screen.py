import pygame
import sys
from settings import *

# initializing the constructor
pygame.init()

class Win:
    def __init__(self):

        # opens up a window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # colours
        self.white = (255, 255, 255)
        self.magenta = (255,0, 255)

        # defining a font
        self.largeFont = pygame.font.SysFont('Corbel', 60)

    def winScreen(self):
        youWinMsg = self.largeFont.render('You Win!!', True, self.magenta)
        playAgainMsg = self.largeFont.render("press space to play again", True, self.white)
        self.screen.blit(youWinMsg, (WIDTH/2, HEIGHT/2-300))
        self.screen.blit(playAgainMsg, (WIDTH/2, HEIGHT/2+100))

        winScreen = True
        while winScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    winScreen = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        exec(open('main.py').read())
                        winScreen = False

            self.screen.fill(self.white)

            # updates the frames of the game
            pygame.display.update()