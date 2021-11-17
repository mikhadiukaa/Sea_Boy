import pygame
from pygame.constants import MOUSEBUTTONDOWN
from pygame.draw import *
import math
from random import randint

pygame.init()
FPS = 100
screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Sea Battle")

button_exit_coord = [[(907,10),(100,100)]]
button_settings_coord = [[(907,110),(100,100)]]
button_play_coord = [[(441,385),(127,143)],[(320,342),(360,108)],[(320,450),(360,108)]]

_menu_ = pygame.image.load('menu_game.png')
menu_rect = _menu_.get_rect(bottomright = (1000,900))
_button_exit = pygame.image.load('button_exit.png')
button_exit_rect = _button_exit.get_rect(bottomright = (1000,900))
_button_play = pygame.image.load('button_play.png')
button_play_rect = _button_play.get_rect(bottomright = (1000,900))
_button_settings = pygame.image.load('button_settings.png')
button_settings_rect = _button_settings.get_rect(bottomright = (1000,900))

_question_about_gamemode = pygame.image.load('question_about_gamemode.png')
_question_about_gamemode_rect = _question_about_gamemode.get_rect(bottomright = (1000,900))
_answer_1 = pygame.image.load('quest_1.png')
answer_1_rect = _answer_1.get_rect(bottomright = (1000,900))
_answer_2 = pygame.image.load('quest_2.png')
answer_2_rect = _answer_2.get_rect(bottomright = (1000,900))

def menu_static_background():
    screen.blit(_menu_,menu_rect)
def menu_dinamic_background(flag):
    if (flag == 1) : screen.blit(_button_exit,button_exit_rect)
    if (flag == 2) : screen.blit(_button_play,button_play_rect)
    if (flag == 3) : screen.blit(_button_settings,button_settings_rect)

def static_question_about_gamemode():
    screen.blit(_question_about_gamemode,_question_about_gamemode_rect)
def dinamic_question_about_gamemode(flag):
    if (flag == 1) : screen.blit(_answer_1,answer_1_rect)
    elif (flag == 2) : screen.blit(_answer_2,answer_2_rect) 


def _button(x, y, coord):
    return(int(x >= coord[0][0] and x <= coord[0][0] + coord[1][0] and y >= coord[0][1] and y <= coord[0][1] + coord[1][1]))

def text(x, y, A, color, size):
    pygame.font.init()
    myfont = pygame.font.SysFont(' ', size)
    textsurface = myfont.render(A, False, color)
    screen.blit(textsurface, (x, y))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

gamemode = 0
level_background = 0
ai_on_flag = 1
localisation_language = 'Russian' 

menu_static_background()

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if (level_background == 0):
            if (event.type == pygame.MOUSEMOTION):
                if (_button(event.pos[0],event.pos[1],button_exit_coord[0])):
                    menu_dinamic_background(1)
                elif (_button(event.pos[0],event.pos[1],button_play_coord[0])):
                    menu_dinamic_background(2)
                elif (_button(event.pos[0],event.pos[1],button_settings_coord[0])):
                    menu_dinamic_background(3)
                else:
                    menu_static_background()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (_button(event.pos[0],event.pos[1],button_exit_coord[0])):

                    finished == True
                    
                elif (_button(event.pos[0],event.pos[1],button_play_coord[0])):
                    level_background = 1
                    static_question_about_gamemode()

                elif (_button(event.pos[0],event.pos[1],button_settings_coord[0])):
                    level_background = -1

        elif (level_background == 1):
            if (event.type == pygame.MOUSEMOTION):
                if (_button(event.pos[0],event.pos[1],button_play_coord[1])):
                    dinamic_question_about_gamemode(1)
                elif (_button(event.pos[0],event.pos[1],button_play_coord[2])):
                    dinamic_question_about_gamemode(2)
                else:
                    static_question_about_gamemode()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (_button(event.pos[0],event.pos[1],button_play_coord[1])):
                    level_background = 2
                    gamemode = 0

                elif (_button(event.pos[0],event.pos[1],button_play_coord[2])):
                    level_background = 2
                    gamemode = 1
            
    pygame.display.update()

pygame.quit()