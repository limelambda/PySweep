import pygame, os, sys, random, math
from pygame.locals import *

pygame.init()

class ColoredRect(pygame.Rect):
    def __init__(self, clr, *args):
        self.clr = clr
        super().__init__(*args)

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def main():
    WIDTH, HEIGHT = (pygame.display.Info().current_w//1.25, pygame.display.Info().current_h//1.25)
    print(WIDTH, HEIGHT)
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.Font(resource_path("assets/04B_30__.ttf"), 15)
    GRID_SIZE = (16, 16)
    grid = []
    grid_tile_scale = min(WIDTH  / (GRID_SIZE[0] + 1) // 1.25, HEIGHT / (GRID_SIZE[1] + 1) // 1.25)
    for y in range(GRID_SIZE[1]):  # Unfortunately iterable unpacking cannot be used in comprehension :(
        for x in range(GRID_SIZE[0]):
            grid.append(ColoredRect((155, 255, 155),
                                    WIDTH  / (GRID_SIZE[0] + 1) * (x + 1),
                                    HEIGHT / (GRID_SIZE[1] + 1) * (y + 1),
                                    grid_tile_scale,
                                    grid_tile_scale,
                                    ))
            grid[y * GRID_SIZE[1] + x].center = grid[y * GRID_SIZE[1] + x].topleft
    while True:
        WIDTH, HEIGHT = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        # upfate grid
        grid_tile_scale = min(WIDTH  / (GRID_SIZE[0] + 1) // 1.25, HEIGHT / (GRID_SIZE[1] + 1) // 1.25)
        for y in range(GRID_SIZE[1]):  # Unfortunately iterable unpacking cannot be used in comprehension :(
            for x in range(GRID_SIZE[0]):
                grid[y * GRID_SIZE[1] + x].center = (
                    WIDTH  / (GRID_SIZE[0] + 1) * (x + 1),
                    HEIGHT / (GRID_SIZE[1] + 1) * (y + 1),)
                grid[y * GRID_SIZE[1] + x].size = (grid_tile_scale, grid_tile_scale)
        m_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == MOUSEBUTTONUP:
                for tile in grid:
                    if tile.collidepoint(m_pos):
                        if event.button == 1:
                            if tile.clr != (255, 255, 155):
                                tile.clr = (155, 55, 55)
                        elif event.button == 3:
                            if tile.clr == (255, 255, 155):
                                tile.clr = (155, 255, 155)
                            else:
                                if tile.clr != (155, 55, 55):
                                    tile.clr = (255, 255, 155)
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(
            pygame.font.Font.render(FONT, str(m_pos), True, (255, 155, 155)),(5, 5),
        )
        for tile in grid:
            pygame.draw.rect(SCREEN, tile.clr, tile)
        pygame.display.flip()
        pygame.display.set_caption(f"PySweeper")

if __name__ == "__main__":
    main()