class GameSettings:
    """Класс для хранения настроек игры"""

    def __init__(self):
        """Инициализация настроек игры"""
        self.screen_width = 1200
        self.window_height = 800
        self.bg_color = (222, 222, 222)

        """Настройки корабля"""
        self.ship_speed = 10
        self.ship_limit = 3

        """параметры снаряда"""
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        """Настройки пришельцев"""
        self.alien_speed = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        #Темп роста стоимости пришельцев
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Инициализация динамических настроек игры"""
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 1

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Увеличение настроек игры"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)
