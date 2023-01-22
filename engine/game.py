import pygame
import sys
from engine.player import Player


class GameManager:
    def __init__(self, width, height) -> None:
        # Initialize pygame window
        pygame.init()
        pygame.display.set_caption("Space Warriors")
        pygame.display.set_icon(pygame.image.load("resources/icon.png"))

        # Initialize GameManager attributes
        self.__is_running = True
        self.__screen = pygame.display.set_mode((width, height))
        self.__clock = pygame.time.Clock()
        self.__player = Player((width / 2, height - 50), width, height, 10)
        self.__player_sprite = pygame.sprite.GroupSingle(self.__player)

    def run(self) -> None:
        # Main game loop
        while self.__is_running:
            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_running = False
                    pygame.quit()
                    sys.exit()

            self.__screen.fill((30, 30, 30))
            self.__player_handler()

            pygame.display.flip()
            self.__clock.tick(60)

    def __player_handler(self):
        self.__player_sprite.update()
        self.__player_sprite.draw(self.__screen)
        self.__player.cannon.cannonballs.draw(self.__screen)
