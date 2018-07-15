import pygame

from src.Settings import Settings

class Snake:
    def __init__(self, display):
        self.x_pos = Settings['game']['width'] / 2
        self.y_pos = Settings['game']['height'] / 2
        self.display = display

    def draw(self):
        pygame.draw.rect(
            self.display, 
            Settings['colors']['green'],
            [
                self.x_pos,
                self.y_pos,
                Settings['snake']['height'],
                Settings['snake']['width']
            ]
        )

    def move(self, x_change, y_change):
        self.x_pos += x_change
        self.y_pos += y_change