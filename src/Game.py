import pygame 

from src.Settings import Settings
from src.Snake import Snake

class Game:
    def __init__(self, display):
        self.display = display
        self.score = 0

    def loop(self):
        clock = pygame.time.Clock()
        snake = Snake(self.display)

        x_change = 0
        y_change = 0
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -Settings['snake']['speed']
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = Settings['snake']['speed']
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        x_change = 0
                        y_change = -Settings['snake']['speed']
                    elif event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = Settings['snake']['speed']
        
            self.display.fill(Settings['colors']['green'])
            
            pygame.draw.rect(
                self.display, 
                Settings['colors']['black'],
                [
                    Settings['game']['bumper_size'],
                    Settings['game']['bumper_size'],
                    Settings['game']['height'] - Settings['game']['bumper_size'] * 2,
                    Settings['game']['width'] - Settings['game']['bumper_size'] * 2
                ]
            )
            
            snake.move(x_change, y_change)
            snake.draw()
            
            pygame.font.init()
            font = pygame.font.Font('./assets/Now-Regular.otf', 28)
            
            score_text = 'Score: {}'.format(self.score)
            score = font.render(score_text, True, Settings['colors']['white'])
            title = font.render('Anaconda', True, Settings['colors']['white'])


            title_rect = title.get_rect(
                center=(
                     Settings['game']['width'] / 2, 
                    10
                )
            )

            score_rect = score.get_rect(
                center=(
                    500/2, 
                    Settings['game']['height'] - 10
                )
            )

            self.display.blit(score, score_rect)
            self.display.blit(title, title_rect)

            pygame.display.update()
            clock.tick(Settings['game']['fps'])
