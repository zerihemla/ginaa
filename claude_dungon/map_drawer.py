import pygame
import threading

from map_defines import *



class MapDrawer():
    def __init__(self, map_arr, map_width, map_height, tile_size, wall_color = GRAY, open_color = WHITE, 
                 entrance_color = BROWN, hallway_color = LIGHT_GRAY, treasure_color = GOLD,
                 trap_color= RED, hole_color = BLACK, obstruction_color = BLUE):
        
        self.map_arr = map_arr
        self.tile_size = tile_size

        self.screen_width = map_width * tile_size
        self.screen_height = map_height * tile_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("D&D Dungeon")


        self.wall_color = wall_color
        self.open_color = open_color
        self.entrance_color = entrance_color
        self.hallway_color = hallway_color
        self.treasure_color = treasure_color
        self.trap_color = trap_color
        self.hole_color = hole_color
        self.obstruction_color = obstruction_color


    ######################################
    ####PUBLIC FUNCTIONS##################
    ######################################
    def display_map(self):
        display_thread = threading.Thread(target = self._display_loop, args=self)



    ######################################
    ####PRIVATE FUNCTIONS#################
    ######################################

    def _display_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BLACK)
            self._process_map()

        pygame.quit()


    def _process_map(self):
        self.screen.fill(BLACK)
        
        for y, row in enumerate(self.map_arr):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                if cell == WALL_CHAR:
                    pygame.draw.rect(self.screen, self.wall_color, rect)
                elif cell == OPEN_CHAR:
                    pygame.draw.rect(self.screen, self.open_color, rect)
                elif cell == ENTRANCE_CHAR:
                    pygame.draw.rect(self.screen, self.entrance_color, rect)
                elif cell == HALLWAY_CHAR:
                    pygame.draw.rect(self.screen, self.hallway_color, rect)
                elif cell == TREASURE_CHAR:
                    pygame.draw.rect(self.screen, self.treasure_color, rect)
                elif cell == TRAP_CHAR:
                    pygame.draw.rect(self.screen, self.trap_color, rect)
                elif cell == HOLE_CHAR:
                    pygame.draw.rect(self.screen, self.hole_color, rect)
                elif cell == OBSTRUCTION_CHAR:
                    pygame.draw.rect(self.screen, self.obstruction_color, rect)
                else:
                    pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1) 
        
        pygame.display.flip() # Draw cell borders

