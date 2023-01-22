import pygame
import sys
from engine.menu.button import Button


class MainMenu:
    def __init__(self, screen, width, height):
        self.__screen = screen
        self.__font = pygame.font.SysFont("arialblack", 100)
        self.__play_button = 0
        self.__quit_button = 0
        self.__width = width
        self.__height = height
        self.__initialize_buttons()
        self.__is_play_clicked = False
        self.__new_game = False

    @property
    def is_play_clicked(self):
        return self.__is_play_clicked

    @is_play_clicked.setter
    def is_play_clicked(self, new_value):
        self.__is_play_clicked = new_value

    @property
    def new_game(self):
        return self.__new_game

    @new_game.setter
    def new_game(self, new_value):
        self.__new_game = new_value

    def __initialize_buttons(self):
        self.__play_button = Button(image=pygame.image.load("resources/play_btn.png"), pos=(self.__width / 2, self.__height / 2 - 100),
                             text_input="PLAY", font=self.__font, base_color="White", hovering_color="#d7fcd4")
        self.__quit_button = Button(image=pygame.image.load("resources/quit_btn.png"), pos=(self.__width / 2, self.__height / 2 + 100),
                             text_input="QUIT", font=self.__font, base_color="White", hovering_color="#d7fcd4")

    def run(self):
        while not self.__is_play_clicked:
            self.__screen.fill((30, 30, 30))

            menu_mouse_pos = pygame.mouse.get_pos()

            menu_text = self.__font.render("SPACE WARRIORS", True, "#d7ffa6")
            menu_rect = menu_text.get_rect(center=(self.__width / 2, self.__height / 2 - 300))

            self.__screen.blit(menu_text, menu_rect)

            for button in [self.__play_button, self.__quit_button]:
                button.change_color(menu_mouse_pos)
                button.update(self.__screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__play_button.check_for_input(menu_mouse_pos):
                        self.__is_play_clicked = True
                        self.__new_game = True
                    if self.__quit_button.check_for_input(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
