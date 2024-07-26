import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BROWN = (165, 42, 42)

# Tile size
TILE_SIZE = 20


def create_dungeon(width, height):
    # Initialize dungeon with walls
    dungeon = [['#' for _ in range(width)] for _ in range(height)]

    room_pts = {}
    # Create rooms
    num_rooms = random.randint(5, 10)
    for _ in range(num_rooms):
        room_width = random.randint(3, 8)
        room_height = random.randint(3, 8)
        x = random.randint(1, width - room_width - 1)
        y = random.randint(1, height - room_height - 1)
        room_pts[x] = y

        for i in range(y, y + room_height):
            for j in range(x, x + room_width):
                dungeon[i][j] = '.'

    # Create corridors
    x_vals = list(room_pts.keys())
    y_vals = list(room_pts.values())

    for i in range(len(x_vals)):
        if i != len(x_vals) - 1:
            x1 = x_vals[i]
            x2 = x_vals[i + 1]
            y1 = y_vals[i]
            y2 = y_vals[i + 1]
            if x1 < x2:
                for j in range(x1, x2):
                    dungeon[y1][j] = '.'
            else:
                for j in range(x2, x1):
                    dungeon[y1][j] = '.'
            if y1 < y2:
                for j in range(y1, y2):
                    dungeon[j][x2] = '.'
            else:
                for j in range(y2, y1):
                    dungeon[j][x2] = '.'

    # Add entrance
    entrance_x = random.randint(1, width - 2)
    entrance_y = random.randint(1, height - 2)
    while dungeon[entrance_y][entrance_x] != '.':
        entrance_x = random.randint(1, width - 2)
        entrance_y = random.randint(1, height - 2)
    dungeon[entrance_y][entrance_x] = 'E'

    return dungeon


def draw_dungeon(screen, dungeon):
    for y, row in enumerate(dungeon):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if cell == '#':
                pygame.draw.rect(screen, GRAY, rect)
            elif cell == '.':
                pygame.draw.rect(screen, WHITE, rect)
            elif cell == 'E':
                pygame.draw.rect(screen, BROWN, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw cell borders

def main():
    print("Welcome to the D&D Dungeon Generator!")
    width = int(input("Enter the width of the dungeon: "))
    height = int(input("Enter the height of the dungeon: "))
    
    dungeon = create_dungeon(width, height)
    
    # Set up the display
    screen_width = width * TILE_SIZE
    screen_height = height * TILE_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("D&D Dungeon")
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        draw_dungeon(screen, dungeon)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
