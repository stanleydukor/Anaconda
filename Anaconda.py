import pygame

from src.Game import Game
from src.Settings import Settings

def main():
    display = pygame.display.set_mode((
        Settings['game']['width'], 
        Settings['game']['height']
    ))
    pygame.display.set_caption(Settings['game']['caption'])

    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()