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

# Game specific variables
exit_game = False
game_over = False
snake_x = 50
snake_y = 50
snake_len = 10
snake_wid = 10

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have enter a right key")

    game_screen.fill(black)
    pygame.draw.rect(game_screen, green, [snake_x, snake_y, snake_len, snake_wid])
    pygame.display.update()

pygame.quit()
quit()