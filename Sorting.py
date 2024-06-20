# This is the sorting algorithmn visualiser
# Version alpha 1.0

import pygame

pygame.init()
screenWidth = 960
screenHeight = 540

mainWindow = pygame.display.set_mode((screenWidth, screenHeight))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
