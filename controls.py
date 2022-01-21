import sys
import time
from random import randrange
import pygame
import settings
from sound import sounds
import pickle


def events(snake, buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if settings.section['game_loop']:
            if event.type == pygame.KEYDOWN:
                if not snake.pos_changing:
                    snake.pos_changing = True
                    if event.key == pygame.K_w:
                        if snake.control['up']:
                            snake.dx, snake.dy = 0, -1
                            snake.control = {'up': True, 'down': False, 'left': True, 'right': True}
                    elif event.key == pygame.K_s:
                        if snake.control['down']:
                            snake.dx, snake.dy = 0, 1
                            snake.control = {'up': False, 'down': True, 'left': True, 'right': True}
                    elif event.key == pygame.K_d:
                        if snake.control['right']:
                            snake.dx, snake.dy = 1, 0
                            snake.control = {'up': True, 'down': True, 'left': False, 'right': True}
                    elif event.key == pygame.K_a:
                        if snake.control['left']:
                            snake.dx, snake.dy = -1, 0
                            snake.control = {'up': True, 'down': True, 'left': True, 'right': False}
                if event.key == pygame.K_ESCAPE:
                    settings.is_pause = not settings.is_pause

            elif event.type == pygame.MOUSEMOTION:
                for button in buttons.values():
                    if button.active:
                        button.is_hover = button.rect.collidepoint(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons.values():
                    if button.rect.collidepoint(pygame.mouse.get_pos()) and button.active:
                        if settings.sound_on:
                            pygame.mixer.Sound.play(sounds[f'menu_1'])
                        button.is_hover = False
                        button.action()
        elif settings.section['menu']:
            if event.type == pygame.MOUSEMOTION:
                for button in buttons.values():
                    if button.active:
                        button.is_hover = button.rect.collidepoint(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons.values():
                    if button.rect.collidepoint(pygame.mouse.get_pos()) and button.active:
                        if settings.sound_on:
                            pygame.mixer.Sound.play(sounds[f'menu_1'])
                        button.is_hover = False
                        button.action()


def menu_update(screen, middle_block, background_img, buttons, img_buttons):
    screen.blit(background_img, (0, 0))
    screen.blit(middle_block, (screen.get_rect().w // 2 - 150, screen.get_rect().h // 2 - 200))
    middle_block.fill(pygame.Color('white'))
    font_36 = pygame.font.Font("font/prstart.ttf", 36)
    font_32 = pygame.font.Font("font/prstart.ttf", 32)
    font_26 = pygame.font.Font("font/prstart.ttf", 26)

    if settings.menu_section['main']:
        text1_img = font_36.render("SNAKE", True, pygame.Color('white'), pygame.Color('black'))
        text1_rect = text1_img.get_rect()
        text1_rect.centerx = screen.get_rect().centerx
        text1_rect.top = screen.get_rect().h // 3 - 50

        buttons['menu_mb_srf_b0'].draw()
        buttons['menu_mb_srf_b1'].img = pygame.transform.scale(
            img_buttons[f'sound_{"on" if settings.sound_on else "off"}'], buttons['menu_mb_srf_b1'].size)
        buttons['menu_mb_srf_b1'].draw()
        buttons['menu_mb_srf_b2'].draw()

        text2_img = font_26.render("HIGH SCORE", True, pygame.Color('white'), pygame.Color('black'))
        text2_rect = text2_img.get_rect()
        text2_rect.centerx = screen.get_rect().centerx
        text2_rect.top = screen.get_rect().h // 2 - 50

        text3_img = font_26.render(str(settings.high_score), True, pygame.Color('red'))
        text3_rect = text3_img.get_rect()
        text3_rect.centerx = screen.get_rect().centerx
        text3_rect.top = screen.get_rect().h // 2

        screen.blit(text1_img, text1_rect)
        screen.blit(text2_img, text2_rect)
        screen.blit(text3_img, text3_rect)
    elif settings.menu_section['choosing_colors']:
        buttons['menu_ccolor_srf_b2'].draw()
        buttons['menu_ccolor_srf_b3'].draw()
        buttons['menu_ccolor_srf_b4'].draw()
    elif settings.menu_section['cell_speed']:
        text1_img = font_32.render("SCALE", True, pygame.Color('white'), pygame.Color('black'))
        text1_rect = text1_img.get_rect()
        text1_rect.centerx = screen.get_rect().centerx
        text1_rect.top = screen.get_rect().h // 4
        screen.blit(text1_img, text1_rect)

        text2_img = font_32.render("SPEED", True, pygame.Color('white'), pygame.Color('black'))
        text2_rect = text2_img.get_rect()
        text2_rect.centerx = screen.get_rect().centerx
        text2_rect.top = screen.get_rect().h // 2

        screen.blit(text1_img, text1_rect)
        screen.blit(text2_img, text2_rect)

        buttons['menu_ccell_srf_b0'].draw()
        buttons['menu_ccell_srf_b1'].draw()
        buttons['menu_ccell_srf_b2'].draw()
        buttons['menu_ccell_srf_b3'].draw()
        buttons['menu_ccell_srf_b4'].draw()
        buttons['menu_ccell_srf_b5'].draw()
        buttons['menu_ccell_srf_b6'].draw()


def gameloop_update(screen, snake, apple, image_field, emerald):
    show_cells = True
    if show_cells:
        for i in range(len(image_field)):
            for j in range(len(image_field[i])):
                screen.blit(image_field[i][j], (i * settings.CELL, j * settings.CELL, settings.CELL, settings.CELL))

    snake.update()
    apple.update()

    snake.draw()
    apple.draw()

    if settings.show_emerald:
        emerald.update()
        emerald.draw()


def pause_update(screen, pause_surface, b_pause):
    screen.blit(pause_surface, (screen.get_rect().w // 2 - 150,
                                screen.get_rect().h // 2 - 250))
    pause_surface.fill(pygame.Color('white'))
    b_pause['pause_srf_b0'].draw()
    b_pause['pause_srf_b1'].draw()


def navbar_update(screen, img, buttons, img_buttons, info):
    screen.blit(img, (0, 0))
    if not settings.is_pause:
        info.update_rects()
        info.update_scores()

    info.draw_rects()
    info.draw_scores()

    buttons['navbar_srf_b0'].draw()
    buttons['navbar_srf_b1'].img = pygame.transform.scale(img_buttons[f'sound_{"on" if settings.sound_on else "off"}'],
                                                          buttons['navbar_srf_b1'].size)
    buttons['navbar_srf_b1'].draw()


def check_high_score():
    if settings.score > settings.high_score:
        settings.high_score = settings.score
        with open('data.pickle', 'wb') as f:
            pickle.dump(settings.score, f)


def check_collisions(snake, apple, emerald, info):
    if pygame.sprite.collide_rect(snake, apple):
        if settings.sound_on:
            pygame.mixer.Sound.play(sounds['apple'])
        settings.score += 1 * settings.bonus_speed
        apple.rect = pygame.Rect(settings.get_random_free_index(),
                                 (settings.CELL, settings.CELL)).inflate(-settings.CELL // 2, -settings.CELL // 2)
        snake.length += 1
        if not settings.show_emerald:
            apple.was_eaten_times += 1
        if apple.was_eaten_times % 5 == 0 and not settings.show_emerald:
            emerald.rect = pygame.Rect(settings.get_random_free_index(),
                                       (settings.CELL, settings.CELL))
            settings.show_emerald = True

    if pygame.sprite.collide_rect(snake, emerald) and settings.show_emerald:
        if settings.sound_on:
            pygame.mixer.Sound.play(sounds['emerald'])
        settings.score += (info.static_rect.w - info.dynamic_rect.w) // (11 - settings.bonus_cell) + 2 * settings.bonus_speed
        settings.show_emerald = False

    settings.field = [[0 for _ in range(0, settings.RES, settings.CELL)] for _ in range(0, settings.RES, settings.CELL)]
    for coord in snake.coordinates:
        if coord[0] < 0 or coord[1] < 0 or len(snake.coordinates) != len(set(snake.coordinates)) \
                or coord[0] >= settings.RES or coord[1] >= settings.RES:
            if settings.sound_on:
                pygame.mixer.Sound.play(sounds[f'lose_{randrange(1, 3)}'])
            time.sleep(3)
            check_high_score()
            settings.section = {'menu': True, 'game_loop': False}
            return

        settings.field[coord[1] // settings.CELL][coord[0] // settings.CELL] = 1
    settings.field[apple.rect.y // settings.CELL][apple.rect.x // settings.CELL] = 2
