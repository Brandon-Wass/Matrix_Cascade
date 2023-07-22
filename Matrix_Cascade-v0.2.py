import pygame
import random
import os


# Driver modifiers
os.environ["SDL_AUDIODRIVER"] = "dummy" # Disables audio driver

# Define the dimensions of the matrix-style face and size of each cell
CELL_SIZE = 10
ROWS, COLS = 70, 120
WIDTH, HEIGHT = CELL_SIZE * COLS, CELL_SIZE * ROWS

# Define the characters to be used in the matrix-style face
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
         'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
         'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Matrix Cascade")

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

# Define the font for the cascading characters
font = pygame.font.SysFont('Courier', CELL_SIZE, bold=True)

# Define the function to generate a computer-generated face using cascading characters
def matrix_cascade():
    # Create the computer-generated face
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Initialize the Pygame window with black color as background
        screen.fill((0, 0, 0))
        
        # Draw the cascading characters over the computer-generated face
        for i in range(ROWS):
            for j in range(COLS):
                char = random.choice(chars)
                color = (0, 255, 0) # Green color for each cell
                text = font.render(char, True, color)
                x = j * CELL_SIZE
                y = i * CELL_SIZE
                screen.blit(text, (x, y))
        
        pygame.display.update()
        pygame.time.wait(8) # Pause for 8 milliseconds
        
# Call the function to display the computer-generated face using cascading characters
matrix_cascade()
