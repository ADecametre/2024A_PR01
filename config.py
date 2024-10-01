# parametre de l'ecran
from fractions import Fraction


screen_width = 800
screen_height = 800

# taille des tuiles
COLS = 16
ROWS = 16
TILE_WIDTH = screen_width / COLS
TILE_HEIGHT = screen_height / ROWS


# direction
class Direction:
    LEFT = (-TILE_WIDTH, 0)
    RIGHT = (TILE_WIDTH, 0)
    UP = (0, -TILE_HEIGHT)
    DOWN = (0, TILE_HEIGHT)
    STOP = (0, 0)


# Taille des fantômes
GHOST_SIZE = (45, 45)

# Taille du pacman
PACMAN_SIZE = (40, 40)

# position de depart
RESET_POS1 = [600, 350]
RESET_POS2 = [400, 350]
RESET_POS3 = [150, 350]
RESET_POS4 = [400, 400]

# Pacman start position
PACMAN_START_POS = (7, 9)

RANDOM_POS = [RESET_POS1, RESET_POS2, RESET_POS3, RESET_POS4]

# vitesse du ghost
GHOST_SPEED = 0.35/12
PACMAN_SPEED = Fraction(1, 12)
EDIBLE_GHOST_TIMER = 5

# fonction utilitaires
def grid_to_screen(grid_pos):
    screen_x = grid_pos[0] * TILE_WIDTH
    screen_y = grid_pos[1] * TILE_HEIGHT
    return screen_x, screen_y

import pygame

def recolor(img):
    COLOR = (220, 150, 200)
    img.fill(COLOR, special_flags=pygame.BLEND_RGB_MAX)
    return img