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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start Setup everything ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Pygame initialization.
pygame.display.init()
pygame.font.init()

# Screen dimensions.
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000

# Cell sizes for outer and inner fields.
CELL_SIZE_OUTER_FIELD = SCREEN_WIDTH // 3
CELL_SIZE_INNER_FIELD = SCREEN_WIDTH // 9

# Colors for lines and player symbols on the board.
OUTER_FIELD_LINE_COLOR = (255, 0, 0)
INNER_FIELD_LINE_COLOR = (255, 255, 255)
PLAYER_X_COLOR = (0, 0, 255)
PLAYER_O_COLOR = (0, 255, 0)

# Thickness values for lines and player symbols on the board.
OUTER_LINE_THICKNESS = 5
INNER_LINE_THICKNESS = 2
PLAYERS_SYMBOL_THICKNESS = 3

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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Setup everything ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~~~~ Start Functions for drawing everything ~~~~~~~~~~~~~~~~~~~~~~~~ #
def draw_game_board():
    
    # Draw the background.
    game_screen.blit(BACKGROUND_IMAGE, (0, 0)) 
    
    # ~~~~~~~~~~~~~~ Start Draw inner field (white) ~~~~~~~~~~~~~~ #
    # Draw the inner fields 9x based on the reference points in "GRID_REFERENCE_POINTS." 
    # Each field is drawn individually, as they need to be modified independently during the game.
    for pos_outer_field in active_game_board.OUTER_FIELD_POSITIONS:
        reference_point = GRID_REFERENCE_POINTS[pos_outer_field]
        draw_inner_field(reference_point)
    # ~~~~~~~~~~~~~~~ End Draw inner field (white) ~~~~~~~~~~~~~~~ #
    
    # ~~~~~~~~~~~~~~~ Start Draw outer field (red) ~~~~~~~~~~~~~~~ #
    # Draw vertikal lines
    for x in range(SCREEN_WIDTH // 3, SCREEN_WIDTH - 1, SCREEN_WIDTH // 3): # The "-1" ensures that a third line is not drawn.
        pygame.draw.line(game_screen, OUTER_FIELD_LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT), OUTER_LINE_THICKNESS)
        
    # Draw horizontal lines
    for y in range(SCREEN_HEIGHT // 3, SCREEN_HEIGHT - 1, SCREEN_HEIGHT // 3): # The "-1" ensures that a third line is not drawn.
        pygame.draw.line(game_screen, OUTER_FIELD_LINE_COLOR, (0, y), (SCREEN_WIDTH, y), OUTER_LINE_THICKNESS)
    # ~~~~~~~~~~~~~~~~ End Draw outer field (red) ~~~~~~~~~~~~~~~~ #
     
    # Display all drawings on the game board. 
    pygame.display.update()

def draw_inner_field(reference_point):
    """
    Draw the lines of an inner field on the game screen.

    Draws both vertical and horizontal lines for a single inner field.

    Args:
        reference_point (tuple): The reference point (top-left corner) of the inner field. 
                                 This point helps determine in which cell of the outer field 
                                 the inner field should be drawn (coordinates on screen).

    Usage:
        draw_inner_field((x, y))
    """
    # Draw vertical lines
    for i in range(1, 3):
        x_position = reference_point[0] + i * CELL_SIZE_INNER_FIELD
        pygame.draw.line(game_screen, INNER_FIELD_LINE_COLOR, (x_position, reference_point[1]), (x_position, reference_point[1] + 3 * CELL_SIZE_INNER_FIELD), INNER_LINE_THICKNESS)

    # Draw horizontal lines
    for i in range(1, 3):
        y_position = reference_point[1] + i * CELL_SIZE_INNER_FIELD
        pygame.draw.line(game_screen, INNER_FIELD_LINE_COLOR, (reference_point[0], y_position), (reference_point[0] + 3 * CELL_SIZE_INNER_FIELD, y_position), INNER_LINE_THICKNESS)
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~ End Functions for drawing everything ~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start Game loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def main():
    """
    Main function to run the 2-layered-TicTacToe game loop.
    """
    game_is_active = True

    while game_is_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_active = False
                break
        
        # Update the game screen.   
        draw_game_board()

    # Stop the game.
    pygame.quit()
    sys.exit()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Game loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Start the game.
if __name__ == "__main__":
    main()
