import pygame
from pygame import draw
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((850, 850))
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
        x = randint(75, 700)
        y = randint(75, 700)
        r = 25
        color = "Black"
        vx = randint(-2, 2)
        vy = randint(-2, 2)
        eye = pygame.image.load("narutomaki_001.png").convert_alpha()
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


class ScoreCounter:
    def __init__(self):
        score = 0
        level = 1
        self.score = score
        self.level = level

    def add_score(self):
        self.score = self.score + 5

    def add_level(self):
        self.level = self.level + 1

    def show_score(self):
        return self.score

    def show_level(self):
        return self.level

    def draw_level(self):
        return "Level: " + str(self.level)

    def draw_score(self):
        return "Score: " + str(self.score)

class Counter:
    def __init__(self):
        allive = ball_count
        shots = ball_count + 2
        self.shots = shots
        self.allive = allive

    def shot(self):
        self.shots = self.shots - 1

    def dead(self):
        self.allive = self.allive - 1

    def draw_shots(self):
        return "Shots: " + str(self.shots)

    def show_allive(self):
        return self.allive

    def show_shots(self):
        return self.shots


#FIXIT Где-то тут бага, шарики улетают за пределы поля в верхнем левом углу, ВРОДЕ.
def draw_objects():
    rect(screen, "black", (36, 61, 775, 775), 3)
    clock.tick(FPS)
    for b in Pool:
        b.draw()
        b.move()
        if b.x > 800 > b.y or b.x < 50 < b.y:
            b.reverse_x()
        if b.y > 800 > b.x or b.y < 75 < b.x:
            b.reverse_y()



class Screen_text_drawer:
    def __init__(self, textSurfaceObj = None, textRectObj = None):
        fontObj = pygame.font.Font("VT323-Regular.ttf", 50)
        self.fontObj = fontObj

    def screen_score(self):
        self.textScore = self.fontObj.render(ss.draw_score(), True, "black")
        self.textScoreRect = self.textScore.get_rect()
        self.textScoreRect.center = (110, 25)

    def screen_shots(self):
        self.textShots = self.fontObj.render(s.draw_shots(), True, "black")
        self.textShotsRect = self.textShots.get_rect()
        self.textShotsRect.center = (700, 25)

    def screen_level(self):
        self.textLevel = self.fontObj.render(ss.draw_level(), True, "black")
        self.textLevelRect = self.textLevel.get_rect()
        self.textLevelRect.center = (350, 25)

    def screen_game_over(self):
        self.textGameover = self.fontObj.render("Game Over", True, "black")
        self.textGemeoverRect = self.textGameover.get_rect()
        self.textGemeoverRect.center = (110, 25)

    def screen_double_kill(self):
        self.textDoublekill = self.fontObj.render("Double Kill!", True, "black")
        self.textDoublekillRect = self.textDoublekill.get_rect()
        self.textDoublekillRect.center = (110, 25)


    def screen_draw_counters(self):
        screen.blit(self.textScore, self.textScoreRect)
        screen.blit(self.textShots, self.textShotsRect)
        screen.blit(self.textLevel, self.textLevelRect)

def game_loop():
    finished = False
    while not finished:
        ssr = Screen_text_drawer()
        ssr.screen_score()
        ssr.screen_shots()
        ssr.screen_level()
        ssr.screen_draw_counters()
        draw_objects()
        for event in pygame.event.get():
            for b in Pool:
                if event.type == pygame.QUIT or s.allive < 1:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    r = b.click()[0]
                    n = sqrt(sq(b.click()[1] - (event.pos[0])) + sq(b.click()[2] - (event.pos[1])))
                    if r > n > -r:
                        b.dead()
                        s.dead()
                        ss.add_score()
                        print(s.allive)
            if event.type == pygame.QUIT or s.shots < 1:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                s.shot()
        pygame.display.update()
        screen.fill("white")
        back = pygame.image.load("maxresdefault_2.jpg").convert_alpha()
        back_rect = back.get_rect(center=(425, 450))
        screen.blit(back, back_rect)


ss = ScoreCounter()
gameround = False
while gameround is False:
    s = Counter()
    Pool = make_pool()
    game_loop()
    ss.add_level()
    for i in range(s.show_shots()):
        ss.score += 1
    if s.allive < 1:
        print("Новый раунд")
        gameround = False
    else:
        gameround = True
print("Вы набрли:", ss.show_score(), "очков!")
pygame.quit()



"""Доделать раунды: старт, гейм овер. Сделать дабл и трипл килл, мб бонусный раунд с шеренганами."""


