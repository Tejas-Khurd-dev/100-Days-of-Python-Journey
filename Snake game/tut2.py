import pygame
pygame.init()

# Creating display
game_screen = pygame.display.set_mode((1200, 600))

# Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
