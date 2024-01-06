import pytest

def test_initial_state(new_board):
    assert new_board.active_player == 'X'
    assert new_board.where_to_play_next is None

@pytest.mark.parametrize("player, outer_field, row, col", [('X', 'top-left', 1, 1), ('O', 'top-mid', 2, 2),])
def test_make_move(new_board, player, outer_field, row, col):
    new_board.make_move(player, outer_field, row, col)
    assert new_board.board_status[outer_field][row][col] == player

def test_invalid_player_raises_error(new_board):
    with pytest.raises(ValueError, match="Invalid player. Player must be 'X' or 'O'."):
        new_board.make_move('Y', 'top-left', 1, 1)

def test_invalid_outer_field_raises_error(new_board):
    with pytest.raises(ValueError, match="Invalid outer field position."):
        new_board.make_move('X', 'left-top', 1, 1)

def test_invalid_inner_field_position_raises_error(new_board):
    with pytest.raises(ValueError, match="Invalid inner field position. Row and column indices must be between 0 and 2."):
        new_board.make_move('X', 'top-left', 3, 1)

def test_non_empty_cell_raises_error(new_board):
    new_board.make_move('X', 'top-left', 1, 1)
    with pytest.raises(ValueError, match="Selected cell is not empty. Choose an empty cell for the move."):
        new_board.make_move('O', 'top-left', 1, 1)

@pytest.mark.parametrize("outer_field, moves, expected_winner", [('top-left', [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (2, 2)], 'X'), ('bottom-right', [(2, 2), (1, 2), (2, 1), (1, 1), (2, 0)], 'O'),])
def test_check_for_win_inner_field(new_board, outer_field, moves, expected_winner):
    for move in moves:
        new_board.make_move('X' if len(moves) % 2 == 0 else 'O', outer_field, move[0], move[1])
    assert new_board.check_for_win_inner_field(outer_field) == expected_winner

def test_check_for_win_outer_field(new_board):
    new_board.mark_outer_cell_as_won('X', 'top-left')
    new_board.mark_outer_cell_as_won('X', 'top-mid')
    new_board.mark_outer_cell_as_won('X', 'top-right')
    assert new_board.check_for_win_outer_field() == 'X'

def test_check_for_draw_inner_field(new_board):
    new_board.make_move('X', 'top-left', 0, 0)
    new_board.make_move('O', 'top-left', 0, 1)
    new_board.make_move('X', 'top-left', 0, 2)
    new_board.make_move('O', 'top-left', 1, 0)
    new_board.make_move('O', 'top-left', 1, 1)
    new_board.make_move('X', 'top-left', 1, 2)
    new_board.make_move('X', 'top-left', 2, 0)
    new_board.make_move('X', 'top-left', 2, 1)
    new_board.make_move('O', 'top-left', 2, 2)
    assert new_board.check_for_draw_inner_field('top-left')

def test_check_for_draw_outer_field(new_board):
    new_board.mark_outer_cell_as_won('X', 'top-left')
    new_board.mark_outer_cell_as_won('O', 'top-mid')
    new_board.mark_outer_cell_as_won('X', 'top-right')
    new_board.mark_outer_cell_as_won('O', 'mid-left')
    new_board.mark_outer_cell_as_won('O', 'mid-mid')
    new_board.mark_outer_cell_as_won('X', 'mid-right')
    new_board.mark_outer_cell_as_won('X', 'bottom-left')
    new_board.mark_outer_cell_as_won('X', 'bottom-mid')
    new_board.mark_outer_cell_as_won('O', 'bottom-right')
    assert new_board.check_for_draw_outer_field()
