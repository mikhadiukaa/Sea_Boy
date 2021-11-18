import pygame
from pygame.draw import *
import math
from random import randint

pygame.init()
FPS = 100
screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("Sea Battle")

button_exit_coord = [[(907,10),(100,100)],[(220,420),(550,55)],[(220,480),(550,55)]]
button_settings_coord = [[(907,110),(100,100)]]
button_play_coord = [[(441,385),(127,143)],[(320,342),(360,108)],[(320,450),(360,108)]]
button_ship_select_coord = [[(723,169),(200,50)],[(723,268),(150,50)],[(723,368),(100,50)],[(723,466),(100,50)]]
map_ = [[(100,100),(500,500)],[(200,200),(200,200)],[(175,175),(350,350)],[(150,150),(400,400)],[(125,125),(450,450)]]
BLACK = (0,0,0)
WHITE = (255,255,255)

_exit_button = pygame.image.load('exit_button.png')
exit_button_rect = _exit_button.get_rect(bottomright = (1000,105))

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

_selection_ships = pygame.image.load('selection_of_ships.png')
selection_rect = _selection_ships.get_rect(bottomright = (1000,900))

_quit_question_ = pygame.image.load('question_quit.png')
quit_question_rect = _quit_question_.get_rect(bottomright = (850,590))
_answer_3 = pygame.image.load('quest_3.png')
answer_3_rect_1 = _answer_3.get_rect(bottomright = (850-75-3,480))
answer_3_rect_2 = _answer_3.get_rect(bottomright = (850-75-2,550))

ship_1 = pygame.image.load('battleship_x.png')
ship_2 = pygame.image.load('heavy_cruiser_x.png')
ship_3 = pygame.image.load('light_cruiser_x.png')
ship_4 = pygame.image.load('destroyer_x.png')

bn_ship_1 = pygame.image.load('button_ship_1.png')
bn_ship_1_rect =  bn_ship_1.get_rect(bottomleft = (723,219))
bn_ship_2 = pygame.image.load('button_ship_2.png')
bn_ship_2_rect =  bn_ship_2.get_rect(bottomleft = (723,318))
bn_ship_3 = pygame.image.load('button_ship_3.png')
bn_ship_3_rect =  bn_ship_3.get_rect(bottomleft = (723,418))
bn_ship_4 = pygame.image.load('button_ship_4.png')
bn_ship_4_rect =  bn_ship_4.get_rect(bottomleft = (723,516))
image_ship = [bn_ship_1,ship_1,ship_2,ship_3,ship_4]

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

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

def static_selection_of_ships():
    screen.blit(_selection_ships,selection_rect)
    battleground(100,100,500)
    for i in range(0,400,100):
        text(950,170 + i, str(ship_catalog[i//100]),BLACK,64)
def dinamic_selection_of_ships(flag):
    if (flag == 1): screen.blit(_exit_button,exit_button_rect)
    elif (flag == 2) : screen.blit(bn_ship_1,bn_ship_1_rect)
    elif (flag == 3) : screen.blit(bn_ship_2,bn_ship_2_rect)
    elif (flag == 4) : screen.blit(bn_ship_3,bn_ship_3_rect)
    elif (flag == 5) : screen.blit(bn_ship_4,bn_ship_4_rect)
    elif (flag == 6) : screen.blit(rot_ship,rot_ship_rect)

def static_question_about_quit():
    screen.blit(_quit_question_,quit_question_rect)
def dinamic_question_about_quit(flag):
    if (flag == 1): screen.blit(_answer_3,answer_3_rect_1)
    elif (flag == 2): screen.blit(_answer_3,answer_3_rect_2)
#semi-servise_function
def battleground(x,y,n):

    for i in range(0,n + n//10,n//10):

        line(screen,BLACK,(x+i,y),(x+i,y+n),5)
        line(screen,BLACK,(x,y+i),(x+n,y+i),5)
#servise_functions
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
flag_quit = 0
localisation_language = 'Russian' 
ship_catalog = [1,2,3,4]

battleground_1, battleground_2 = [['0'] * 12] * 12 , [['0'] * 12] * 12

menu_static_background()


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or flag_quit == 1:
            finished = True
        if (level_background == 0): #MENU
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
                    flag_quit = 1
                elif (_button(event.pos[0],event.pos[1],button_play_coord[0])):
                    level_background = 1
                    static_question_about_gamemode()

                elif (_button(event.pos[0],event.pos[1],button_settings_coord[0])):
                    level_background = -1

        elif (level_background == 1):#GAMEMODE
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
                    ship_catalog = [1,2,3,4]
                    flag_choice = 0
                    angle = 0
                    static_selection_of_ships()

                elif (_button(event.pos[0],event.pos[1],button_play_coord[2])):
                    level_background = 2
                    gamemode = 1
                    flag_choice = 0
                    angle = 0
                    ship_catalog = [1,2,3,4]
                    static_selection_of_ships()

        elif (level_background == 2): #SELECT SHIPS
            if (gamemode == 0):
                if (event.type == pygame.MOUSEMOTION):
                    fl = True
                    if (_button(event.pos[0],event.pos[1],button_exit_coord[0])):
                        dinamic_selection_of_ships(1)
                        fl = False
                    if (flag_choice == 0):
                        for i in range(0,4):
                            if (_button(event.pos[0],event.pos[1],button_ship_select_coord[i])):
                                dinamic_selection_of_ships(i+2)
                                fl = False
                        if (fl): static_selection_of_ships()
                    else:
                        if (_button(event.pos[0],event.pos[1],map_[flag_choice])):
                            rot_ship,rot_ship_rect = rot_center(image_ship[flag_choice],angle,event.pos[0],event.pos[1])
                            dinamic_selection_of_ships(6)
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    print(angle)
                    if (_button(event.pos[0],event.pos[1],button_exit_coord[0])):
                        level_background = 3
                        static_question_about_quit()
                    else:
                        if flag_choice == 0:
                            for i in range(4):
                                if (_button(event.pos[0],event.pos[1],button_ship_select_coord[i])):
                                    if (ship_catalog[i] > 0):
                                        ship_catalog[i] -= 1
                                        flag_choice = i + 1
                                    static_selection_of_ships()
                        else:
                            if (event.button == 2):
                                ship_catalog[flag_choice-1] += 1
                                flag_choice = 0
                                angle = 0
                            elif (event.button == 3):
                                angle += 90

        elif (level_background == 3):
            if (event.type == pygame.MOUSEMOTION):
                if (_button(event.pos[0],event.pos[1],button_exit_coord[1])):
                    dinamic_question_about_quit(1)
                elif (_button(event.pos[0],event.pos[1],button_exit_coord[2])):
                    dinamic_question_about_quit(2)    
                else:
                    static_question_about_quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if (_button(event.pos[0],event.pos[1],button_exit_coord[1])):
                    level_background = 0
                    menu_static_background()
                elif (_button(event.pos[0],event.pos[1],button_exit_coord[2])):
                    flag_quit = 1

    pygame.display.update()

pygame.quit()
