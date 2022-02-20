import pygame, sys
import random

from icons import Icon
from win_screen import Win
from settings import *


class Game:

    def __init__(self):
        pygame.init()
        # Title and Icon
        pygame.display.set_caption("Online School Simulator")
        # icon = pygame.image.load("")
        # pygame.display.set_icon(icon)
        self.score = 0
        self.wave = 0
        self.level = 0

        # initialize font
        self.font = pygame.font.SysFont("comicsansms", 95)

        # initliaze clock
        self.clock = pygame.time.Clock()
        self.current_time = 0

        # create the screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # self.screen.fill((255,0,0))

        # set background
        self.bg_img = pygame.image.load('images2/menu_v1.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))

        self.screen.blit(self.bg_img, (0, 0))
        # Loops through and adds every icon to the screen
        # self.randomizeScreen()
        print(f"\n---------\ninit!")

    def advance_level(self):
        self.wave = 0
        self.level += 1
        self.score += self.level * 100 # level bonus
        print(f"\n-------\nNEW LEVEL, level = {self.level}, score = {self.score}")

    def randomizeScreen(self):
        print("\nRandomize Screen")

        # Title and Icon
        pygame.display.set_caption("Online School Simulator")
        # icon = pygame.image.load("")
        # pygame.display.set_icon(icon)
        # initialize font
        self.font = pygame.font.SysFont("comicsansms", 95)

        # create the screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # self.screen.fill((255,0,0))

        # set background
        self.bg_img = pygame.image.load('images2/background_V1.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))


        self.screen.blit(self.bg_img, (0, 0))
        # Loops through and adds every icon to the screen
        #counts all right answers
        self.rightAnswers = 0

        # FOCUS BAR
        self.focusHeight = 1
        self.MaxFocus = pygame.draw.rect(self.screen, (255, 255, 255), (1750, 40, 150, 900))
        self.focus = pygame.draw.rect(self.screen, (0, 0, 0), (1750, 40, 150, self.focusHeight))

        # CREATE ICONS
        self.listOfIcons = self.initIcons()

        # COMPUTER SCREEN
        self.computerScreen = []
        self.compScreen = []
        self.visited = []

        # Starting position of computer screen
        self.startX = 355
        self.startY = 48

        # Width and height of every image
        self.rectWidth = 210
        self.rectHeight = 210

        for row in range(5):
            # appends row
            self.computerScreen.append([])
            self.compScreen.append([])
            self.visited.append([])
            for col in range(3):
                # chose random icon load it and then scale it
                ICON = self.listOfIcons[random.randint(0, 15)]
                tmp_image = pygame.image.load(ICON.name)
                # print(ICON.points)
                # print(self.rightAnswers)
                if ICON.points > 0:
                    self.rightAnswers += 1
                image = pygame.transform.scale(tmp_image, (self.rectWidth, self.rectHeight))

                # prints the icon to the screen
                self.screen.blit(image, (self.startX + (row * self.rectWidth), self.startY + (col * self.rectHeight)))

                # appends icon & transparent rect
                self.compScreen[row].append(ICON)
                self.visited[row].append(True)

                transRect = Rect((self.startX + (row * self.rectWidth), self.startY + (col * self.rectHeight),
                                  self.rectWidth, self.rectHeight))
                self.computerScreen[row].append(transRect)

                # displays icons
                pygame.display.update()
        pygame.display.update()
    # def removeIcon(self, col, row):

    def initIcons(self):
        return [Icon('images2/g_adobeconnect.png', 100), Icon('images2/g_sublimetext.png', 100),
                Icon('images2/g_exel.png', 25), Icon('images2/g_tophat.png', 100),
                Icon('images2/g_msteams.png', 100),
                Icon('images2/g_onenote.png', 5), Icon('images2/g_vmware.png', 100),
                Icon('images2/g_outlook.png', 100), Icon('images2/g_word.png', 50), Icon('images2/g_zoom.png', 50),
                Icon('images2/g_powerpoint.png', 100), Icon('images2/googleChrome.png', -100),
                Icon('images3/b_discord.png', -100), Icon('images3/b_facebook.png', -50),
                Icon('images3/b_instagram.png', -50),
                Icon('images3/b_music.png', -100), Icon('images3/b_netflix.png', -100),
                Icon('images3/b_reddit.png', -100), Icon('images3/b_snapchat.png', -100),
                Icon('images3/b_spotify.png', -100), Icon('images3/b_spotify.png', -100),
                Icon('images3/b_tiktok.png', -50), Icon('images3/b_twitch.png', -100),
                Icon('images3/b_twitter.png', -50), Icon('images3/b_whatsapp.png', -100),
                Icon('images3/b_youtube.png', -100),]

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text,1,color)
        textrect =textobj.get_rect()
        textrect.topleft = (x,y)
        surface.blit(textobj,textrect)

    def main_menu(self):

        pygame.mixer.music.load('78bpm gametimeee.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.15)

        while True:
            pos = pygame.mouse.get_pos()

            buttonOne = pygame.Rect(590, 300, 565, 140)
            buttonTwo = pygame.Rect(590, 500, 565, 140)

            if buttonOne.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                #self.screen.fill(0,0,0)
                self.randomizeScreen()
                self.run()
                print("clicked buttonOne")

            if buttonTwo.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                self.help_page()

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


    def help_page(self):
        pygame.mixer.music.load('78bpm gametimeee.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.15)
        self.bg_img = pygame.image.load('images2/howtoplay.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))
        self.bg_img.blit(self.bg_img, (0, 0))
        display.update()
        while True:
            pos = pygame.mouse.get_pos()

            buttonOne = pygame.Rect(590, 300, 565, 140)

            if buttonOne.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                self.main_menu()

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

    def run(self):
        pygame.mixer.music.load('78bpm gametimeee.mp3')
        # pygame.mixer.music.queue('78bpm gametimeee.mp3')
        # pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.15)

        # Game Loop
        running = True
        counter = 0
        flag = False
        while running:
            # pygame.display.update()
            pos = pygame.mouse.get_pos()
            mouse = pygame.draw.circle(self.screen, (0, 0, 0), pos, 0)

            # decrease focus
            self.current_time = pygame.time.get_ticks()
            self.focusHeight *= (1 + 0.01*self.level + 0.00005 * (self.current_time / 1000))
            # print(f"just decreased focus, focusHeight = {self.focusHeight}")
            self.focus = pygame.draw.rect(self.screen, (0, 0, 0), (1750, 40, 150, self.focusHeight))
            if self.focusHeight >= 900:
                exec(open('endgame.py').read())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("End game")

                # check whenever you click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # loop through all images constantly as game runs

                    for i in range(len(self.computerScreen)):
                        for j in range(len(self.computerScreen[i])):
                            rectImage = self.computerScreen[i][j]
                            icon = self.compScreen[i][j]
                            # check that the image is on the mouse
                            if rectImage.collidepoint(pos) and self.visited[i][j]:
                                if icon.points < 0:
                                    self.visited[i][j] = True
                                # print("clicked on a rect")
                                if icon.points > 0:
                                    self.score += icon.points
                                    counter += 1
                                    print("\tcounter" + str(counter) + "  RightAnswers" + str(self.rightAnswers))
                                    if counter == self.rightAnswers:
                                        flag = True
                                        counter = 0
                                    print(f"\ti = {i}, j = {j}, points = {icon.points}, name = {icon.name}")
                                    rec = pygame.draw.rect(self.screen, (255, 255, 255), (
                                    self.startX + (self.rectWidth * i), self.startY + (self.rectWidth * j),
                                    self.rectWidth, self.rectHeight))
                                    self.rectImage = pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 0, 0))
                                else:
                                    self.focusHeight += -icon.points
                                    # if image.points<0:
                                    #     #focus goes down

                        # if image.points<0 -> focus goes down

            pygame.display.update()
            self.clock.tick(60)
            if flag:
                self.wave += 1
                self.score += 100*self.wave
                print(f"\nwave = {self.wave}, score = {self.score}")
                if self.wave == 2:
                    self.advance_level()
                    winScreen = Win()
                    winScreen.winScreen()
                self.randomizeScreen()
                flag = False


if __name__ == '__main__':
    game = Game()
    game.main_menu()
