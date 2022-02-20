import pygame, sys
import main
from icons import Icon
import random
from settings import *

class MainMenu:

    def __init__(self):
        pygame.init()
        print("INitialized")
        # initialize clock and game
        self.clock = pygame.time.Clock()



        # set screen
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.screen.fill((240,248,255))
        pygame.display.set_caption("Online School Simulator")
        # set font
        self.font = pygame.font.SysFont("comicsansms",95)

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text,1,color)
        textrect =textobj.get_rect()
        textrect.topleft = (x,y)
        surface.blit(textobj,textrect)
    
    def main_menu(self):

        while True:
            self.draw_text('im a dissapoint me, please help',self.font,(0,0,0),self.screen,20,20)
            pos = pygame.mouse.get_pos()
            buttonOne = pygame.Rect(50,100,200,50)
            if buttonOne.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                exec(open('main.py').read())
                print("clicked button")

            buttonTwo = pygame.Rect(50,200,200,50)
            if buttonTwo.collidepoint(pos):
                pass

            pygame.draw.rect(self.screen, (255,0,0), buttonOne)
            pygame.draw.rect(self.screen, (255,0,0), buttonTwo)
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
            self.clock.tick(FPS)

    # def options(self):
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #             if event.type == KEYDOWN:
    #                 if event.key == K_ESCAPE:
    #                     pygame.quit()
    #                     sys.exit()
    #         pygame.display.update()
    #         self.clock.tick(FPS)


mainmenu = MainMenu()
mainmenu.main_menu()
