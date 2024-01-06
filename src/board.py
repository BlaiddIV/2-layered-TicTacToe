class TicTacToe_Board_2_layers:
    """
    Represents a 2-layered Tic-Tac-Toe board. In the project, the large TicTacToe field, that is, 
    the one on the first level, is referred to as the outer field, and the TicTacToe fields in the 
    cells of the large TicTacToe field, i.e., the TicTacToe fields within the TicTacToe field (second level), 
    are referred to as the inner field.
    
    Note: For a better understanding of the code, it may be helpful to familiarize yourself with the rules of the game.
          To view the rules, you could search for "meta-TicTacToe" on Wikipedia or read the README.

    Attributes:
        EMPTY_CELL (str): Represents an empty cell on the board.
        PLAYER_X (str): Represents player X.
        PLAYER_O (str): Represents player O.
        DRAW_SYMBOL (str) : Represents a draw in an inner field.
        POSITIONS_MAPPING_DICT (dict): Dictionary mapping each outer field position (str) to its numeric positions (Tuple).
        OUTER_FIELD_POSITIONS (list): List of positions for the outer field.
        board_status (dict): Dictionary to store the status of each position on the board.
        where_to_play_next: Represents the position in the outer field where the next move should be made.
        active_player (str): Represents the player (either 'X' or 'O') who is currently making a move.
    """

    EMPTY_CELL = ''
    
    PLAYER_X = 'X'
    PLAYER_O = 'O'
    DRAW_SYMBOL = "D"
    
    POSITIONS_MAPPING_DICT = {
            'top-left': (0, 0),
            'top-mid': (0, 1),
            'top-right': (0, 2),
            'mid-left': (1, 0),
            'mid-mid': (1, 1),
            'mid-right': (1, 2),
            'bottom-left': (2, 0),
            'bottom-mid': (2, 1),
            'bottom-right': (2, 2)
        }

    # Constructor.
    def __init__(self):
        """
        Initialize the 2-layered Tic-Tac-Toe board.

        Each position on the board is a 3x3 grid, and the outer field consists of nine such positions.
        The board is represented as a dictionary with outer field positions as keys and 3x3 grids as values.
        Each grid contains empty cells initially.

        Usage:
            tic_tac_toe_board = TicTacToe_Board_2_layers()
        """

        # List of positions for the outer field.
        self.OUTER_FIELD_POSITIONS = ["top-left", "top-mid", "top-right",
                                      "mid-left", "mid-mid", "mid-right",
                                      "bottom-left", "bottom-mid", "bottom-right"]

        # Initialize the board status with empty cells.
        self.board_status = {position: [[self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL],
                                        [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL],
                                        [self.EMPTY_CELL, self.EMPTY_CELL, self.EMPTY_CELL]]
                             for position in self.OUTER_FIELD_POSITIONS}
        
        # Represents the position in the outer field where the next move should be made.
        self.where_to_play_next = None
        
        # Represents the player who is currently making a move.
        self.active_player = self.PLAYER_X  # Start with player X.
        
    def is_inner_field_full(self, pos_outer_field) -> bool:
        """
        Check if the specified inner field is full. This would cause a draw.

        Args:
            pos_outer_field (str): The position in the outer field.

        Returns:
            bool: True if the inner field is full, False otherwise.

        Usage:
            is_full = tic_tac_toe_board.is_inner_field_full('top-left')
        """
        # Check if the inner field is already won or a draw.
        if type(self.board_status[pos_outer_field]) == str:
            return False
        
        # Check if every cell in the specified inner field is filled. 
        else:     
            return all([all([inner_cell != self.EMPTY_CELL for inner_cell in inner_row]) for inner_row in self.board_status[pos_outer_field]])
    
    def is_outer_field_full(self) -> bool:
        """
        Check if the entire outer field is full. This would cause an overall draw.

        Returns:
            bool: True if the entire outer field is full, False otherwise.

        Usage:
            is_full = tic_tac_toe_board.is_outer_field_full()
        """
        # Check if every cell on the outer field is won (full).
        return all([self.is_cell_of_outer_field_won(pos_outer_field) for pos_outer_field in self.board_status.keys()])
   
    def update_where_to_play_next(self, row_inner_field, col_inner_field):   
        """
        Update the 'where_to_play_next' attribute based on the inner field position specified in the last made move.

        Args:
            row_inner_field (int): The row index of the inner field from last move.
            col_inner_field (int): The column index of the inner field from last move.

        Usage:
            tic_tac_toe_board.update_where_to_play_next(row_inner_field, col_inner_field)
        """
        # Iterate through the POSITIONS_MAPPING_DICT to find the outer position for the next move corresponding to the given inner field position.
        for key, value in self.POSITIONS_MAPPING_DICT.items():
            if value == (row_inner_field, col_inner_field):
                self.where_to_play_next = key
                break
    
    def mark_outer_cell_as_won(self, player, pos_outer_field):
        """
        Mark the specified outer cell as won by the given player.

        Args:
            player (str): The player who won the inner field ('X' or 'O').
            pos_outer_field (str): The position in the outer field.

        Usage:
            tic_tac_toe_board.mark_outer_cell_as_won('X', 'top-left')
        """
        if player == self.PLAYER_X:
            self.board_status[pos_outer_field] = self.PLAYER_X

        elif player == self.PLAYER_O:
            self.board_status[pos_outer_field] = self.PLAYER_O
            
    def mark_outer_field_as_draw(self, pos_outer_field):
        """
        Mark the specified inner field as a draw.

        Args:
            pos_outer_field (str): The position in the outer field.

        Usage:
            tic_tac_toe_board.mark_outer_field_as_won('X', 'top-left')
        """
        self.board_status[pos_outer_field] = self.DRAW_SYMBOL
    
    def is_cell_of_outer_field_won(self, pos_outer_field) -> bool:
        """
        Check if the entire inner field is won.

        Args:
            pos_outer_field (str): The position of the outer field.

        Returns:
            bool: True if the outer field is won, False otherwise.

        Usage:
            is_won = tic_tac_toe_board.is_cell_of_outer_field_won('top-left')
        """
        # If the outer field is won, the structure of board.status has changed, 
        # and the value associated with its key is no longer a two-dimensional list. 
        # It would be set to either 'X' or 'O'. Therefore, the value associated with 
        # the key "pos_outer_field" would be a string.
        return False if type(self.board_status[pos_outer_field]) == list else True
            
    def is_cell_of_inner_field_empty(self, pos_outer_field, row_inner_field, col_inner_field) -> bool:
        """
        Check if a cell in the inner field is empty.

        Args:
            pos_outer_field (str): The position in the outer field.
            row_inner_field (int): The row index of the inner field.
            col_inner_field (int): The column index of the inner field.

        Returns:
            bool: True if the cell is empty, False otherwise.

        Usage:
            is_empty = tic_tac_toe_board.is_cell_of_inner_field_empty('top-left', 1, 1)
        """
        
        # Check if the outer field is won, as in that case, the structure of board.status has changed, 
        # and the value associated with its key is no longer a two-dimensional list. 
        # It would be set to either 'X' or 'O'.
        if not self.is_cell_of_outer_field_won(pos_outer_field):
            return self.board_status[pos_outer_field][row_inner_field][col_inner_field] == ''  
        else:
            return False
    
    def make_move(self, player, pos_outer_field, row_inner_field, col_inner_field):
        """
        Update the board status based on the inner field where the player made their move.

        Args:
            player (str): The player making the move ('X' or 'O').
            pos_outer_field (str): The position in the outer field.
            row_inner_field (int): The row index of the inner field.
            col_inner_field (int): The column index of the inner field.
            
        Raises:
            ValueError: If the player is not 'X' or 'O'.
            ValueError: If the outer field position is invalid.
            ValueError: If the inner field position is invalid.

        Usage:
            tic_tac_toe_board.make_move('X', 'top-left', 1, 1)
        """
        # Validate player.
        if player not in (self.PLAYER_X, self.PLAYER_O):
            raise ValueError("Invalid player. Player must be 'X' or 'O'.")

        # Validate outer field position.
        if pos_outer_field not in self.OUTER_FIELD_POSITIONS:
            raise ValueError("Invalid outer field position.")

        # Validate inner field position
        if not (0 <= row_inner_field < 3 and 0 <= col_inner_field < 3):
            raise ValueError("Invalid inner field position. Row and column indices must be between 0 and 2.")

        # Check if the selected cell is empty before making a move
        if not self.is_cell_of_inner_field_empty(pos_outer_field, row_inner_field, col_inner_field):
            raise ValueError("Selected cell is not empty. Choose an empty cell for the move.")
        
        if player == self.PLAYER_X:
            self.board_status[pos_outer_field][row_inner_field][col_inner_field] = "X"

        elif player == self.PLAYER_O:
            self.board_status[pos_outer_field][row_inner_field][col_inner_field] = "O"
        
    def check_for_draw_inner_field(self, pos_outer_field) -> bool:
        """
        Check for a draw in the specified inner field.

        Args:
            pos_outer_field (str): The position in the outer field.

        Returns:
            bool: True if the inner field is a draw, False otherwise.

        Usage:
            is_draw = tic_tac_toe_board.check_for_draw_inner_field('top-left')
        """
        # Check if the inner field is full and if there is no winner.
        return self.is_inner_field_full(pos_outer_field) and not self.check_for_win_inner_field(pos_outer_field)
    
    def check_for_draw_outer_field(self) -> bool:
        """
        Check for a draw in the outer field.

        Returns:
            bool: True if the outer field is a draw, False otherwise.

        Usage:
            is_draw = tic_tac_toe_board.check_for_draw_outer_field()
        """
        # Check if the outer field is full and if there is no winner.
        return self.is_outer_field_full() and not self.check_for_win_outer_field()
    
    def check_for_win_inner_field(self, pos_outer_field) -> str:
        """
        Check for a winner in the specified inner field.

        Args:
            pos_outer_field (str): The position in the outer field.

        Returns:
            str: The winner symbol ('X' or 'O') if there is a winner, otherwise None.

        Usage:
            winner = tic_tac_toe_board.check_for_win_inner_field('top-left')
        """
        # Retrieve the specified inner field.
        check_this_inner_field = self.board_status[pos_outer_field]

        # Check for a winner in horizontal and vertical lines.
        for i in range(3):
            if check_this_inner_field[i][0] == check_this_inner_field[i][1] == check_this_inner_field[i][2] != self.EMPTY_CELL:
                return check_this_inner_field[i][0]  # Winner in horizontal line.

            if check_this_inner_field[0][i] == check_this_inner_field[1][i] == check_this_inner_field[2][i] != self.EMPTY_CELL:
                return check_this_inner_field[0][i]  # Winner in vertical line.

        # Check for a winner in diagonal lines.
        if check_this_inner_field[0][0] == check_this_inner_field[1][1] == check_this_inner_field[2][2] != self.EMPTY_CELL:
            return check_this_inner_field[0][0]  # Winner in the main diagonal.

        if check_this_inner_field[0][2] == check_this_inner_field[1][1] == check_this_inner_field[2][0] != self.EMPTY_CELL:
            return check_this_inner_field[0][2]  # Winner in the secondary diagonal.

        return None  # No winner.
    
    def check_for_win_outer_field(self) -> str:
        """
        Check for an overall winner in the outer field.

        Returns:
            str: The winner symbol ('X' or 'O') if there is a winner, otherwise None.

        Usage:
            winner = tic_tac_toe_board.check_for_win_outer_field()
        """
        # Define the lines to check for a winner in the outer field; horizontal, vertical or diagonal winner.
        lines_to_check = [['top-left', 'top-mid', 'top-right'],
                          ['mid-left', 'mid-mid', 'mid-right'],
                          ['bottom-left', 'bottom-mid', 'bottom-right'],
                          ['top-left', 'mid-left', 'bottom-left'],
                          ['top-mid', 'mid-mid', 'bottom-mid'],
                          ['top-right', 'mid-right', 'bottom-right'],
                          ['top-left', 'mid-mid', 'bottom-right'],
                          ['top-right', 'mid-mid', 'bottom-left']]

        # Check each line for a winner in the outer field.
        for line in lines_to_check:
            if (all([type(self.board_status[outer_cell]) is not list for outer_cell in line])) and (self.board_status[line[0]] == self.board_status[line[1]] == self.board_status[line[2]]) and self.board_status[line[0]] != self.DRAW_SYMBOL:
                return self.board_status[line[0]]  # Winner

        return None  # No winner.