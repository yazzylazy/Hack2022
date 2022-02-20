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
        self.screen = pygame.image.load('images2/howtoplay_v3.png')
        self.screen = pygame.transform.scale(self.screen, (WIDTH, HEIGHT))

    def how_to_play(self):
        pygame.mixer.music.load('78bpm gametimeee.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.15)
        self.bg_img = pygame.image.load('images2/howtoplay_v3.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))
        self.bg_img.blit(self.bg_img, (0, 0))
        display.update()
        while True:
            pos = pygame.mouse.get_pos()

            buttonOne = pygame.Rect(590, 300, 565, 140)

            if buttonOne.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                exec(open('main.py').read())


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

if __name__ == '__main__':
    HowToPlay = HowToPlay()
    HowToPlay.how_to_play()