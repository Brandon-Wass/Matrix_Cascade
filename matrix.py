import pygame
import random
import os

# Driver modifiers
os.environ["SDL_AUDIODRIVER"] = "dummy" 

# Constants
CELL_SIZE = 10
ROWS, COLS = 108, 192
WIDTH, HEIGHT = CELL_SIZE * COLS, CELL_SIZE * ROWS
chars = [chr(i) for i in range(32, 127)]  # This will use the entire English keyboard

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Matrix Cascade")
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.HWSURFACE | pygame.DOUBLEBUF)
font = pygame.font.SysFont('Courier', CELL_SIZE, bold=True)

layers = [
    (0, 255, 0, 3),  # Brightest and Fastest
    (0, 230, 0, 2.5),
    (0, 205, 0, 2),
    (0, 180, 0, 1.5)  # Dimmest and Slowest
]


class Drop:
    def __init__(self, x, color, speed):
        self.x = x
        self.y = random.randint(-30, -1) * CELL_SIZE
        self.speed = speed
        self.color = color
        self.char = random.choice(chars)
    
    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-30, -1) * CELL_SIZE
            self.char = random.choice(chars)

    def show(self, screen):
        text = font.render(self.char, True, self.color)
        screen.blit(text, (self.x, self.y))

class Stream:
    def __init__(self, x, color):
        self.drops = []
        drop_count = random.randint(1, 10)
        speed = random.uniform(1, 4)
        for _ in range(drop_count):
            self.drops.append(Drop(x, color, speed))
            x += CELL_SIZE

    def update(self):
        for drop in self.drops:
            drop.update()

    def show(self, screen):
        for drop in self.drops:
            drop.show(screen)

streams = []
for i in range(COLS):
    color_layer = random.choice(layers)
    _, color, _, _ = color_layer
    streams.append(Stream(i * CELL_SIZE, (0, color, 0)))

def matrix_cascade():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))

        for stream in streams:
            stream.update()
            stream.show(screen)

        pygame.display.update()
        pygame.time.wait(1 // 60)

matrix_cascade()