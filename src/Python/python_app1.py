import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простая бродилка")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройки персонажа
player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT // 2
speed = 5

# Платформы
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
    pygame.Rect(200, 400, 200, 20),
    pygame.Rect(500, 300, 150, 20)
]

# Гравитация
gravity = 0.5
jump_power = -12
vertical_momentum = 0
on_ground = False

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                vertical_momentum = jump_power
                on_ground = False

    # Движение
    keys = pygame.key.get_pressed()
    horizontal_movement = 0
    if keys[pygame.K_a]:
        horizontal_movement -= speed
    if keys[pygame.K_d]:
        horizontal_movement += speed

    # Применение гравитации
    vertical_momentum += gravity
    if vertical_momentum > 10:
        vertical_momentum = 10

    # Горизонтальное перемещение
    player_x += horizontal_movement
    
    # Вертикальное перемещение
    player_y += vertical_momentum

    # Коллизия с платформами
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform):
            if vertical_momentum > 0:
                player_y = platform.y - player_size
                vertical_momentum = 0
                on_ground = True
            elif vertical_momentum < 0:
                player_y = platform.y + platform.height
                vertical_momentum = 0

    # Ограничение границ экрана
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    # Отрисовка
    # Платформы
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)
    
    # Персонаж
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()