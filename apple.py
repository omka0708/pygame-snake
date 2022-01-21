import pygame

import settings


class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.RES = screen.get_height()
        self.rect = pygame.Rect(settings.get_random_free_index(),
                                (settings.CELL, settings.CELL)).inflate(-settings.CELL // 2,
                                                                -settings.CELL // 2)  # rect.width, rect.height
        self.img = pygame.transform.scale(pygame.image.load("img/apple/apple.png"), (self.rect.width, self.rect.height))
        self.was_eaten_times = 0

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def update(self):
        pass

    def create_apple(self):
        self.rect = pygame.Rect(settings.get_random_free_index(),
                                (settings.CELL, settings.CELL)).inflate(-settings.CELL // 2,
                                                                -settings.CELL // 2)  # rect.width, rect.height
        self.was_eaten_times = 0
