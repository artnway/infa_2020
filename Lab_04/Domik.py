import pygame
from pygame.draw import *
import house

pygame.init()

FPS = 30

sh = 900  # screen_height
sw = 900   # screen_width
cent = 450  # centre
x = 0
y = 0
screen = pygame.display.set_mode((sw, sh))


def draw_background(surface, x, y, width, height, color1, color2):
    # grass:
    rect(surface, color2, (x, y, width, height))
    # sky:
    height /= 2
    rect(surface, color1, (x, y, width, height))
    # sun:
    x = cent + 250
    y = cent - 250
    circle(surface, "orange", (x, y), 50)


draw_background(screen, x, y, sw, sh, 'lightblue', 'darkgreen')

house.draw_house(screen, 100, 700, 300, 400, 'darkgrey', 'brown', 'lightblue', 'darkred')
house.draw_house(screen, 600, 500, 75, 100, 'darkgrey', 'brown', 'lightblue', 'darkred')
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
