import pygame
from pygame.draw import *
from random import randint
import numpy as np

pygame.init()

FPS = 30
screen_size = 600
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
finished = False

Xmark_Color = (255, 0, 0)
Omarl_Color = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACK = (20, 189, 172)
FRONT = (17, 153, 139)
LINE = (35, 107, 100)
COLORS = [WHITE, BLACK]
Xmark = BLACK
Omark = WHITE
x = 0
y = 0
mat1 = np.zeros((3, 3))

def Add_mat_1(i, j):
    mat1[i, j] = 1


def Add_mat_2(i, j):
    mat1[i, j] = 2


class GameField():
    def __init__(self):
        color = COLORS
        color_new = None
        scale = screen_size / 1.5
        Xmark_image = pygame.image.load("X_Mark.png").convert_alpha()
        Xmark_image = pygame.transform.scale(Xmark_image, (scale/4, scale/4))
        Omark_image = pygame.image.load("O_Mark.png").convert_alpha()
        Omark_image = pygame.transform.scale(Omark_image, (scale/4, scale/4))
        self.scale = scale
        self.zero = scale/4
        self.b = self.scale/3
        self.color = color
        self.color_new = color_new
        self.Xmark_image = Xmark_image
        self.Omark_image = Omark_image


    def draw_Xmark(self, n1, n2):
        self.Xmark_rect = self.Xmark_image.get_rect(center=(self.zero + self.b / 2 +n1, self.zero + self.b / 2+n2))
        screen.blit(self.Xmark_image, self.Xmark_rect)

    def draw_Omark(self, n1, n2):
        self.Omark_rect = self.Omark_image.get_rect(center=(self.zero + self.b / 2+n1, self.zero + self.b / 2+n2))
        screen.blit(self.Omark_image, self.Omark_rect)

    def draw_field(self):
        pygame.draw.rect(screen, BACK, [0, 0, screen_size, screen_size])
        #pygame.draw.rect(screen, RED, [self.zero, self.zero, self.scale, self.scale])
        pygame.draw.line(screen, FRONT, (self.zero+self.b, self.zero), (self.zero+self.b, self.zero+self.scale), 5)
        pygame.draw.line(screen, FRONT, (self.zero+self.b*2, self.zero), (self.zero+self.b*2, self.zero+self.scale), 5)
        pygame.draw.line(screen, FRONT, (self.zero, self.zero+self.b), (self.zero+self.scale,self.zero+self.b), 5)
        pygame.draw.line(screen, FRONT, (self.zero, self.zero+self.b*2), (self.zero+self.scale, self.zero+self.b*2), 5)

    def rect_1(self):
        if mat1[0, 0] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self, 0, 0)
                Add_mat_1(0, 0)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self, 0, 0)
                Add_mat_2(0, 0)
                gm.Turn_Done()
        else:
            return

    def rect_2(self):
        if mat1[0, 1] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self,self.b, 0)
                Add_mat_1(0, 1)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self, self.b, 0)
                Add_mat_2(0, 1)
                gm.Turn_Done()
        else:
            return

    def rect_3(self):
        if mat1[0, 2] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self, self.b*2, 0)
                Add_mat_1(0, 2)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self, self.b*2, 0)
                Add_mat_2(0, 2)
                gm.Turn_Done()
        else:
            return

    def rect_4(self):
        if mat1[1, 0] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self, 0, self.b)
                Add_mat_1(1, 0)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self, 0, self.b)
                Add_mat_2(1, 0)
                gm.Turn_Done()
        else:
            return

    def rect_5(self):
        if mat1[1, 1] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self,self.b, self.b)
                Add_mat_1(1, 1)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self,self.b, self.b)
                Add_mat_2(1, 1)
                gm.Turn_Done()
        else:
            return

    def rect_6(self):
        if mat1[1, 2] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self, self.b*2,self.b)
                Add_mat_1(1, 2)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self, self.b*2,self.b)
                Add_mat_2(1, 2)
                gm.Turn_Done()
        else:
            return

    def rect_7(self):
        if mat1[2, 0] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self, 0,self.b*2)
                Add_mat_1(2, 0)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self, 0,self.b*2)
                Add_mat_2(2, 0)
                gm.Turn_Done()
        else:
            return

    def rect_8(self):
        if mat1[2, 1] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self, self.b,self.b*2)
                Add_mat_1(2, 1)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self, self.b,self.b*2)
                Add_mat_2(2, 1)
                gm.Turn_Done()
        else:
            return

    def rect_9(self):
        if mat1[2, 2] == 0:
            if gf.color_new == Xmark:
                GameField.draw_Xmark(self, self.b*2,self.b*2)
                Add_mat_1(2, 2)
                gm.Turn_Done()
            else:
                GameField.draw_Omark(self, self.b*2,self.b*2)
                Add_mat_2(2, 2)
                gm.Turn_Done()
        else:
            return

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

    def Win_Line_1(self):
        pygame.draw.line(screen, LINE, (self.zero, self.zero + self.b / 2), (self.zero + self.scale, self.zero + self.b / 2), 15)

    def Win_Line_2(self):
        pygame.draw.line(screen, LINE, (self.zero, self.zero + self.b * 1.5), (self.zero + self.scale, self.zero + self.b * 1.5), 15)

    def Win_Line_3(self):
        pygame.draw.line(screen, LINE, (self.zero, self.zero + self.b * 2.5), (self.zero + self.scale, self.zero + self.b * 2.5), 15)

    def Win_Line_4(self):
        pygame.draw.line(screen, LINE, (self.zero + self.b / 2, self.zero), (self.zero + self.b / 2, self.zero + self.scale), 15)

    def Win_Line_5(self):
        pygame.draw.line(screen, LINE, (self.zero + self.b * 1.5, self.zero), (self.zero + self.b * 1.5, self.zero + self.scale), 15)

    def Win_Line_6(self):
        pygame.draw.line(screen, LINE, (self.zero + self.b * 2.5, self.zero), (self.zero + self.b * 2.5, self.zero + self.scale), 15)

    def Win_Line_7(self):
        pygame.draw.line(screen, LINE, (self.zero, self.zero), (self.zero + self.scale, self.zero + self.scale), 20)

    def Win_Line_8(self):
        pygame.draw.line(screen, LINE, (self.zero, self.zero + self.scale), (self.zero + self.scale, self.zero), 20)



class GameMech():
    def __init__(self):
        turn = 1
        result = 0
        self.result = result
        self.turn = turn

    def Turn_Done(self):
        self.turn += 1
        if self.turn % 2 == 0:
            gf.color_new = Omark
        else:
            gf.color_new = Xmark

    def check_mat(self):
        c = np.diag(mat1)
        d = np.fliplr(mat1).diagonal(0)
        if c[0] == c[1] == c[2] > 0:
            self.result = c[0]
            gf.Win_Line_7()
        elif d[0] == d[1] == d[2] > 0:
            self.result = d[0]
            gf.Win_Line_8()
        for i in range(3):
            a = mat1[i, :]
            b = mat1[:, i]
            if a[0] == a[1] == a[2] > 0:
                self.result = a[0]
                if i == 0:
                    gf.Win_Line_1()
                elif i == 1:
                    gf.Win_Line_2()
                else:
                    gf.Win_Line_3()
            elif b[0] == b[1] == b[2] > 0:
                self.result = b[0]
                if i == 0:
                    gf.Win_Line_4()
                elif i == 1:
                    gf.Win_Line_5()
                else:
                    gf.Win_Line_6()




gf = GameField()
gm = GameMech()
gf.draw_field()
gf.color_new = Xmark
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            x = pos[0]
            y = pos[1]
            gf.find_rect()
            gm.check_mat()
            if gm.result == 1:
                print("Победили Крестики")
            elif gm.result == 2:
                print("Победили Нолики")



    pygame.display.update()
pygame.quit()
