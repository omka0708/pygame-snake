import pygame.font
import settings


class Info:
    def __init__(self, screen):
        self.screen = screen
        self.text_color = pygame.Color('white')
        self.font = pygame.font.Font("font/prstart.ttf", 36)
        self.static_rect = pygame.Rect(settings.RES - 200, 30, 150, 40)
        self.dynamic_rect = pygame.Rect(settings.RES - 200, 30, 0, 40)
        self.speed_count = 0
        self.speed = settings.SPEED // 4
        self.score_img = self.font.render("null", True, self.text_color)
        self.score_rect = (0, 0, 0, 0)

    def update_rects(self):
        self.speed_count += 1
        if self.speed_count % self.speed == 0:
            if settings.show_emerald and self.dynamic_rect.width < self.static_rect.width:
                self.dynamic_rect.width += 1
            else:
                settings.show_emerald = False
                self.dynamic_rect = pygame.Rect(settings.RES - 200, 30, 0, 40)

    def draw_rects(self):
        pygame.draw.rect(self.screen, pygame.Color('white'), self.static_rect, width=-int(not settings.show_emerald))
        pygame.draw.rect(self.screen, pygame.Color('black'), self.dynamic_rect)

    def update_scores(self):
        self.score_img = self.font.render(str(settings.score), True, self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.centerx = self.screen.get_rect().centerx
        self.score_rect.top = 35

    def draw_scores(self):
        self.screen.blit(self.score_img, self.score_rect)
