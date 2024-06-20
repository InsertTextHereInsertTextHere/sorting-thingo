"""import pygame
import math
import random


# check quit button
def isQuit():
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# swapping function
def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    redRects.append(pos1)
    redRects.append(pos2)


def draw():
    # fill the screen with a color to wipe away anything from last frame
    window.fill("black")
    # draw bar graph
    i = 0
    for item in arr:
        pygame.draw.rect(
            window,
            "red" if i in redRects else "white",
            (i * rectWidth, window.get_height() - item, math.ceil(rectWidth), item),
        )
        i += 1
    pygame.display.flip()


# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

arr = []
for i in range(1, 721):
    arr.append(i)
arrLen = len(arr)
rectWidth = window.get_width() / arrLen
redRects = []


while running:
    # Swap random items

    for j in range(0, 100):
        redRects = []
        swap(arr, j, random.randint(j + 1, arrLen - 1))
        draw()
    for I in range(0, arrLen):
        for II in range(0, arrLen - I - 1):
            if arr[II] > arr[II + 1]:
                redRects = []
                swap(arr, II, II + 1)
        draw()

pygame.quit()
"""

import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Sorting algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield j


# Quicksort with yield
def quicksort(arr, low, high):
    if low < high:
        pi = yield from partition(arr, low, high)
        yield from quicksort(arr, low, pi - 1)
        yield from quicksort(arr, pi + 1, high)
    yield arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield [i, j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield [i + 1, high]
    return i + 1


# Drawing function
def draw_array(arr, highlight1=None, highlight2=None, swapped=False):
    screen.fill(BLACK)
    bar_width = screen_width // len(arr)
    for i in range(len(arr)):
        color = (
            GREEN
            if swapped and (i == highlight1 or i == highlight2)
            else RED if i == highlight1 or i == highlight2 else WHITE
        )
        pygame.draw.rect(
            screen, color, (i * bar_width, screen_height - arr[i], bar_width, arr[i])
        )
    pygame.display.flip()


# Generate array
arr = [random.randint(0, screen_height) for _ in range(1000)]
sorting = quicksort(arr, 0, len(arr) - 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    try:
        J = next(sorting)
        draw_array(arr, J[0], J[1])
    except StopIteration:
        running = False

    pygame.time.delay(0)  # Delay to control the speed of the visualization

pygame.quit()
