import pytest
import src.board as board 

@pytest.fixture
def new_board():
    return board.TicTacToe_Board_2_layers()