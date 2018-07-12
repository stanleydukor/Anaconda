import pygame 

class Game:
    def loop(self):
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

                print(event)

        pygame.display.update()
        clock.tick(60)
