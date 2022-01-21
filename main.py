import random
import sys
import pygame
import controls
import settings
from apple import Apple
from button import Button
from emerald import Emerald
from info import Info
from snake import Snake


def set_default():
    global snake, apple, emerald, info, navbar_img, pattern, image_field, buttons
    settings.field = [[0 for _ in range(0, settings.RES, settings.CELL)] for _ in range(0, settings.RES, settings.CELL)]
    settings.is_pause = False
    settings.score = 0
    snake = Snake(game_surface, settings.snake_color)
    apple = Apple(game_surface)
    emerald = Emerald(game_surface, settings.emerald_color)
    info = Info(navbar)

    for button in buttons.values():
        button.choosed = False

    navbar_img = pygame.image.load(f"img/navbar/navbar_{settings.navbar_num}.png")
    pattern = [
        pygame.transform.scale(pygame.image.load(f"img/{settings.pattern_name}/{settings.pattern_name}{i + 1}.png"),
                               (settings.CELL, settings.CELL)) for i in range(14)]
    image_field = []
    for i in range(0, settings.RES // settings.CELL):
        image_field.append([])
        for j in range(0, settings.RES // settings.CELL):
            image_field[i].append(random.choice(pattern))


def b_pause():
    settings.is_pause = not settings.is_pause


def b_sound():
    settings.sound_on = not settings.sound_on


def b_goto_choosing_color():
    settings.menu_section = {'main': False, 'choosing_colors': True, 'cell_speed': False}


def go_back_to_menu():
    settings.section = {'menu': True, 'game_loop': False}
    settings.menu_section = {'main': True, 'choosing_colors': False, 'cell_speed': False}


def go_back_cell_speed():
    for button in buttons.values():
        button.choosed = False
    settings.section = {'menu': True, 'game_loop': False}
    settings.menu_section = {'main': False, 'choosing_colors': True, 'cell_speed': False}


def choose_color_1():
    settings.navbar_num = 1
    settings.snake_color = 'purple'
    settings.emerald_color = 'orange'
    settings.pattern_name = 'gf'
    b_goto_cell_speed()


def choose_color_2():
    settings.navbar_num = 2
    settings.snake_color = 'green'
    settings.emerald_color = 'green'
    settings.pattern_name = 'sd'
    b_goto_cell_speed()


def b_goto_cell_speed():
    settings.menu_section = {'main': False, 'choosing_colors': False, 'cell_speed': True}


def choose_cell_26():
    global buttons
    buttons['menu_ccell_srf_b0'].choosed = True
    buttons['menu_ccell_srf_b1'].choosed = False
    settings.CELL = 25
    settings.bonus_cell = 3


def choose_cell_13():
    global buttons
    buttons['menu_ccell_srf_b0'].choosed = False
    buttons['menu_ccell_srf_b1'].choosed = True
    settings.CELL = 50
    settings.bonus_cell = 1


def choose_speed_slow():
    global buttons
    buttons['menu_ccell_srf_b2'].choosed = True
    buttons['menu_ccell_srf_b3'].choosed = False
    buttons['menu_ccell_srf_b4'].choosed = False
    settings.SPEED = 14
    settings.bonus_speed = 1


def choose_speed_normal():
    global buttons
    buttons['menu_ccell_srf_b2'].choosed = False
    buttons['menu_ccell_srf_b3'].choosed = True
    buttons['menu_ccell_srf_b4'].choosed = False
    settings.SPEED = 8
    settings.bonus_speed = 2


def choose_speed_fast():
    global buttons
    buttons['menu_ccell_srf_b2'].choosed = False
    buttons['menu_ccell_srf_b3'].choosed = False
    buttons['menu_ccell_srf_b4'].choosed = True
    settings.SPEED = 5
    settings.bonus_speed = 4


def start_game():
    global buttons
    if any([buttons['menu_ccell_srf_b2'].choosed, buttons['menu_ccell_srf_b3'].choosed,
            buttons['menu_ccell_srf_b4'].choosed]) \
            and any([buttons['menu_ccell_srf_b0'].choosed, buttons['menu_ccell_srf_b1'].choosed]):
        set_default()
        settings.section = {'menu': False, 'game_loop': True}
        settings.menu_section = {'main': True, 'choosing_colors': False, 'cell_speed': False}


pygame.init()
screen = pygame.display.set_mode((settings.RES, settings.RES + 100), flags=pygame.NOFRAME)
img_icon = pygame.image.load("img/icons/icon.png")
pygame.display.set_icon(img_icon)
clock = pygame.time.Clock()

menu_surface = pygame.Surface((settings.RES, settings.RES + 100))
menu_background_img = pygame.transform.scale(pygame.image.load("img/menu/menu_background.png"),
                                             menu_surface.get_size())
middle_block = pygame.Surface((300, 400))
middle_block.set_alpha(100)

game_surface = pygame.Surface((settings.RES, settings.RES))
navbar = pygame.Surface((settings.RES, 100))

pause_surface = pygame.Surface((300, 500))
pause_surface.set_alpha(100)

snake = None
apple = None
emerald = None
info = None

navbar_img = None
pattern = None
image_field = None

img_buttons = {
    'pause_icon': pygame.image.load("img/icons/pause_icon.png"),
    'sound_on': pygame.image.load("img/icons/sound_on_icon.png"),
    'sound_off': pygame.image.load("img/icons/sound_off_icon.png"),
    'first_color': pygame.image.load("img/menu/first_color.png"),
    'second_color': pygame.image.load("img/menu/second_color.png"),
    'back': pygame.image.load("img/icons/back_icon.png")
}

buttons = {
    'pause_srf_b0': Button(screen, (screen.get_rect().w // 2, screen.get_rect().h // 2), b_pause, (50, 50),
                           img=img_buttons['pause_icon']),
    'pause_srf_b1': Button(screen, (screen.get_rect().w // 2, screen.get_rect().h // 2 + 150), go_back_to_menu,
                           (50, 50),
                           img=img_buttons['back']),
    'navbar_srf_b0': Button(navbar, (75, navbar.get_rect().h // 2), b_pause, (35, 35),
                            img=img_buttons['pause_icon']),
    'navbar_srf_b1': Button(navbar, (125, navbar.get_rect().h // 2), b_sound, (35, 35),
                            img=img_buttons['sound_on']),
    'menu_mb_srf_b0': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 - 100),
                             b_goto_choosing_color, text="START", font_size=26),
    'menu_mb_srf_b1': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 + 150),
                             b_sound, (40, 40),
                             img=img_buttons['sound_on']),
    'menu_mb_srf_b2': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 + 100),
                             sys.exit, text="QUIT", font_size=26),
    'menu_ccolor_srf_b2': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 - 100),
                                 choose_color_2, (280, 180), img=img_buttons['first_color']),
    'menu_ccolor_srf_b3': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 + 100),
                                 choose_color_1, (280, 180), img=img_buttons['second_color']),
    'menu_ccolor_srf_b4': Button(menu_surface,
                                 (menu_surface.get_rect().w // 2 - 175, menu_surface.get_rect().h // 2 + 175),
                                 go_back_to_menu, (40, 40),
                                 img=img_buttons['back']),
    'menu_ccell_srf_b0': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 - 135),
                                choose_cell_26, text="26x26", font_size=20, choosing=True),
    'menu_ccell_srf_b1': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 - 100),
                                choose_cell_13, text="13x13", font_size=20, choosing=True),
    'menu_ccell_srf_b2': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 + 50),
                                choose_speed_slow, text="SLOW", font_size=20, choosing=True),
    'menu_ccell_srf_b3': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 + 75),
                                choose_speed_normal, text="NORMAL", font_size=20, choosing=True),
    'menu_ccell_srf_b4': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 + 100),
                                choose_speed_fast, text="FAST", font_size=20, choosing=True),
    'menu_ccell_srf_b5': Button(menu_surface,
                                (menu_surface.get_rect().w // 2 - 175, menu_surface.get_rect().h // 2 + 175),
                                go_back_cell_speed, (40, 40),
                                img=img_buttons['back']),
    'menu_ccell_srf_b6': Button(menu_surface, (menu_surface.get_rect().w // 2, menu_surface.get_rect().h // 2 + 155),
                                start_game, text="GO!", font_size=18)

}


def run():
    while True:
        clock.tick(settings.FPS)
        pygame.display.set_caption(f"FPS: {int(clock.get_fps())} Snake")
        if settings.section['menu']:
            screen.blit(menu_surface, (0, 0))
            controls.events(snake, buttons)
            controls.menu_update(menu_surface, middle_block, menu_background_img, buttons, img_buttons)
            # buttons handler
            if settings.menu_section['main']:
                for key in buttons:
                    buttons[key].active = 'menu_mb_' in key
            elif settings.menu_section['choosing_colors']:
                for key in buttons:
                    buttons[key].active = 'menu_ccolor_' in key
            elif settings.menu_section['cell_speed']:
                for key in buttons:
                    buttons[key].active = 'menu_ccell_' in key

        elif settings.section['game_loop']:
            screen.blit(navbar, (0, 0))
            screen.blit(game_surface, (screen.get_rect().w // 2 - game_surface.get_rect().w // 2,
                                       screen.get_rect().h // 2 - game_surface.get_rect().h // 2 + 50))
            controls.events(snake, buttons)
            controls.navbar_update(navbar, navbar_img, buttons, img_buttons, info)

            if not settings.is_pause:
                controls.gameloop_update(game_surface, snake, apple, image_field, emerald)
                controls.check_collisions(snake, apple, emerald, info)

                # buttons handler
                for key in buttons:
                    buttons[key].active = 'navbar_' in key
            else:
                controls.pause_update(screen, pause_surface, buttons)

                # buttons handler
                for key in buttons:
                    buttons[key].active = 'pause_srf_' in key
        pygame.display.update()


run()
