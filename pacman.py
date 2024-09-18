import math
import pygame
from config import *

class PacMan:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.x, self.y = PACMAN_START_POS
        self.speed = PACMAN_SPEED
        self.size = 40  # Size of Pac-Man (radius)
        self.color = (255, 255, 0)  # Yellow color for Pac-Man
        self.size_grid = 50  
        self.direction = None
        self.frame_count = 0
        self.changed_direction = None
        self.mouth_open_angle = 45  # Angle of the mouth opening (in degrees) # NOTE Totally useful :)
        self.lives = 3
        #self.screen_pos = grid_to_screen(grid_pos=[self.x, self.y], tile_size=[self.size_grid, self.size_grid])
        self.rect = pygame.Rect(self._get_screen_pos(), PACMAN_SIZE)

    def _get_screen_pos(self):
        return grid_to_screen(grid_pos=[self.x, self.y], tile_size=[self.size_grid, self.size_grid])
    
    def get_pos(self): return (self.x, self.y)
        
    def draw(self):
        # Load the Pac-Man image
        pacman_image = pygame.image.load('assets/images/pacman.png')
        pacman_image = pygame.transform.scale(pacman_image, (self.size, self.size))

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
        screen_x = float(self.x) * self.size_grid
        screen_y = float(self.y) * self.size_grid

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
    
    def calculate_new_pos(self, direction=None):
        if(direction==None): direction=self.direction
        return self.x + direction[0] * self.speed, self.y + direction[1] * self.speed
        

    def move(self):
        if self.direction:        
            # [x] Extraire la direction de déplacement à partir de l'attribut `self.direction`.
            # vect = self.direction
            
            # [x] Calculer les nouvelles coordonnées X et Y en fonction de la direction
            # Ajouter la direction à la position actuelle (self.x, self.y) pour obtenir la nouvelle position.
            new_pos = self.calculate_new_pos() #self.x + vect[0] * self.speed, self.y + vect[1] * self.speed

            # [x] Vérifier si la nouvelle position entre en collision avec un mur
            # Utiliser `self.board[new_y][new_x]` pour voir si la case correspond à un chemin (0) ou à un mur (1).
            if(self.check_collision(new_pos)):
                # [x] Mettre à jour la position de Pac-Man si aucun mur n'est rencontré
                self.x, self.y = new_pos

                # [x] Convertir les nouvelles coordonnées de la grille en position à l'écran
                # Utiliser une fonction comme `grid_to_screen` pour obtenir les coordonnées sur l'écran.

                # [x] Mettre à jour la position du rectangle de Pac-Man dans l'interface
                # Mettre à jour `self.rect.topleft` avec la nouvelle position à l'écran pour déplacer l'affichage de Pac-Man.
                self.rect.topleft = self._get_screen_pos()

    def set_direction(self, direction):
        self.direction = direction

    def stop(self):
        self.direction = None

    def reset(self):
        self.x, self.y = PACMAN_START_POS
        self.direction = None

    def die(self):

        if self.lives == 0:
            # Game over
            return True
        
        # Reduce the number of lives
        self.lives -= 1

        self.reset()