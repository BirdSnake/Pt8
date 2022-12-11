import pygame.font
from pygame.sprite import Group

from Alien_game.main import Ship


class Scoreboard:
    "Вывод игровой информаций"
    def __init__(self, ai_game):
        """Атрибуты подсчета очков"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_ships()

    def prep_score(self):
        """Вывод счета на экран"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships(self):
        """Кол-во кораблей оставшихся в запасе"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_lefts):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.ships.draw(self.screen)
