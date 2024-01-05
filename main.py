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
OUTER_FIELD_LINE_COLOR = (68, 204, 221)
INNER_FIELD_LINE_COLOR = (85, 17, 55)
PLAYER_X_COLOR = (68, 238, 34)
PLAYER_O_COLOR = (238, 170, 85)

# Thickness values for lines and player symbols on the board.
OUTER_LINE_THICKNESS = 5
INNER_LINE_THICKNESS = 3
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
        
def draw_winner_screen(winner):
    """
    Draw the winner screen with the specified winner.

    Args:
        winner (str): Symbol of the winning player ('X' or 'O').

    Usage:
        draw_winner_screen('X')
    """
    # Fill the screen with white color
    game_screen.fill((255, 255, 255))

    # Set up the font
    font = pygame.font.Font(None, 75)

    # Render the text with the winner information
    text = font.render(f"Player {winner} wins!", True, (0, 0, 0))

    # Get the rectangle of the text and center it on the screen
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    
    # Draw the text on the screen
    game_screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()
    
def draw_draw_screen():
    """
    Draws the screen for a draw.

    Usage:
        draw_draw_screen()
    """
    # Fill the screen with white color
    game_screen.fill((255, 255, 255))

    # Set up the font
    font = pygame.font.Font(None, 75)

    # Render the text for a draw
    text = font.render("It's a draw!", True, (0, 0, 0))

    # Get the rectangle of the text and center it on the screen
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    
    # Draw the text on the screen
    game_screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()
# ~~~~~~~~~~~~~~~~~~~~~~~~~ End Functions for drawing everything ~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start helper functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def transform_coordinates_to_indices(x_coordinate, y_coordinate) -> tuple:
    """
    Transform pixel coordinates to indices for inner and outer fields.

    Args:
        x_coordinate (int): The x-coordinate of the pixel.
        y_coordinate (int): The y-coordinate of the pixel.

    Returns:
        tuple: A tuple containing the outer field position (str), row index of inner field (int), and column index of inner field (int).

    Usage:
        result = transform_coordinates_to_indices(x, y)
    """
    # Keep in mind that the y-coordinate corresponds to the row, and the x-coordinate corresponds to the column.
    # Calculate row and column indices for the inner field.
    row_inner_field = y_coordinate // CELL_SIZE_INNER_FIELD % 3
    col_inner_field = x_coordinate // CELL_SIZE_INNER_FIELD % 3

    # Calculate row and column indices for the outer field.
    row_outer_field = y_coordinate // CELL_SIZE_OUTER_FIELD
    col_outer_field = x_coordinate // CELL_SIZE_OUTER_FIELD

    # Find the corresponding outer field position (str) based on indices.
    str_outer_field = ""
    for key, value in active_game_board.POSITIONS_MAPPING_DICT.items():
        if value == (row_outer_field, col_outer_field):
            str_outer_field = key
            break

    # Return the result as a tuple.
    return (str_outer_field, row_inner_field, col_inner_field)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End helper functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start Game loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def main():
    """
    Main function to run the 2-layered-TicTacToe game loop.
    """
    game_is_active = True

    # Main game loop.
    while game_is_active:
        
        # Event handling loop.
        for event in pygame.event.get():
            
            # Quit event handling.
            if event.type == pygame.QUIT:
                game_is_active = False
                break
            
            # Mouse button down event handling. Player is picking a cell in the inner field.
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                
                # Get mouse coordinates from player pick.
                mouse_event_x = event.pos[0]
                mouse_event_y = event.pos[1]
                
                # Transform pixel coordinates to game board indices.
                transformed_board_indices = transform_coordinates_to_indices(mouse_event_x, mouse_event_y)
                
                # Check if the outer field cell is already won. If so, the player can choose any inner field.
                if active_game_board.where_to_play_next != None and active_game_board.is_cell_of_outer_field_won(active_game_board.where_to_play_next):
                    active_game_board.where_to_play_next = None
                
                # Check if the clicked cell is valid and not already occupied.
                if (transformed_board_indices[0] == active_game_board.where_to_play_next or active_game_board.where_to_play_next == None) and active_game_board.is_cell_of_inner_field_empty(transformed_board_indices[0], transformed_board_indices[1], transformed_board_indices[2]):
                    # Update game board by given move.
                    active_game_board.make_move(
                        active_game_board.active_player,
                        transformed_board_indices[0],
                        transformed_board_indices[1],
                        transformed_board_indices[2],
                    )
                    
                    # Check if the inner field is a draw, and if so, update the board by putting a "D" in the active board.
                    if active_game_board[transformed_board_indices[0]] != active_game_board.DRAW_SYMBOL and active_game_board.is_inner_field_full(transformed_board_indices[0]):
                        active_game_board.mark_outer_field_as_draw(transformed_board_indices[0])
                    
                    # Update the 'where_to_play_next' attribute, based on previous move.
                    active_game_board.update_where_to_play_next(transformed_board_indices[1], transformed_board_indices[2])

                    # Change the active player after valid move.
                    active_game_board.active_player = active_game_board.PLAYER_O if active_game_board.active_player == active_game_board.PLAYER_X else active_game_board.PLAYER_X
                   
        # Update the game screen.   
        draw_game_board()
        
        # Check if the entire game is a draw.
        if active_game_board.is_outer_field_full() and active_game_board.check_for_win_outer_field() == None:
            game_is_active = False
            draw_draw_screen()
            time.sleep(5)
            break
        
        # Check if one player has won the entire game.
        winner = active_game_board.check_for_win_outer_field()
        if winner != None:
            game_is_active = False
            draw_winner_screen(winner)
            time.sleep(5)
            break

    # Stop the game.
    pygame.quit()
    sys.exit()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Game loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Start the game.
if __name__ == "__main__":
    main()
