import random
import sys

from map_defines import *
from map_drawer import *

# Initialize Pygame



# Tile size
DEFAULT_TILE_SIZE = 20

DEFAULT_WIDTH = 50
DEFAULT_HEIGHT = 50

DEFAULT_MIN_NUM_ROOMS = 5
DEFAULT_MAX_NUM_ROOMS = 10

DEFAULT_MIN_ROOM_DIM = 3
DEFAULT_MAX_ROOM_DIM = 8

DEFAULT_MIN_NUM_TREASURE = 1
DEFAULT_MAX_NUM_TREASURE = 3

DEFAULT_MIN_NUM_TRAPS = 1
DEFAULT_MAX_NUM_TRAPS = 3

DEFAULT_MIN_NUM_HOLES = 1
DEFAULT_MAX_NUM_HOLES = 3

DEFAULT_MIN_NUM_OBSTRUCTIONS = 1
DEFAULT_MAX_NUM_OBSTRUCTIONS = 3




class GeneratedMap():
    def __init__(self, width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT, tile_size = DEFAULT_TILE_SIZE,
                 min_num_rooms = DEFAULT_MIN_NUM_ROOMS, max_num_rooms = DEFAULT_MAX_NUM_ROOMS,
                 min_room_dim = DEFAULT_MIN_ROOM_DIM, max_room_dim = DEFAULT_MAX_ROOM_DIM,
                 min_num_treasure = DEFAULT_MIN_NUM_TREASURE, max_num_treasure = DEFAULT_MAX_NUM_TREASURE,
                 min_num_traps = DEFAULT_MIN_NUM_TRAPS, max_num_traps = DEFAULT_MAX_NUM_TRAPS,
                 min_num_holes = DEFAULT_MIN_NUM_HOLES, max_num_holes = DEFAULT_MAX_NUM_HOLES,
                 min_num_obstructions = DEFAULT_MIN_NUM_OBSTRUCTIONS, max_num_obstructions = DEFAULT_MAX_NUM_OBSTRUCTIONS):
        self.map_arr = []
        self.room_sizes = []
        self.room_centers = []


        self.map_width = width
        self.map_height = height
        self.tile_size = tile_size
        
        self.min_num_rooms = min_num_rooms
        self.max_num_rooms = max_num_rooms

        self.min_room_dim = min_room_dim
        self.max_room_dim = max_room_dim

        self.min_num_treasure = min_num_treasure
        self.max_num_treasure = max_num_treasure

        self.min_num_traps = min_num_traps
        self.max_num_traps = max_num_traps

        self.min_num_holes = min_num_holes
        self.max_num_holes = max_num_holes

        self.min_num_obstructions = min_num_obstructions
        self.max_num_obstructions = max_num_obstructions

        #Variables that are generated randomly
        self.num_rooms = random.randint(self.min_num_rooms, self.max_num_rooms)
        self.num_treasure = random.randint(self.min_num_treasure, self.max_num_treasure)
        self.num_holes = random.randint(self.min_num_holes, self.max_num_holes)
        self.num_traps = random.randint(self.min_num_traps, self.max_num_traps)
        self.num_obstructions = random.randint(self.min_num_obstructions, self.max_num_obstructions)



    ######################################
    ####PUBLIC FUNCTIONS##################
    ######################################

    def generate_map(self):
        self._init_map()
        self._create_rooms()
        self._add_entrance()
        self._add_treasure()
        self._link_rooms()
        self._add_traps()
        self._add_holes()
        self._add_obstructions()


    def draw_map(self):
        drawn_map = MapDrawer(self.map_arr, self.map_width, self.map_height, self.tile_size)
        drawn_map.display_map()

    def print_raw(self):
        self._print_raw_map()
        self._print_data_structure()

    ######################################
    ####PRIVATE FUNCTIONS#################
    ######################################

    def _print_raw_map(self):
        for line in self.map_arr:
            for char in line:
                print(char, end = "")
            print("")
        print(f"\n\n")

    def _print_data_structure(self):
        print("Printing Data Structure!")
        self._print_data("map width", self.map_width)
        self._print_data("map height", self.map_height)
        print()
        self._print_data("tile size", self.tile_size)
        print()
        self._print_data("num rooms", self.num_rooms)
        self._print_data("num treasure", self.num_treasure)
        self._print_data("num traps", self.num_traps)
        self._print_data("num holes", self.num_holes)
        self._print_data("num obstructions", self.num_obstructions)
        print()
        self._print_data("min room dim", self.min_room_dim)
        self._print_data("max room dim", self.max_room_dim)
        print(f"\nRoom Sizes")
        print(self.room_sizes)
        print(f"\n Room Centers")
        print(self.room_centers)
        


    def _print_data(self, name, data):
        print(f"{name}:\t{data}")

    def _init_map(self):
        # Initialize map with walls
        self.map_arr = [[WALL_CHAR for _ in range(self.map_width)] for _ in range(self.map_height)]

    def _create_rooms(self):
        for _ in range(self.num_rooms):
            room_width = random.randint(self.min_room_dim, self.max_room_dim)
            room_height = random.randint(self.min_room_dim, self.max_room_dim)
            x = random.randint(1, self.map_width - room_width - 1)
            y = random.randint(1, self.map_height - room_height - 1)

            for i in range(y, y + room_height):
                for j in range(x, x + room_width):
                    self.map_arr[i][j] = OPEN_CHAR
            self.room_sizes.append((room_width, room_height))
            self.room_centers.append((x + room_width // 2, y + room_height // 2))


    def _add_entrance(self):
        self._replace_random_char(OPEN_CHAR, ENTRANCE_CHAR)

    def _add_treasure(self):
        for _ in range(self.num_treasure):
            self._replace_random_char(OPEN_CHAR, TREASURE_CHAR)

    def _add_traps(self):
        for _ in range(self.num_traps):
            self._replace_random_char(OPEN_CHAR, TRAP_CHAR)

    def _add_holes(self):
        for _ in range(self.num_holes):
            self._replace_random_char(OPEN_CHAR, HOLE_CHAR)

    def _add_obstructions(self):
        for _ in range(self.num_obstructions):
            self._replace_random_char(OPEN_CHAR, OBSTRUCTION_CHAR)


    def _replace_random_char(self, char_to_find, char_to_put, max_tries = 100):
        num_tries = 0

        while True:
            random_x = random.randint(1, self.map_width - 2)
            random_y = random.randint(1, self.map_height - 2)
            
            if self.map_arr[random_y][random_x] == char_to_find:
                self.map_arr[random_y][random_x] = char_to_put
                break
        
            if num_tries >= max_tries:
                break


    def _link_rooms(self):
        for i in range(len(self.room_centers) - 1):
            x1, y1 = self.room_centers[i]
            x2, y2 = self.room_centers[i + 1]
            if random.choice([True, False]):
                create_corridor(self.map_arr, x1, y1, x2, y1)
                create_corridor(self.map_arr, x2, y1, x2, y2)
            else:
                create_corridor(self.map_arr, x1, y1, x1, y2)
                create_corridor(self.map_arr, x1, y2, x2, y2)

    def _create_hallways(self, x1, y1, x2, y2):
        if x1 < x2:
            for x in range(x1, x2 + 1):
                self.map_arr[y1][x] = OPEN_CHAR
        elif x1 > x2:
            for x in range(x2, x1 + 1):
                self.map_arr[y1][x] = OPEN_CHAR
        if y1 < y2:
            for y in range(y1, y2 + 1):
                self.map_arr[y][x2] = OPEN_CHAR
        elif y1 > y2:
            for y in range(y2, y1 + 1):
                self.map_arr[y][x2] = OPEN_CHAR
    

def create_corridor(dungeon, x1, y1, x2, y2):
    if x1 < x2:
        for x in range(x1, x2 + 1):
            dungeon[y1][x] = '.'
    elif x1 > x2:
        for x in range(x2, x1 + 1):
            dungeon[y1][x] = '.'
    if y1 < y2:
        for y in range(y1, y2 + 1):
            dungeon[y][x2] = '.'
    elif y1 > y2:
        for y in range(y2, y1 + 1):
            dungeon[y][x2] = '.'


def create_dungeon(width, height):
    # Initialize dungeon with walls
    dungeon = [[WALL_CHAR for _ in range(width)] for _ in range(height)]

    room_centers = []
    # Create rooms
    num_rooms = random.randint(5, 10)
    for _ in range(num_rooms):
        room_width = random.randint(3, 8)
        room_height = random.randint(3, 8)
        x = random.randint(1, width - room_width - 1)
        y = random.randint(1, height - room_height - 1)

        for i in range(y, y + room_height):
            for j in range(x, x + room_width):
                dungeon[i][j] = '.'

        room_centers.append((x + room_width // 2, y + room_height // 2))

    # Create corridors
    for i in range(len(room_centers) - 1):
        x1, y1 = room_centers[i]
        x2, y2 = room_centers[i + 1]
        if random.choice([True, False]):
            create_corridor(dungeon, x1, y1, x2, y1)
            create_corridor(dungeon, x2, y1, x2, y2)
        else:
            create_corridor(dungeon, x1, y1, x1, y2)
            create_corridor(dungeon, x1, y2, x2, y2)

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
            if cell == WALL_CHAR:
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

def class_main():
    print("Running map class")
    map = GeneratedMap()
    map.generate_map()
    map.print_raw()
    map.draw_map()


if __name__ == "__main__":
    class_main()
