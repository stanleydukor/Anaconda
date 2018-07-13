import pygame 

from src.Settings import Settings

class Game:
    def loop(self):
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

        pygame.display.update()
        clock.tick(Settings.game.fps)
