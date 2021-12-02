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

def draw_trunk(surface, trunk_x, trunk_y, trunk_width, trunk_height, color1):
    rect(surface, color1, (trunk_x, trunk_y, trunk_width, trunk_height))

def draw_leaves(surface, x, y, width, color2):
    circle(surface, color2, [x, y], width)
    circle(surface, "black", [x, y], width, 1)
    x = x + width*1.2
    y = y + width
    circle(surface, color2, [x, y], width)
    circle(surface, "black", [x, y], width, 1)
    x = x - width*2.4
    circle(surface, color2, [x, y], width)
    circle(surface, "black", [x, y], width, 1)
    x = x + width*1.2
    y = y + width*.9
    circle(surface, color2, [x, y], width)
    circle(surface, "black", [x, y], width, 1)
    x = x + width
    y = y + width
    circle(surface, color2, [x, y], width)
    circle(surface, "black", [x, y], width, 1)
    x = x - width*2
    circle(surface, color2, [x, y], width)
    circle(surface, "black", [x, y], width, 1)
def draw_tree(surface, x, y, width, height, color1, color2):
    trunk_width = width / 8
    trunk_height = height / 2
    trunk_x = (x + width / 2) - trunk_width / 2
    trunk_y = y + height - trunk_height
    draw_trunk(surface, trunk_x, trunk_y, trunk_width, trunk_height, color1)
    leaves_x = x + width/2
    leaves_width = width/3.5
    leaves_y = y + leaves_width
    draw_leaves(surface, leaves_x, leaves_y, leaves_width, color2)

draw_background(screen, x, y, sw, sh, 'lightblue', 'darkgreen')
draw_tree(screen, 400, 350, 150, 300, "black", "darkgreen")
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
