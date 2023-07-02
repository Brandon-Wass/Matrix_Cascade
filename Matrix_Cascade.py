import pygame
import random
import os

# Constants
BLACK = pygame.Color('black')
GREEN = pygame.Color('green')
FONT_SIZE = 10
CELL_SIZE = 10
ROWS, COLS = 70, 120
WIDTH, HEIGHT = CELL_SIZE * COLS, CELL_SIZE * ROWS

# Disable SDL audio  
os.environ["SDL_AUDIODRIVER"] = "dummy"   

# Initialize characters  
chars = {chr(i): None for i in range(ord('0'), ord('z') + 1)}   

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Matrix Cascade")
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
font = pygame.font.SysFont('Courier', FONT_SIZE, bold=True)

# Set the frame rate of the display
clock = pygame.time.Clock()

# Generate the matrix cascade
def matrix_cascade():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw the cascading characters
        for i in range(ROWS):
            for j in range(COLS):
                char = random.choice(list(chars))
                text = font.render(char, True, GREEN)
                screen.blit(text, (j * CELL_SIZE, i * CELL_SIZE))

        # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(16)

# Call the function to display the computer-generated face using cascading characters
matrix_cascade()
