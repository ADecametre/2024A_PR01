import math
import pygame
from config import *

class PacMan:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self._pos = PACMAN_START_POS
        self.speed = PACMAN_SPEED
        self.size = PACMAN_SIZE  # Size of Pac-Man (radius)
        self.color = (255, 255, 0)  # Yellow color for Pac-Man # NOTE Amazing
        self.size_grid = (TILE_WIDTH, TILE_HEIGHT)
        self.premove_direction = None
        self.direction = None
        self.frame_count = 0 # ?
        self.mouth_open_angle = 45  # Angle of the mouth opening (in degrees) # NOTE Totally useful :)
        self.lives = 3
        #self.screen_pos = grid_to_screen(grid_pos=[self.x, self.y], tile_size=[self.size_grid, self.size_grid])
        self._rect = pygame.Rect(grid_to_screen(self.pos), self.size)
    
    @property
    def pos(self): return self._pos
    
    @pos.setter
    def pos(self, value):
        self._pos = value
        self._rect.topleft = grid_to_screen(self.pos)
        
    @property
    def rect(self): return self._rect
        
    def draw(self):
        # Load the Pac-Man image
        pacman_image = pygame.image.load('assets/images/pacman.png')
        pacman_image = pygame.transform.scale(pacman_image, self.size)

        # Rotate the image based on the direction
        if self.direction is None or self.direction == (1, 0):  # Default to the right
            rotated_image = pacman_image
        elif self.direction == (-1, 0):  # Left
            rotated_image = pygame.transform.rotate(pacman_image, 180)
        elif self.direction == (0, -1):  # Down
            rotated_image = pygame.transform.rotate(pacman_image, 90)
        elif self.direction == (0, 1):  # Up
            rotated_image = pygame.transform.rotate(pacman_image, 270)

        # Calculate the screen position of Pac-Man
        x, y = self.pos
        grid_w, grid_h = self.size_grid
        screen_x = float(x) * grid_w
        screen_y = float(y) * grid_h

        # Draw the rotated image at the current position
        self.screen.blit(rotated_image, (screen_x, screen_y))
        
    def check_collision(self, new_pos):
        new_x, new_y = new_pos
        functions = [math.floor, math.ceil]
        for fn1 in functions:
            for fn2 in functions:
                if(self.board[fn1(new_y)][fn2(new_x)]):
                    return False
        return True
    
    def calculate_new_pos(self, vect):
        if(vect == None): return None
        x, y = self.pos
        dx, dy = vect
        new_pos = x + dx * self.speed, y + dy * self.speed
        return new_pos if self.check_collision(new_pos) else None

    def move(self):
            # [x] Extraire la direction de déplacement à partir de l'attribut `self.direction`.
            # vect = self.direction
            # [x] Calculer les nouvelles coordonnées X et Y en fonction de la direction
            # Ajouter la direction à la position actuelle (self.x, self.y) pour obtenir la nouvelle position.
            # [x] Vérifier si la nouvelle position entre en collision avec un mur
            # Utiliser `self.board[new_y][new_x]` pour voir si la case correspond à un chemin (0) ou à un mur (1).
                # [x] Mettre à jour la position de Pac-Man si aucun mur n'est rencontré
                # [x] Convertir les nouvelles coordonnées de la grille en position à l'écran
                # Utiliser une fonction comme `grid_to_screen` pour obtenir les coordonnées sur l'écran.
                # [x] Mettre à jour la position du rectangle de Pac-Man dans l'interface
                # Mettre à jour `self.rect.topleft` avec la nouvelle position à l'écran pour déplacer l'affichage de Pac-Man.
        
        new_pos = None
        directions = [self.premove_direction, self.direction]
        
        for d in directions:
            if d:
                new_pos = self.calculate_new_pos(d)
                if(new_pos):
                    self.direction = d
                    self.pos = new_pos
                    return

    def stop(self):
        self.direction = self.premove_direction = None

    def reset(self):
        self.pos = PACMAN_START_POS
        self.stop()

    def die(self):

        if self.lives == 0:
            # Game over
            return True
        
        # Reduce the number of lives
        self.lives -= 1

        self.reset()