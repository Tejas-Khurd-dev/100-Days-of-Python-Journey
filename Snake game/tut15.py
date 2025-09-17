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
screen_height = 700
game_screen = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()

# Game specific variables
food_x = random.randint(20, screen_width - 10)
food_y = random.randint(20, screen_height - 10)

#  None is default system font
font = pygame.font.SysFont(None, 30)

def plot_snake(game_window, color, snk_list, snk_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snk_size, snk_size])

def text_screen(text , color, x, y):
    screen_text = font.render(text, True, color)
    game_screen.blit(screen_text, [x,y])

def welcome():
    exit_game = False
    while not exit_game:
        game_screen.fill(black)
        text_screen("Welcome to Snake Game", white, 330, screen_height/2 - 90)
        text_screen("Press Space Bar To Play", white, 330, screen_height / 2 - 50)
        text_screen("-Tejas Sandeep Khurd", white, 330, screen_height / 2 - 8)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(60)

def game_loop():

    global food_x, food_y

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

    score = 0

    with open("high_score.txt", "r") as f:
        high_score = f.read()

    # Creating a game loop
    while not exit_game:

        if game_over:
            game_screen.fill(white)
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))

            text_screen("Game Over!", red, 380, screen_height/2 - 50)
            text_screen("Press Enter to play game again ", black, 280, screen_height / 2 - 20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
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
                    elif event.key == pygame. K_q:
                        score += 5
            # It will not go diagonal because we have set second axis direction 0 while we are working on first axis

            snake_x += snake_vel_x
            snake_y += snake_vel_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1

                food_x = random.randint(20, screen_width - 10)
                food_y = random.randint(20, screen_height - 10)

                snake_len += 3

                if score > int(high_score):
                    high_score = score

            game_screen.fill(black)
            text_screen(f"score: {score}  HS: {high_score}", white, 5, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_y < 0 or snake_x > screen_width or snake_y > screen_height:
                game_over = True

            plot_snake(game_screen, green, snake_list, snake_size)
            pygame.draw.rect(game_screen, red, [food_x, food_y, snake_size - 2, snake_size - 2])

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
