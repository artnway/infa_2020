import pygame
from pygame.draw import *

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
    sky_x = x
    sky_y = y
    sky_height = height / 2
    sky_width = width
    rect(surface, color1, (sky_x, sky_y, sky_width, sky_height))
    # sun:
    x = cent + 250
    y = cent - 250
    circle(surface, "orange", (x, y), 50)

    cloud_width = sky_width/4
    cloud_height = sky_height / 4
    cloud_x = sky_x + cloud_width
    cloud_y = sky_y + cloud_height
    draw_clouds(surface, cloud_x, cloud_y, cloud_width, cloud_height, 'white')
    draw_clouds(surface, 50, 100, cloud_width, 50, 'white')
    draw_clouds(surface, 650, 200, cloud_width, cloud_height, 'white')


def draw_clouds(surface, cloud_x, cloud_y, cloud_width, cloud_height, color1):
    element_radius = cloud_height/3
    element_y = cloud_y + element_radius
    element_x = cloud_x + element_radius
    draw_cloud_element(surface, element_x, element_y, element_radius, color1)


def draw_cloud_element(surface, element_x, element_y, element_radius, color1):
    element_y = element_y + element_radius
    for i in range(4):
        circle(surface, color1, [element_x, element_y], element_radius)
        circle(surface, 'black', [element_x, element_y], element_radius, 1)
        element_x = element_x + element_radius
    element_y = element_y - element_radius
    element_x = element_x - element_radius*3
    for i in range(2):
        circle(surface, color1, [element_x, element_y], element_radius)
        circle(surface, 'black', [element_x, element_y], element_radius, 1)
        element_x = element_x + element_radius


def draw_base(surface, x, y, width, base_height, color1):
    rect(surface, color1, (x, y, width, base_height))
    rect(surface, "black", (x, y, width, base_height), 2)


def draw_walls(surface, walls_x, walls_y, walls_width, walls_height, color2):
    rect(surface, color2, (walls_x, walls_y, walls_width, walls_height))
    rect(surface, "black", (walls_x, walls_y, walls_width, walls_height), 2)


def draw_window(surface, window_x, window_y, window_width, window_height, color3):
    rect(surface, color3, (window_x, window_y, window_width, window_height))
    rect(surface, "#583F29", (window_x, window_y, window_width, window_height), 2)
    line1_start_x = window_x
    line1_start_y = window_y + window_height/2
    line1_end_x = line1_start_x + window_width
    line1_end_y = line1_start_y
    line(surface, "#583F29", (line1_start_x, line1_start_y), (line1_end_x, line1_end_y), 3)
    line2_start_x = window_x + window_width/2
    line2_start_y = window_y
    line2_end_x = line2_start_x
    line2_end_y = line2_start_y + window_height
    line(surface, "#583F29", (line2_start_x, line2_start_y), (line2_end_x, line2_end_y), 3)


def draw_roof(surface, roof_x, roof_y, roof_width, roof_height, color4):
    x3 = roof_x
    y3 = roof_y
    x1 = roof_x + roof_width
    y1 = roof_y
    x2 = roof_x + roof_width/2
    y2 = roof_y - roof_height
    polygon(surface, color4, [(x1, y1), (x2, y2), (x3, y3)], 0)
    polygon(surface, "black", [(x1, y1), (x2, y2), (x3, y3)], 2)


def draw_house(surface, x, y, house_width, house_height, color1, color2, color3, color4):
    tree_width = house_width / 2
    tree_height = house_height - house_height / 4
    tree_x = x + house_width
    tree_y = y - house_height * .8
    draw_tree(surface, tree_x, tree_y, tree_width, tree_height, "black", 'darkgreen')

    base_width = house_width
    base_height = house_height * 0.05
    round(base_height)
    draw_base(surface, x, y, base_width, base_height, color1)

    walls_width = house_width * .95
    round(walls_width)
    walls_height = house_height * .6
    round(walls_height)
    walls_y = y - walls_height
    walls_x = x + (house_width - walls_width) / 2
    draw_walls(surface, walls_x, walls_y, walls_width, walls_height, color2)

    window_width = house_width * .25
    round(window_width)
    window_height = walls_height * .4
    round(window_height)
    window_y = walls_y + walls_height*0.25
    window_x = walls_x + walls_width*0.5 - window_width*0.5
    draw_window(surface, window_x, window_y, window_width, window_height, color3)

    roof_width = house_width
    roof_height = house_height - walls_height - base_height
    roof_x = x
    roof_y = y - walls_height
    draw_roof(surface, roof_x, roof_y, roof_width, roof_height, color4)


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


def draw_tree(surface, tree_x, tree_y, tree_width, tree_height, color1, color2):
    trunk_width = tree_width / 8
    trunk_height = tree_height / 2
    trunk_x = (tree_x + tree_width / 2) - trunk_width / 2
    trunk_y = tree_y + tree_height - trunk_height
    draw_trunk(surface, trunk_x, trunk_y, trunk_width, trunk_height, color1)
    leaves_x = tree_x + tree_width/2
    leaves_width = tree_width/3.5
    leaves_y = tree_y + leaves_width
    draw_leaves(surface, leaves_x, leaves_y, leaves_width, color2)




draw_background(screen, x, y, sw, sh, 'lightblue', 'darkgreen')
draw_house(screen, 100, 700, 300, 400, 'darkgrey', 'brown', 'lightblue', 'darkred')
draw_house(screen, 600, 500, 75, 100, 'darkgrey', 'brown', 'lightblue', 'darkred')



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
