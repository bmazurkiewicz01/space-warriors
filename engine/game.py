import pygame, sys

class GameManager:
    def __init__(self, width, height) -> None:
        pygame.init()
        pygame.display.set_caption("Space Warriors")
        self.__screen = pygame.display.set_mode((width, height))
        self.__clock = pygame.time.Clock()
        self.__is_running = True
    def run(self) -> None:
        while self.__is_running:

            self.__screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            self.__clock.tick(60)