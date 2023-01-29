import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, explosion_speed=10):
        super().__init__()
        self.__images_list = []
        for image_number in range(1, 6):
            image = pygame.image.load(f"resources/exp{image_number}.png")
            image = pygame.transform.scale(image, (150, 150))
            self.__images_list.append(image)
        self.__current_index = 0
        self.image = self.__images_list[self.__current_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.__counter = 0
        self.__explosion_speed = explosion_speed

    def update(self):
        self.__counter += 1

        if self.__counter >= self.__explosion_speed and self.__current_index < len(self.__images_list) - 1:
            self.__counter = 0
            self.__current_index += 1
            self.image = self.__images_list[self.__current_index]
        if self.__current_index >= len(self.__images_list) - 1 and self.__counter >= self.__explosion_speed:
            self.kill()