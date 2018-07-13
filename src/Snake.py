import pygame

class Snake:
    def __init__(self):
        self.x_pos = 400
        self.y_pos = 300

    def draw(self):
        pass
    
    def move(self, x_change, y_change):
        self.x_pos += x_change
        self.y_pos += y_change