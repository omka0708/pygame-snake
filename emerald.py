import pygame

import settings


class Emerald(pygame.sprite.Sprite):
    def __init__(self, screen, color):
        super(Emerald, self).__init__()
        self.screen = screen
        self.RES = screen.get_height()
        self.SIZE = settings.CELL
        self.color = color
        self.rect = pygame.Rect(settings.get_random_free_index(),
                                (self.SIZE, self.SIZE))
        self.img = pygame.transform.scale(pygame.image.load(f"img/emerald/emerald_{color}.png"),
                                          (self.rect.width, self.rect.height))

        self.speed_count, self.speed = 0, settings.SPEED

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def update(self):
        self.speed_count += 0.5
        if self.speed_count % self.speed == 0.0:
            self.img = pygame.transform.flip(self.img, True, False)

    def create_emerald(self):
        self.rect = pygame.Rect(settings.get_random_free_index(),
                                (self.SIZE, self.SIZE))
