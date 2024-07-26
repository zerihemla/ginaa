import random
import pygame
import sys

class DungeonGenerator:
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (100, 100, 100)
    BROWN = (165, 42, 42)

    # Tile size
    TILE_SIZE = 20

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dungeon = None
        self.screen = None

    def create_dungeon(self):
        # Initialize dungeon with walls
        self.dungeon = [['#' for _ in range(self.width)] for _ in range(self.height)]
        
        # Create rooms
        num_rooms = random.randint(5, 10)
        for _ in range(num_rooms):
            self._create_room()
        
        # Create corridors
        self._create_corridors()
        
        # Add entrance
        self._add_entrance()

    def _create_room(self):
        room_width = random.randint(3, 8)
        room_height = random.randint(3, 8)
        x = random.randint(1, self.width - room_width - 1)
        y = random.randint(1, self.height - room_height - 1)
        
        for i in range(y, y + room_height):
            for j in range(x, x + room_width):
                self.dungeon[i][j] = '.'

    def _create_corridors(self):
        for _ in range(self.width + self.height):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if self.dungeon[y][x] == '.':
                dx = random.choice([-1, 0, 1])
                dy = random.choice([-1, 0, 1]) if dx == 0 else 0
                
                for _ in range(random.randint(3, 10)):
                    nx, ny = x + dx, y + dy
                    if 0 < nx < self.width - 1 and 0 < ny < self.height - 1:
                        self.dungeon[ny][nx] = '.'
                        x, y = nx, ny
                    else:
                        break

    def _add_entrance(self):
        entrance_x = random.randint(1, self.width - 2)
        entrance_y = random.randint(1, self.height - 2)
        while self.dungeon[entrance_y][entrance_x] != '.':
            entrance_x = random.randint(1, self.width - 2)
            entrance_y = random.randint(1, self.height - 2)
        self.dungeon[entrance_y][entrance_x] = 'E'

    def setup_display(self):
        pygame.init()
        screen_width = self.width * self.TILE_SIZE
        screen_height = self.height * self.TILE_SIZE
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("D&D Dungeon")

    def draw_dungeon(self):
        self.screen.fill(self.BLACK)
        for y, row in enumerate(self.dungeon):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                if cell == '#':
                    pygame.draw.rect(self.screen, self.GRAY, rect)
                elif cell == '.':
                    pygame.draw.rect(self.screen, self.WHITE, rect)
                elif cell == 'E':
                    pygame.draw.rect(self.screen, self.BROWN, rect)
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)  # Draw cell borders
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_dungeon()
        pygame.quit()

def main():
    print("Welcome to the D&D Dungeon Generator!")
    width = int(input("Enter the width of the dungeon: "))
    height = int(input("Enter the height of the dungeon: "))
    
    dungeon_gen = DungeonGenerator(width, height)
    dungeon_gen.create_dungeon()
    dungeon_gen.setup_display()
    dungeon_gen.run()

if __name__ == "__main__":
    main()
