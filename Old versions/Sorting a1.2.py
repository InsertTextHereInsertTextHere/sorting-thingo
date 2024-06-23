# This is the sorting algorithmn visualiser

# This version of Sorting Algoritmhn visualiser is the exact same as:
# Version Alpha 1.0
# Version Alpha 1.1

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
