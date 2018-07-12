import pygame

from src.Game import Game

def main():
    gameDisplay = pygame.display.set_mode((8000,600))
    pygame.display.set_caption('Anaconda')

    game = Game()
    game.loop()

if __name__ == '__main__':
    main()