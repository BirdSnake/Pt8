import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """Инициализация отрибутов кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Размеры и свойства кнопок
        self.height, self.width = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Выравние кнопки по центру
        self.rect = pygame.Rect(0,0, self.height, self.width)
        self.rect.center = self.screen_rect.center

        # Сообщение
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Создание сообщения и вывведение его на кнопку"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отрисовка кнопки и вывод сообщения"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

