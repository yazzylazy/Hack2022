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
        youWinMsg = self.largeFont.render('You Win!!', True, self.magenta)
        playAgainMsg = self.largeFont.render("press space to play again", True, self.white)
        self.screen.blit(youWinMsg, (WIDTH/2, HEIGHT/2-200))
        self.screen.blit(playAgainMsg, (WIDTH/2, HEIGHT/2+100))


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

                    if event.key == pygame.K_SPACE:
                        print("back to main game")
                        exec(open('main.py').read())
                        winScreen = False

            self.screen.fill(self.white)


            # updates the frames of the game
            pygame.display.update()


win = Win()
win.winScreen()
