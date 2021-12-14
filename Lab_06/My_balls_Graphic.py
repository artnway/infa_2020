import pygame
from pygame import draw
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
finished = False
ball_count = randint(5, 9)


def sq(n):
    return int(n) ** 2


def sqrt(n):
    return int(n)**0.5


def pool_item(n=None):
    for i in n:
        return i


def make_pool():
    items = [Ball() for i in range(ball_count)]
    return items


class Ball:
    def __init__(self, x=0, y=0, r=0, color=None, vx=0, vy=0, eye=0, eye_rect=0, items=0):
        x = randint(30, 725)
        y = randint(30, 725)
        r = 25
        color = "Black"
        vx = randint(-2, 2)
        vy = randint(-2, 2)
        eye = pygame.image.load("Eye_001.png").convert_alpha()
        eye = pygame.transform.scale(eye, (r*2, r*2))
        self.vy = vy
        self.vx = vx
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.eye = eye
        self.eye_rect = eye_rect
        self.items = items

    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def reverse_x(self):
        self.vx = self.vx * -1

    def reverse_y(self):
        self.vy = self.vy * -1

    def draw(self):
        self.eye_rect = self.eye.get_rect(center=(self.x, self.y))
        screen.blit(self.eye, self.eye_rect)

    def click(self):
        return self.r, self.x, self.y

    def dead(self):
        self.x = self.y = -100
        self.vx = self.vy = 0


class Counter:
    def __init__(self, n=0):
        allive = ball_count
        shots = ball_count + 2
        self.shots = shots
        self.allive = allive
        self.score = n

    def shot(self):
        self.shots = self.shots - 1

    def add_point(self):
        self.score = self.score + 5

    def dead(self):
        self.allive = self.allive - 1

    def show_score(self):
        return self.score

    def show_allive(self):
        return self.allive

    def show_shots(self):
        return self.shots


class Manager:
    finished = False

    def main_move(self):
        for b in Pool:
            b.draw()
            b.move()
            if b.x > 749 > b.y or b.x < 26 < b.y:
                b.reverse_x()
            if b.y > 749 > b.x or b.y < 26 < b.x:
                b.reverse_y()

    def if_allive(self, finished=None):
        self.finished = finished
        if event.type == pygame.QUIT or s.allive < 1 or s.shots < 1:
            self.finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            r = b.click()[0]
            n = sqrt(sq(b.click()[1] - (event.pos[0])) + sq(b.click()[2] - (event.pos[1])))
            if r > n > -r:
                b.dead()
                s.dead()
                s.add_point()
                print('В точку!')
                print("Осталось ", s.allive, "шарика.")

    def if_empty(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            s.shot()
            print("Осталось ", s.show_shots(), "выстрелов.")


s = Counter()
m = Manager()
Pool = make_pool()
ip = pool_item(Pool)
while not m.finished:
    rect(screen, "black", (25, 25, 725, 725), 3)
    clock.tick(FPS)
    m.main_move()
    for event in pygame.event.get():
        for b in Pool:
            m.if_allive()
        m.if_empty()
    pygame.display.update()
    screen.fill("white")

"""Сделать раунды: старт, гейм овер. Сделать отображение кол-ва выстрелов, кол-ва очков,
и прикрутить прицел на мышку."""

pygame.quit()

if s.shots > 0:
    for i in range(s.shots):
        s.add_point()
    print("Вы набрли:", s.show_score(), "очков!")
else:
    print("Вы набрли:", s.show_score(), "очков!")
