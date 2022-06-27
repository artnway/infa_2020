import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 1
screen_size = 600
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
finished = False

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACK = (20, 189, 172)
FRONT = (17, 153, 139)
COLORS = [RED, BLUE, WHITE, BLACK]
Xmark = BLACK
Omark = WHITE

class GameField():
    def __init__(self):
        color = COLORS
        color_new = None
        scale = screen_size / 1.5
        turn = 1
        self.turn = turn
        self.scale = scale
        self.zero = scale/4
        self.b = self.scale/3
        self.color = color
        self.color_new = color_new


    def draw_field(self):
        pygame.draw.rect(screen, BACK, [0, 0, screen_size, screen_size])
        #pygame.draw.rect(screen, RED, [self.zero, self.zero, self.scale, self.scale])
        pygame.draw.line(screen, FRONT, (self.zero+self.b, self.zero), (self.zero+self.b, self.zero+self.scale), 5)
        pygame.draw.line(screen, FRONT, (self.zero+self.b*2, self.zero), (self.zero+self.b*2, self.zero+self.scale), 5)
        pygame.draw.line(screen, FRONT, (self.zero, self.zero+self.b), (self.zero+self.scale,self.zero+self.b), 5)
        pygame.draw.line(screen, FRONT, (self.zero, self.zero+self.b*2), (self.zero+self.scale, self.zero+self.b*2), 5)

    def rect_1(self):
        pygame.draw.rect(screen, self.color_new, [self.zero, self.zero, self.b, self.b])
        GameField.Turn_Done(self)

    def rect_2(self):
        pygame.draw.rect(screen, self.color_new, [self.zero+self.b, self.zero, self.b, self.b])
        GameField.Turn_Done(self)

    def rect_3(self):
        pygame.draw.rect(screen, self.color_new, [self.zero+self.b*2, self.zero, self.b, self.b])
        GameField.Turn_Done(self)

    def rect_4(self):
        pygame.draw.rect(screen, self.color_new, [self.zero, self.zero+self.b, self.b, self.b])
        GameField.Turn_Done(self)

    def rect_5(self):
        pygame.draw.rect(screen, self.color_new, [self.zero+self.b, self.zero+self.b, self.b, self.b])
        GameField.Turn_Done(self)

    def rect_6(self):
        pygame.draw.rect(screen, self.color_new, [self.zero+self.b*2, self.zero+self.b, self.b, self.b])
        GameField.Turn_Done(self)

    def rect_7(self):
        pygame.draw.rect(screen, self.color_new, [self.zero, self.zero+self.b*2, self.b, self.b])
        GameField.Turn_Done(self)

    def rect_8(self):
        pygame.draw.rect(screen, self.color_new, [self.zero+self.b, self.zero+self.b*2, self.b, self.b])
        GameField.Turn_Done(self)

    def rect_9(self):
        pygame.draw.rect(screen, self.color_new, [self.zero+self.b*2, self.zero+self.b*2, self.b, self.b])
        GameField.Turn_Done(self)


    def find_rect(self):
        if self.zero < x < self.zero+self.b:
            if self.zero < y < self.zero+self.b:
                GameField.rect_1(self)
            elif self.zero+self.b < y < self.zero+self.b*2:
                GameField.rect_4(self)
            elif self.zero+self.b*2 < y < self.zero+self.scale:
                GameField.rect_7(self)
        elif self.zero+self.b < x < self.zero+self.b*2:
            if self.zero < y < self.zero+self.b:
                GameField.rect_2(self)
            elif self.zero+self.b < y < self.zero+self.b*2:
                GameField.rect_5(self)
            elif self.zero+self.b*2 < y < self.zero+self.scale:
                GameField.rect_8(self)
        elif self.zero + self.b * 2 < x < self.zero + self.scale:
            if self.zero < y < self.zero+self.b:
                GameField.rect_3(self)
            elif self.zero+self.b < y < self.zero+self.b*2:
                GameField.rect_6(self)
            elif self.zero + self.b * 2 < y < self.zero + self.scale:
                GameField.rect_9(self)

    def Turn_Done(self):
        self.turn += 1
        if self.turn % 2 == 0:
            gf.color_new = Xmark
        else:
            gf.color_new = Omark


gf = GameField()
x = 0
y = 0
gf.draw_field()
gf.color_new = Omark
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            x = pos[0]
            y = pos[1]
            print(x, y)
            gf.find_rect()
            print(gf.turn)

    pygame.display.update()
pygame.quit()
