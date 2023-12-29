"""
2-layered-TicTacToe Game

This program implements a 2-layered-TicTacToe (also called meta-TicTacToe) game using the Pygame library. The game features an outer 
TicTacToe field divided into nine inner TicTacToe fields, forming a 3x3 grid. Players take turns making moves in 
the inner fields, and the goal is to win the game by achieving victory in the outer field.

The program uses the `TicTacToe_Board_2_layers` class from the `src.board` module to represent and manage the game board.

Note: For a better understanding of the code, it may be helpful to familiarize yourself with the rules of the game.
      To view the rules, you could search for "meta-TicTacToe" on Wikipedia or read the README.

Controls:
    - Click on an empty cell in the inner field to make a move.
    - The game ends when a player wins the outer field or when there is a draw.

Dependencies:
    - Pygame library
    - 'game_background.jpeg' image in the 'assets/images' directory for the game background.

Usage:
    - Ensure the Pygame library is installed (`pip install pygame`).
    - Run the script to start the 2-layered-TicTacToe game.
"""

from src.board import TicTacToe_Board_2_layers
import pygame
import sys
import time

# Pygame initialization.
pygame.display.init()
pygame.font.init()

# Screen dimensions.
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000

# Cell sizes for outer and inner fields.
CELL_SIZE_OUTER_FIELD = SCREEN_WIDTH // 3
CELL_SIZE_INNER_FIELD = SCREEN_WIDTH // 9

# Coordinates of grid reference points for cell positions (top left of a cell).
GRID_REFERENCE_POINTS = {
    f'{["top", "mid", "bottom"][row]}-{["left", "mid", "right"][col]}': (col * SCREEN_WIDTH // 3, row * SCREEN_HEIGHT // 3)
    for row in range(3)
    for col in range(3)
}

# Loading background image.
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('assets/images/game_background.jpeg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Pygame screen setup.
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2-layered-TicTacToe")

# Initialize the game board.
active_game_board = TicTacToe_Board_2_layers()

# Game loop.
def main():
    """
    Main function to run the 2-layered-TicTacToe game loop.
    """
    game_is_active = True

    while game_is_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_active = False

    # Stopping the game.
    pygame.quit()
    sys.exit()

# Starting the game.
if __name__ == "__main__":
    main()
