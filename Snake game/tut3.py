import pygame
pygame.init()

# Creating display
game_screen = pygame.display.set_mode((1200, 600))

# Game title
pygame.display.set_caption("Snake Game")


# Game specific variables
exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have enter a right key")

pygame.quit()
quit()