import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)

# Tile size
TILE_SIZE = 50


def create_irregular_puddle(dungeon, width, height):
    # Fill the dungeon with walls initially
    for i in range(height):
        for j in range(width):
            dungeon[i][j] = '#'

    # Puddle center and max radius
    center_x = width // 2
    center_y = height // 2
    max_radius_x = width // 3
    max_radius_y = height // 3

    for y in range(height):
        for x in range(width):
            # Calculate normalized distance from the center
            dx = x - center_x
            dy = y - center_y
            normalized_x = dx / max_radius_x
            normalized_y = dy / max_radius_y

            # Create an elliptical shape with some irregularities
            ellipse_distance = (normalized_x ** 2 + normalized_y ** 2) ** 0.5
            irregularity = random.uniform(0.85, 1.15)

            # Check if the point is within the elliptical boundary
            if ellipse_distance < irregularity:
                dungeon[y][x] = '.'


def add_red_spots(dungeon, width, height, num_spots):
    for _ in range(num_spots):
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)

            # Only place a spot if it's in the white area
            if dungeon[y][x] == '.':
                dungeon[y][x] = 'R'
                break


def draw_dungeon(screen, dungeon):
    for y, row in enumerate(dungeon):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if cell == '#':
                pygame.draw.rect(screen, GRAY, rect)
            elif cell == '.':
                pygame.draw.rect(screen, WHITE, rect)
            elif cell == 'R':
                pygame.draw.rect(screen, RED, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw cell borders


def main():
    print("Welcome to the Irregular Puddle Room Layout Generator!")

    width = 20
    height = 20

    # Get user input for the number of red spots
    num_spots = int(input("Enter the number of red spots: "))

    # Initialize dungeon
    dungeon = [['#' for _ in range(width)] for _ in range(height)]

    # Create an irregular puddle room
    create_irregular_puddle(dungeon, width, height)

    # Add red spots
    add_red_spots(dungeon, width, height, num_spots)

    # Set up the display
    screen_width = width * TILE_SIZE
    screen_height = height * TILE_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Irregular Puddle Room Layout with Red Spots")

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)  # Fill the background with white
        draw_dungeon(screen, dungeon)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
