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

# Colors for lines and player/draw symbols on the board.
OUTER_FIELD_LINE_COLOR = (68, 204, 221)
INNER_FIELD_LINE_COLOR = (85, 17, 55)
PLAYER_X_COLOR = (68, 238, 34)
PLAYER_O_COLOR = (238, 170, 85)
DRAW_SYMBOL_COLOR = (255, 0, 0)

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
def draw_game_board(no_needed_inner_fields):
    """
    Draw the entire game board, including outer and inner fields, on the game screen.

    Args:
        no_needed_inner_fields (list): A list of outer field positions that have already been won and do not need to be drawn.

    Usage:
        draw_game_board(['top-left', 'top-mid', ...])

    Note:
        This function assumes the existence of certain global variables, such as `game_screen`, `BACKGROUND_IMAGE`,
        `OUTER_FIELD_LINE_COLOR`, `OUTER_LINE_THICKNESS`, `GRID_REFERENCE_POINTS`, and others. Ensure these variables
        are defined before calling this function.
    """
    # Draw the background.
    game_screen.blit(BACKGROUND_IMAGE, (0, 0)) 
    
    # ~~~~~~~~~~~~~~ Start Draw inner field (white) ~~~~~~~~~~~~~~ #
    # Draw the inner fields 9x based on the reference points in "GRID_REFERENCE_POINTS." 
    # Each field is drawn individually, as they need to be modified independently during the game.
    for pos_outer_field in active_game_board.OUTER_FIELD_POSITIONS:
        # Only draw inner fields that have not been won yet. If so, this cell only needs a player or draw symbol.
        if pos_outer_field not in no_needed_inner_fields:
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
    
    # Draw all player-pick symbols by looping through (only small symbols in inner fields).
    for pos_outer_field in active_game_board.OUTER_FIELD_POSITIONS:
        inner_field = active_game_board.board_status[pos_outer_field]
        # Check if the inner field has not been won or is not a draw yet. If yes, it is represented by a list (game field not finished).
        if type(inner_field) == list:
            for row_inner_field in range(3):
                for col_inner_field in range(3):
                    # Check which player symbol is in the current cell.
                    if inner_field[row_inner_field][col_inner_field] == active_game_board.PLAYER_X:
                        draw_player_symbol(game_screen, (pos_outer_field, row_inner_field, col_inner_field), active_game_board.PLAYER_X)
                    elif inner_field[row_inner_field][col_inner_field] == active_game_board.PLAYER_O:
                        draw_player_symbol(game_screen, (pos_outer_field, row_inner_field, col_inner_field), active_game_board.PLAYER_O)
        # Inner field is already won. Draw a bigger player symbol.              
        elif type(inner_field) == str and inner_field in [active_game_board.PLAYER_O, active_game_board.PLAYER_X]:
            draw_inner_field_win(game_screen, pos_outer_field, inner_field)
        # Inner field is a draw. Draw a big draw symbol.    
        elif type(inner_field) == str and inner_field == active_game_board.DRAW_SYMBOL:
            draw_inner_field_draw(game_screen, pos_outer_field)
    
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
        
def draw_player_symbol(game_screen, coordinates, player):
    """
    Draw the symbol for the specified player at the given coordinates on the game screen.

    Args:
        game_screen (pygame.Surface): The game screen surface.
        coordinates (tuple): Tuple containing the outer field position and inner field indices (pos_outer_field, row_inner_field, col_inner_field).
        player (str): The player symbol ('X' or 'O').

    Usage:
        draw_player_symbol(game_screen, ('top-left', 1, 1), 'X')
    """
    pos_outer_field, row_inner_field, col_inner_field = coordinates
    
    reference_point = GRID_REFERENCE_POINTS[pos_outer_field]
    
    if player == active_game_board.PLAYER_X:
        # Draw an 'X' symbol for Player X with respect to the reference point in the outer field. Added some constants for better looking (no overlap with field lines).
        pygame.draw.line(game_screen, PLAYER_X_COLOR, (reference_point[0] + CELL_SIZE_INNER_FIELD * col_inner_field + 2.5, reference_point[1] + CELL_SIZE_INNER_FIELD * row_inner_field + 2.5), 
                         (reference_point[0] + CELL_SIZE_INNER_FIELD * (col_inner_field + 1) - 2.5, reference_point[1] + CELL_SIZE_INNER_FIELD * (row_inner_field + 1) - 2.5), PLAYERS_SYMBOL_THICKNESS)
        
        pygame.draw.line(game_screen, PLAYER_X_COLOR, (reference_point[0] + CELL_SIZE_INNER_FIELD * (col_inner_field + 1) - 2.5, reference_point[1] + CELL_SIZE_INNER_FIELD * row_inner_field + 2.5), 
                         (reference_point[0] + CELL_SIZE_INNER_FIELD * col_inner_field + 2.5, reference_point[1] + CELL_SIZE_INNER_FIELD * (row_inner_field + 1) - 2.5), PLAYERS_SYMBOL_THICKNESS)
    
    elif player == active_game_board.PLAYER_O:
        # Draw an 'O' symbol for Player O with respect to the reference point in the outer field. Scaling the radius a bit for a better looking (no overlap with field lines).
        pygame.draw.circle(game_screen, PLAYER_O_COLOR, (reference_point[0] + CELL_SIZE_INNER_FIELD * col_inner_field + CELL_SIZE_INNER_FIELD // 2, 
                                                         reference_point[1] + CELL_SIZE_INNER_FIELD * row_inner_field + CELL_SIZE_INNER_FIELD // 2), CELL_SIZE_INNER_FIELD // 2.1, PLAYERS_SYMBOL_THICKNESS)
        
def draw_inner_field_win(game_screen, pos_outer_field, player):
    """
    Draw a winning symbol in the inner field.

    Parameters:
        game_screen (pygame.Surface): The surface to draw on.
        pos_outer_field (str): The position of the outer field.
        player (str): The player who won the inner field (active_game_board.PLAYER_X or active_game_board.PLAYER_O).
    
    Usage:
        draw_inner_field_win(game_screen, 'top-left', 'X')
    """
    # Retrieve the reference point for drawing based on the outer field position.
    reference_point = GRID_REFERENCE_POINTS[pos_outer_field]

    # Check which player has won the inner field and draw the corresponding symbol.
    if player == active_game_board.PLAYER_X:
        # Draw an X symbol for Player X.
        pygame.draw.line(game_screen, PLAYER_X_COLOR, (reference_point[0], reference_point[1]), 
                         (reference_point[0] + CELL_SIZE_OUTER_FIELD, reference_point[1] + CELL_SIZE_OUTER_FIELD), 3)
        
        pygame.draw.line(game_screen, PLAYER_X_COLOR, (reference_point[0], reference_point[1] + CELL_SIZE_OUTER_FIELD), 
                         (reference_point[0] + CELL_SIZE_OUTER_FIELD, reference_point[1]), PLAYERS_SYMBOL_THICKNESS)
    
    elif player == active_game_board.PLAYER_O:
        # Draw a circle symbol for Player O.
        pygame.draw.circle(game_screen, PLAYER_O_COLOR, (reference_point[0] + CELL_SIZE_OUTER_FIELD // 2, 
                                                  reference_point[1] + CELL_SIZE_OUTER_FIELD // 2), CELL_SIZE_OUTER_FIELD // 2, PLAYERS_SYMBOL_THICKNESS)

        
def draw_inner_field_draw(game_screen, pos_outer_field):
    """
    Draw a 'D' symbol for a draw in the inner field.

    Parameters:
        game_screen (pygame.Surface): The surface to draw on.
        pos_outer_field (str): The position of the outer field.
        
    Usage:
        draw_inner_field_win(game_screen, 'top-left')
    """
    # Retrieve the reference point for drawing based on the outer field position.
    reference_point = GRID_REFERENCE_POINTS[pos_outer_field]

    # Set the font for the 'D' symbol.
    font = pygame.font.Font(None, CELL_SIZE_OUTER_FIELD)

    # Render the 'D' symbol.
    draw_text = font.render(active_game_board.DRAW_SYMBOL, True, DRAW_SYMBOL_COLOR)  # White color

    # Get the rect object to center the 'D' symbol in the inner field.
    draw_rect = draw_text.get_rect(center=(reference_point[0] + CELL_SIZE_OUTER_FIELD // 2, reference_point[1] + CELL_SIZE_OUTER_FIELD // 2))

    # Blit the 'D' symbol onto the game screen.
    game_screen.blit(draw_text, draw_rect)

                       
def draw_winner_screen(winner):
    """
    Draw the winner screen with the specified winner.

    Args:
        winner (str): Symbol of the winning player ('X' or 'O').

    Usage:
        draw_winner_screen('X')
    """
    # Fill the screen with white color.
    game_screen.fill((255, 255, 255))

    # Set up the font.
    font = pygame.font.Font(None, 75)

    # Render the text with the winner information.
    text = font.render(f"Player {winner} wins!", True, (0, 0, 0))

    # Get the rectangle of the text and center it on the screen.
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    
    # Draw the text on the screen.
    game_screen.blit(text, text_rect)

    # Update the display.
    pygame.display.update()
    
    # Display the winner screen for a configurable duration (in milliseconds).
    display_duration = 5000  # 5 seconds
    start_time = pygame.time.get_ticks()

    # Give the player the option to quit early.
    while pygame.time.get_ticks() - start_time < display_duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
def draw_draw_screen():
    """
    Draws the screen for a draw.

    Usage:
        draw_draw_screen()
    """
    # Fill the screen with white color.
    game_screen.fill((255, 255, 255))

    # Set up the font.
    font = pygame.font.Font(None, 75)

    # Render the text for a draw.
    text = font.render("It's a draw!", True, (0, 0, 0))

    # Get the rectangle of the text and center it on the screen.
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    
    # Draw the text on the screen.
    game_screen.blit(text, text_rect)

    # Update the display.
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
    # Keep track of won inner fields because they should not be drawn anymore.
    no_needed_inner_fields = []
    
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
                pos_outer_field, row_inner_field, col_inner_field = transformed_board_indices
                
                # Check if the outer field cell is already won. If so, the player can choose any inner field.
                if active_game_board.where_to_play_next != None and active_game_board.is_cell_of_outer_field_won(active_game_board.where_to_play_next):
                    active_game_board.where_to_play_next = None
                
                # Check if the clicked cell is valid and not already occupied.
                if (pos_outer_field == active_game_board.where_to_play_next or active_game_board.where_to_play_next == None) and active_game_board.is_cell_of_inner_field_empty(pos_outer_field, row_inner_field, col_inner_field):
                    # Update game board by given move.
                    active_game_board.make_move(
                        active_game_board.active_player,
                        pos_outer_field,
                        row_inner_field,
                        col_inner_field,
                    )
                    
                    # Check if the inner field is won, and if so, update the board by placing the player's symbol in the game state.
                    winner_inner_field = active_game_board.check_for_win_inner_field(pos_outer_field)
                    if winner_inner_field != None:
                        active_game_board.mark_outer_cell_as_won(active_game_board.active_player, pos_outer_field)
                        no_needed_inner_fields.append(pos_outer_field)  
                    
                    # Check if the inner field is a draw, and if so, update the board by putting a "D" in the active board.
                    if active_game_board.board_status[pos_outer_field] != active_game_board.DRAW_SYMBOL and active_game_board.is_inner_field_full(pos_outer_field):
                        active_game_board.mark_outer_field_as_draw(pos_outer_field)
                        no_needed_inner_fields.append(pos_outer_field)  
                    
                    # Update the 'where_to_play_next' attribute, based on previous move.
                    active_game_board.update_where_to_play_next(row_inner_field, col_inner_field)

                    # Change the active player after valid move.
                    active_game_board.active_player = active_game_board.PLAYER_O if active_game_board.active_player == active_game_board.PLAYER_X else active_game_board.PLAYER_X
                   
        # Update the game screen.   
        draw_game_board(no_needed_inner_fields)
        
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
            break

    # Stop the game.
    pygame.quit()
    sys.exit()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End Game loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Start the game.
if __name__ == "__main__":
    main()
