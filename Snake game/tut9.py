import pygame
pygame.init()

# Colors
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
snake_len = 10
snake_wid = 10
fps = 60
snake_vel_x = 0
snake_vel_y = 0

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_vel_x = 4

            elif event.key == pygame.K_LEFT:
                snake_vel_x = -4

            elif event.key == pygame.K_DOWN:
                snake_vel_y = 4

            elif event.key == pygame.K_UP:
                snake_vel_y = -4


    # It will go diagonal because in resultant velocity

    snake_x += snake_vel_x
    snake_y += snake_vel_y

    game_screen.fill(black)
    pygame.draw.rect(game_screen, green, [snake_x, snake_y, snake_len, snake_wid])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()