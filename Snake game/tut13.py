import pygame
import random
pygame.init()

# Colors
white = 255, 255, 255
black = (41, 37, 37)
red = (255, 0, 0)
green = (0, 255, 0)

# Creating display
screen_width = 900
screen_height = 600
game_screen = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()

# Game specific variables
exit_game = False
game_over = False

snake_x = 50
snake_y = 50

snake_size = 10
snake_len = 1
snake_list = []

fps = 30

snake_vel_x = 0
snake_vel_y = 0
init_vel = 5

food_x = random.randint(10, screen_width - 10)
food_y = random.randint(10, screen_height - 10)

#  None is default system font
font = pygame.font.SysFont(None, 30)

def plot_snake(gameWindow, color, snk_list, snk_size):
    print(snake_list)
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snk_size, snk_size])

def screen_score(text , color, x, y):
    screen_text = font.render(text, True, color)
    game_screen.blit(screen_text, [x,y])

score = 0

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_vel_x = init_vel
                snake_vel_y = 0
            elif event.key == pygame.K_LEFT:
                snake_vel_x = -init_vel
                snake_vel_y = 0
            elif event.key == pygame.K_DOWN:
                snake_vel_y = init_vel
                snake_vel_x = 0
            elif event.key == pygame.K_UP:
                snake_vel_y = -init_vel
                snake_vel_x = 0

    # It will not go diagonal because we have set second axis direction 0 while we are working on first axis

    snake_x += snake_vel_x
    snake_y += snake_vel_y

    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        score += 1

        food_x = random.randint(10, screen_width - 10)
        food_y = random.randint(10, screen_height - 10)

        snake_len += 3

    game_screen.fill(black)
    screen_score(f"score: {score}", white, 5, 5)

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len(snake_list) > snake_len:
        del snake_list[0]

    plot_snake(game_screen, green, snake_list, snake_size)
    pygame.draw.rect(game_screen, red, [food_x, food_y, snake_size - 2, snake_size - 2])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
