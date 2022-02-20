import pygame

pygame.init()
 
#create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Online School Simulator")
#icon = pygame.image.load("")
#pygame.display.set_icon(icon)
maxFocus = 500
focus = 0
#Game Loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,0,0))
    pygame.display.update()

