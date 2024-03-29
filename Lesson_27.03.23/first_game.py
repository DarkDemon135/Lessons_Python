import pygame
import random

SCREEN_WIDTH = 500 # Ширина экрана
SCREEN_HEIGHT = 500 # Высота экрана

PLAYER_WIDTH = SCREEN_WIDTH // 10 # Ширина экрана
PLAYER_HEIGHT = SCREEN_HEIGHT // 10 # Высота экрана
PLAYER_SPEED = PLAYER_HEIGHT // 4

ITEM_WIDTH = SCREEN_WIDTH // 15
ITEM_HEIGHT = SCREEN_HEIGHT // 15

GREEN   = (0, 200, 0)
RED     = (255, 0, 0)
BLUE    = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MyGame")

pl_x = (SCREEN_WIDTH // 2) - (PLAYER_WIDTH // 2)
pl_y = (SCREEN_HEIGHT // 2) - (PLAYER_HEIGHT // 2)
# pl_x = (SCREEN_WIDTH // 2)
# pl_y = (SCREEN_HEIGHT // 2)

items = []
for i in range(3):
    item_x = random.randint(ITEM_WIDTH, SCREEN_WIDTH - ITEM_WIDTH)
    item_y = random.randint(ITEM_HEIGHT, SCREEN_HEIGHT - ITEM_HEIGHT)
    items.append((item_x, item_y))

def draw_player(x, y):
    pygame.draw.rect(screen, RED, [x, y, PLAYER_WIDTH, PLAYER_HEIGHT])

def draw_items(items):
    for item in items:
        pygame.draw.ellipse(screen, BLUE, [item[0], item[1], ITEM_WIDTH, ITEM_HEIGHT])

def check_collision(items):
    global pl_y
    global pl_x
    for item in items:
        if pl_x < item[0] + ITEM_WIDTH and pl_x + PLAYER_WIDTH > item[0] \
        and pl_y < item[1] + ITEM_HEIGHT and pl_y + PLAYER_HEIGHT > item[1]:
            items.remove(item)


def player_move(diff_x, diff_y) :
    global pl_y
    global pl_x

    new_pl_y = pl_y + diff_y
    if (new_pl_y >= 0 and new_pl_y < SCREEN_HEIGHT):
        pl_y = new_pl_y
    new_pl_x = pl_x + diff_x
    if (new_pl_x >= 0 and new_pl_x < SCREEN_WIDTH):
        pl_x = new_pl_x


def keys_hook(keys):
    if keys[pygame.K_UP]:
        player_move(0, -PLAYER_HEIGHT)
    if keys[pygame.K_DOWN]:
        player_move(0, PLAYER_HEIGHT)
    if keys[pygame.K_LEFT]:
        player_move(-PLAYER_WIDTH, 0)
    if keys[pygame.K_RIGHT]:
        player_move(PLAYER_WIDTH ,0)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            keys_hook(pygame.key.get_pressed())
            check_collision(items)
            screen.fill(GREEN)
            draw_player(pl_x, pl_y)
            draw_items(items)
            pygame.display.update()

if __name__ == '__main__':
    main_loop()