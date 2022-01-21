import pygame
import settings


class Snake:
    def __init__(self, screen, color):
        super(Snake, self).__init__()
        self.screen = screen
        self.length = 1
        self.rect = pygame.Rect(settings.get_random_free_index(),  # rect.y
                                (settings.CELL, settings.CELL))  # rect.width, rect.height
        self.coordinates = [(self.rect.x, self.rect.y)]
        self.coord_and_nav = {}  # index of coordinates: 'nav'
        self.dx, self.dy = 0, 0
        self.control = {'up': True, 'down': True, 'left': True, 'right': True}
        self.speed_count, self.speed = 0, settings.SPEED
        self.pos_changing = False
        self.color = color
        self.img_head = {'up': pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_head_up.png"),
                                                      (self.rect.width, self.rect.height)),
                         'down': pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_head_down.png"),
                                                        (self.rect.width, self.rect.height)),
                         'left': pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_head_left.png"),
                                                        (self.rect.width, self.rect.height)),
                         'right': pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_head_right.png"),
                                                         (self.rect.width, self.rect.height))
                         }
        self.img_body = [pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_body_1.png"),
                                                (self.rect.width, self.rect.height)),
                         pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_body_2.png"),
                                                (self.rect.width, self.rect.height)),
                         pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_body_3.png"),
                                                (self.rect.width, self.rect.height)),
                         pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_body_4.png"),
                                                (self.rect.width, self.rect.height)),
                         pygame.transform.scale(pygame.image.load(f"img/snake_{self.color}/snake_body.png"),
                                                (self.rect.width, self.rect.height))
                         ]

    def draw(self):
        for i in range(len(self.coordinates)):
            x = self.coordinates[i][0]
            y = self.coordinates[i][1]
            if i == len(self.coordinates) - 1:
                if not self.control['up']:  # looking down
                    self.screen.blit(self.img_head['down'], (x, y, self.rect.width, self.rect.height))
                elif not self.control['down']:  # looking right
                    self.screen.blit(self.img_head['up'], (x, y, self.rect.width, self.rect.height))
                elif not self.control['right']:
                    self.screen.blit(self.img_head['left'], (x, y, self.rect.width, self.rect.height))
                elif not self.control['left']:
                    self.screen.blit(self.img_head['right'], (x, y, self.rect.width, self.rect.height))
                else:
                    self.screen.blit(self.img_head['up'], (x, y, self.rect.width, self.rect.height))
            else:
                nav = self.coord_and_nav[self.coordinates[i]]
                if nav == 'updwn':
                    self.screen.blit(self.img_body[i % 2], (x, y, self.rect.width, self.rect.height))
                elif nav == 'rl':
                    self.screen.blit(self.img_body[i % 2 + 2], (x, y, self.rect.width, self.rect.height))
                elif nav == 'rot':
                    self.screen.blit(self.img_body[4], (x, y, self.rect.width, self.rect.height))

    def update(self):
        self.speed_count += 1
        if self.speed_count % self.speed == 0:
            self.rect.x += self.dx * settings.CELL
            self.rect.y += self.dy * settings.CELL

            for i in range(len(self.img_body)):
                self.img_body[i] = pygame.transform.rotate(self.img_body[i], 180)

            if not self.control['up'] or not self.control['down']:  # looking up/down
                self.coord_and_nav[(self.rect.x, self.rect.y)] = 'updwn'
                self.coordinates.append((self.rect.x, self.rect.y))
            elif not self.control['right'] or not self.control['left']:
                self.coord_and_nav[(self.rect.x, self.rect.y)] = 'rl'
                self.coordinates.append((self.rect.x, self.rect.y))

            self.coordinates = self.coordinates[-self.length:]

            for i in range(1, len(self.coordinates)):
                if self.coord_and_nav[self.coordinates[i]] == 'updwn' and self.coord_and_nav[
                    self.coordinates[i - 1]] == 'rl' or self.coord_and_nav[self.coordinates[i - 1]] == 'updwn' and \
                        self.coord_and_nav[self.coordinates[i]] == 'rl':
                    self.coord_and_nav[self.coordinates[i - 1]] = 'rot'

            self.pos_changing = False

    def create_snake(self):
        self.length = 1
        self.rect = pygame.Rect(settings.get_random_free_index(),  # rect.y
                                (settings.CELL, settings.CELL))  # rect.width, rect.height
        self.coordinates = [(self.rect.x, self.rect.y)]
        self.coord_and_nav = {}  # index of coordinates: 'nav'
        self.dx, self.dy = 0, 0
        self.control = {'up': True, 'down': True, 'left': True, 'right': True}
        self.speed_count, self.speed = 0, settings.SPEED
        self.pos_changing = False
