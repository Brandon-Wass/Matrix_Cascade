import pygame
import random
import os

# Driver modifiers
os.environ["SDL_AUDIODRIVER"] = "dummy" 

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Screen dimensions
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
FONT_SIZE = 20

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Matrix Cascade")

# Font settings
font = pygame.font.SysFont("Courier New", FONT_SIZE, bold=True)

class Column:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.chars = [random.choice(" 0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ ") for _ in range(random.randint(SCREEN_HEIGHT // FONT_SIZE, 2 * (SCREEN_HEIGHT // FONT_SIZE)))]
        self.offset = random.randint(0, len(self.chars))

    def draw(self, screen):
        for index, char in enumerate(self.chars):
            y_pos = (self.y + index - self.offset) % len(self.chars)
            screen.blit(font.render(char, True, GREEN), (self.x, y_pos * FONT_SIZE))

    def update(self):
        self.offset = (self.offset + 1) % len(self.chars)

# Create columns to fill the screen width
columns = [Column(x, random.randint(0, SCREEN_HEIGHT // FONT_SIZE)) for x in range(0, SCREEN_WIDTH, FONT_SIZE)]

# Clock for controlling FPS
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill(BLACK)

    for column in columns:
        column.draw(screen)
        column.update()

    pygame.display.flip()
    
    # Cap the FPS at 60
    clock.tick(10)

pygame.quit()
