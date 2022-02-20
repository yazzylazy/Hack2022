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
        self.magenta = (255, 0, 255)

        # defining a font
        self.largeFont = pygame.font.SysFont('comicsansms', 90)

    def drawText(self, text, font, color, surface, x, y):
        textobj = font.render(text,1,color)
        textrect =textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj,textrect)

    def winScreen(self):
        winScreen = True
        while winScreen:
            self.screen.fill(self.white)
            self.drawText("You win!! congratsss", self.largeFont, self.magenta, self.screen,
                          WIDTH / 2 - 200, HEIGHT / 2 - 200)
            self.drawText("Press any key to play again", self.largeFont, self.magenta, self.screen,
                          WIDTH / 2 - 200, HEIGHT / 2 + 100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    winScreen = False
                if event.type == pygame.KEYDOWN:
                    exec(open('main.py').read())
                    winScreen = False

            # updates the frames of the game
            pygame.display.update()