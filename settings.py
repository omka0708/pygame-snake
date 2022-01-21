import random
import pickle

RES = 650
FPS = 60
CELL = 25
SPEED = 10

bonus_speed = 0
bonus_cell = 0

section = {'menu': True, 'game_loop': False}
menu_section = {'main': True, 'choosing_colors': False, 'choosing_cell': False}

navbar_num = 1
snake_color = 'green'
emerald_color = 'green'
pattern_name = 'gf'

field = [[0 for _ in range(0, RES, CELL)] for _ in range(0, RES, CELL)]

show_emerald = False
is_pause = False
sound_on = True

score = 0
with open('data.pickle', 'rb') as f:
    high_score = pickle.load(f)


def get_random_free_index():
    free_indexes = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 0:
                free_indexes.append((j * CELL, i * CELL))
    if free_indexes:
        free_indx = random.choice(free_indexes)
    else:
        free_indx = (-CELL, -CELL)
    return free_indx

# def init_all(num):
#     global CELL, SPEED, section, navbar_num, snake_color, emerald_color, \
#         pattern_name, field, show_emerald, is_pause, sound_on, score, choosed
#
#     section = {'menu': True, 'game_loop': False, 'settings': False}
#
#     if num:
#         navbar_num = 1
#         snake_color = 'purple'
#         emerald_color = 'orange'
#         pattern_name = 'gf'
#     else:
#         navbar_num = 2
#         snake_color = 'green'
#         emerald_color = 'green'
#         pattern_name = 'sd'
#
#     field = [[0 for _ in range(0, RES, CELL)] for _ in range(0, RES, CELL)]
#     show_emerald = False
#     is_pause = False
#     choosed = False
#
#     score = 0
