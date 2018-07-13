import pygame

from src.Game import Game
from src.Settings import Settings

def main():
    display = pygame.display.set_mode((Settings['game']['width'], Settings['game']['width']))
    pygame.display.set_caption('Anaconda')

    game = Game()
    game.loop()

if __name__ == '__main__':
    main()