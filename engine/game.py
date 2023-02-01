import pygame
import sys

from engine.level.level import Level
from engine.menu.menu import MainMenu
from engine.player import Player
from engine.weapon.cannon.cannon import Cannon
from engine.weapon.explosion import Explosion


class GameManager:
    def __init__(self, width, height, levels):
        # Initialize pygame window
        pygame.init()
        pygame.display.set_caption("Space Warriors")
        pygame.display.set_icon(pygame.image.load("resources/icon.png"))

        # Initialize GameManager attributes
        self.__is_running = True
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((width, height))
        self.__clock = pygame.time.Clock()
        self.__font = pygame.font.SysFont("arialblack", 48)
        self.__is_game_stopped = True
        self.__player_won = False

        # Player handler variables
        self.__player = 0
        self.__player_sprite = 0

        # Create a MainMenu object to handle game states
        self.__main_menu = MainMenu(self.__screen, width, height)

        # Create levels
        self.__levels = []
        self.__previous_level_index = 0
        self.__level_index = 0
        for level in levels:
            self.__levels.append(Level(self.__screen, width, height, level["level_name"],
                                       level["obstacle_amount"], level["alien_rows"], level["alien_columns"],
                                       level["alien_damage"], level["alien_shooting_time"], level["level_audio_path"]))

        # Create timer for alien shooting
        self.__alien_timer = pygame.USEREVENT + 1

        # Create group for explosions
        self.__cannon_explosions = pygame.sprite.Group()
        self.__laser_explosions = pygame.sprite.Group()

        # Import sound
        self.__pop_sound = pygame.mixer.Sound("audio/pop.wav")
        self.__pop_sound.set_volume(0.4)
        self.__explosions_sound = pygame.mixer.Sound("audio/explosion.wav")
        self.__explosions_sound.set_volume(0.7)

    def run(self):
        # Main game loop
        while self.__is_running:
            self.__screen.fill((30, 30, 30))

            # Check current game state
            if self.__main_menu.is_play_clicked:
                if self.__main_menu.new_game:
                    self.__cannon_explosions = pygame.sprite.Group()
                    self.__laser_explosions = pygame.sprite.Group()
                    self.__main_menu.new_game = False
                    self.__initialize_player()
                    self.__levels[self.__level_index].initialize_aliens()
                    self.__levels[self.__level_index].game_music.play(loops=-1)
                    self.__is_game_stopped = False
                    self.__player_won = False
                    pygame.time.set_timer(self.__alien_timer, self.__levels[self.__level_index].alien_shooting_time)
                    pygame.time.wait(10)
                if not self.__is_game_stopped:
                    self.__player_handler()
                    self.__levels[self.__level_index].enemy_handler()
                    self.__explosions_handler()
                self.__check_victory_condition()
                self.__check_player_health()
            else:
                self.__main_menu.run()

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__main_menu.is_play_clicked = False
                        self.__levels[self.__level_index].game_music.stop()
                if event.type == self.__alien_timer and not self.__is_game_stopped:
                    self.__levels[self.__level_index].alien_attack()

            # Refresh screen
            pygame.display.update()
            self.__clock.tick(60)

    def __initialize_player(self):
        self.__player = Player((self.__width / 2, self.__height - 80), self.__width, self.__height, 10, self.__screen)
        self.__player_sprite = pygame.sprite.GroupSingle(self.__player)

    def __player_handler(self):
        self.__player_sprite.update()
        self.__player_sprite.draw(self.__screen)
        self.__check_collisions()
        for weapon in self.__player.weapons:
            weapon.weapon_shots.draw(self.__screen)

    def __check_player_health(self):
        if self.__player.health <= 0:
            self.__is_game_stopped = True
            victory_text = self.__font.render(f"You died!", False, "white")
            new_game_font = pygame.font.SysFont("arialblack", 24)
            new_game_text = new_game_font.render(f"Please click escape to start a new game", False, "red")

            victory_rect = victory_text.get_rect()
            victory_rect.centerx = self.__width / 2
            victory_rect.centery = self.__height / 2 - 100
            self.__screen.blit(victory_text, victory_rect)

            new_game_rect = new_game_text.get_rect()
            new_game_rect.centerx = self.__width / 2
            new_game_rect.centery = self.__height / 2 - 25
            self.__screen.blit(new_game_text, new_game_rect)

    def __explosions_handler(self):
        self.__cannon_explosions.draw(self.__screen)
        self.__cannon_explosions.update()
        self.__laser_explosions.draw(self.__screen)
        self.__laser_explosions.update()

    def __check_victory_condition(self):
        if not self.__levels[self.__level_index].aliens:
            if not self.__player_won:
                self.__levels[self.__level_index].game_music.stop()
                self.__is_game_stopped = True
                self.__previous_level_index = self.__level_index
                self.__level_index += 1
                self.__player_won = True
                if self.__level_index >= len(self.__levels):
                    self.__level_index = 0
            victory_text = self.__font.render(
                f"You finished level: {self.__levels[self.__previous_level_index].level_name}!", False, "white")
            score_text = self.__font.render(f"Your score is {self.__player.score}", False, "white")
            new_game_font = pygame.font.SysFont("arialblack", 24)
            new_game_text = new_game_font.render(f"Please click escape to start a new game", False, "red")

            victory_rect = victory_text.get_rect()
            victory_rect.centerx = self.__width / 2
            victory_rect.centery = self.__height / 2 - 100
            self.__screen.blit(victory_text, victory_rect)

            score_rect = score_text.get_rect()
            score_rect.centerx = self.__width / 2
            score_rect.centery = self.__height / 2
            self.__screen.blit(score_text, score_rect)

            new_game_rect = new_game_text.get_rect()
            new_game_rect.centerx = self.__width / 2
            new_game_rect.centery = self.__height / 2 + 50
            self.__screen.blit(new_game_text, new_game_rect)

    def __check_collisions(self):
        # Check player lasers and cannon
        if self.__player.weapons:
            for weapon in self.__player.weapons:
                if isinstance(weapon, Cannon):
                    for bullet in weapon.weapon_shots:
                        alien_collisions = pygame.sprite.spritecollide(bullet, self.__levels[self.__level_index].aliens,
                                                                       True)
                        block_collisions = pygame.sprite.spritecollide(bullet, self.__levels[self.__level_index].blocks,
                                                                       True)
                        if alien_collisions:
                            self.__player.score += 1
                        if block_collisions or alien_collisions:
                            explosion = Explosion(bullet.rect.x, bullet.rect.y, 7)
                            self.__cannon_explosions.add(explosion)
                            bullet.kill()
                            self.__explosions_sound.play()
                            pygame.sprite.spritecollide(explosion, self.__levels[self.__level_index].blocks, True)

                            extra_alien_collisions = pygame.sprite.spritecollide(explosion, self.__levels[
                                self.__level_index].aliens,
                                                                                 True)
                            for alien in extra_alien_collisions:
                                self.__player.score += 1
                else:
                    for bullet in weapon.weapon_shots:
                        if pygame.sprite.spritecollide(bullet, self.__levels[self.__level_index].blocks, True):
                            bullet.kill()
                            explosion = Explosion(bullet.rect.x, bullet.rect.y, 3, "resources/laserexp", (70, 70))
                            self.__laser_explosions.add(explosion)
                        if pygame.sprite.spritecollide(bullet, self.__levels[self.__level_index].aliens, True):
                            self.__player.score += 1
                            bullet.kill()
                            self.__pop_sound.play()
                            explosion = Explosion(bullet.rect.x, bullet.rect.y, 3, "resources/laserexp", (70, 70))
                            self.__laser_explosions.add(explosion)

        # Check alien lasers
        if self.__levels[self.__level_index].alien_weapons:
            for weapon in self.__levels[self.__level_index].alien_weapons:
                if pygame.sprite.spritecollide(weapon, self.__levels[self.__level_index].blocks, True):
                    weapon.kill()
                    self.__pop_sound.play()
                    explosion = Explosion(weapon.rect.x, weapon.rect.y, 3, "resources/laserexp", (70, 70))
                    self.__laser_explosions.add(explosion)
                if pygame.sprite.spritecollide(weapon, self.__player_sprite, False):
                    self.__player.health -= self.__levels[self.__level_index].alien_damage
                    weapon.kill()
                    self.__pop_sound.play()
                    explosion = Explosion(weapon.rect.x, weapon.rect.y, 3, "resources/laserexp", (70, 70))
                    self.__laser_explosions.add(explosion)

        # Check alien collisions
        if self.__levels[self.__level_index].aliens:
            for alien in self.__levels[self.__level_index].aliens:
                pygame.sprite.spritecollide(alien, self.__levels[self.__level_index].blocks, True)

                if pygame.sprite.spritecollide(alien, self.__player_sprite, False):
                    self.__player.health = 0
