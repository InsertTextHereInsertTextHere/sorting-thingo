# This is the sorting algorithmn visualiser

# This version of Sorting Algoritmhn visualiser is the exact same as:
# None

import pygame
from sys import exit

pygame.init()
screenWidth = 960
screenHeight = 540

mainWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Sorting Moment")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
