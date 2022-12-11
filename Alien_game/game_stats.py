"""Game_stats"""

class GameStats:
    """Отслеживание статистики игры"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0

        self.game_active = False

    def reset_stats(self):
        self.ship_lefts = self.settings.ship_limit
