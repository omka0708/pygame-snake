import pygame


class Button:  # img-button or text-button
    def __init__(self, screen, position, action, size=(0, 0), img=None, text='', font_size=36, choosing=False):
        self.screen = screen
        self.x, self.y = position
        self.size = size
        self.w, self.h = size
        if img:
            self.img = pygame.transform.scale(img, (self.w, self.h))
            self.rect = pygame.Rect(
                (self.x - self.img.get_rect().w // 2, self.y - self.img.get_rect().h // 2),
                self.img.get_size())
        else:
            self.img = None
            self.font = pygame.font.Font("font/prstart.ttf", font_size)
            self.text = text
            self.text_img = self.font.render(str(self.text), True, pygame.Color('white'), pygame.Color('black'))
            self.rect = pygame.Rect(
                (self.x - self.text_img.get_rect().w // 2, self.y - self.text_img.get_rect().h // 2),
                self.text_img.get_size())
        self.is_hover = False
        self.hover_width = 4
        self.action = action
        self.active = False
        self.choosing = choosing
        self.choosed = False

    def draw(self):
        if self.img:
            self.screen.blit(self.img, self.rect)
        else:
            self.screen.blit(self.text_img, self.rect)
        if self.is_hover:
            pygame.draw.rect(self.screen, pygame.Color('white'),
                             (self.rect.x - self.hover_width // 2, self.rect.y - self.hover_width // 2,
                              self.rect.w + self.hover_width, self.rect.h + self.hover_width),
                             3)
        if self.choosed:
            pygame.draw.rect(self.screen, pygame.Color('red'),
                             (self.rect.x - self.hover_width // 2, self.rect.y - self.hover_width // 2,
                              self.rect.w + self.hover_width, self.rect.h + self.hover_width),
                             3)
