import random
import time

import pygame as pg
import sys

pg.init()
height = 400
width = 600
window = (width, height)

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)

display = pg.display.set_mode(window)
pg.display.set_caption('Snake game')

x_snake = 300
y_snake = 300

x_snake_change = 0
y_snake_change = 0

clock = pg.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pg.font.SysFont(None, 40)

screen = display.get_rect()


def send_message(mess, color):
    message = font_style.render(mess, True, color)
    display.blit(message, (screen.center[0] // 3, screen.center[1] // 2))


def game_loop():
    global x_snake, y_snake, x_snake_change, y_snake_change
    game_over = False
    game_close = False

    x_snake = width // 2
    y_snake = height // 2

    x_snake_change = 0
    y_snake_change = 0

    food_x = round(random.randrange(0, screen.right - snake_block) / 10) * 10
    food_y = round(random.randrange(0, screen.bottom - snake_block) / 10) * 10

    while not game_over:

        while game_close:
            display.fill(white)
            send_message('Ты проиграл! нажми Q или C', red)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pg.K_c:
                        game_loop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_snake_change = -10
                    y_snake_change = 0
                elif event.key == pg.K_RIGHT:
                    x_snake_change = 10
                    y_snake_change = 0
                elif event.key == pg.K_UP:
                    x_snake_change = 0
                    y_snake_change = -10
                elif event.key == pg.K_DOWN:
                    x_snake_change = 0
                    y_snake_change = 10

        x_snake += x_snake_change
        y_snake += y_snake_change
        display.fill(white)

        snake = pg.draw.rect(display, blue, (x_snake, y_snake, snake_block, snake_block))
        food = pg.draw.rect(display, red, (food_x, food_y, snake_block, snake_block))

        collide = snake.colliderect(food)

        if snake.right >= screen.right or snake.left <= screen.left or snake.top <= screen.top or snake.bottom >= screen.bottom:
            game_close = True

        if collide:
            print('Еда')

        pg.display.update()

        clock.tick(snake_speed)

    sys.exit()

game_loop()
