import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Размеры окна
WIDTH = 800
HEIGHT = 600

# Настройки змейки
BLOCK_SIZE = 20
SPEED = 15

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEn, [x, y, BLOCK_SIZE, BLOCK_SIZE])

def game_loop():
    game_over = False
    game_close = False

    # Начальная позиция змейки
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    # Генерация еды
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            font = pygame.font.SysFont(None, 50)
            text = font.render("Игра окончена! Q-Выход, C-Играть снова", True, RED)
            screen.blit(text, (WIDTH//2 - 250, HEIGHT//2 - 50))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = BLOCK_SIZE
                    dx = 0

        # Проверка границ
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += dx
        y += dy
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Проверка столкновения с собой
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)
        pygame.display.update()

        # Съедание еды
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

game_loop()