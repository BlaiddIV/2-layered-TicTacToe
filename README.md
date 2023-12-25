# Enhanced TicTacToe with Depth 2

## Description:
Welcome to the Enhanced TicTacToe with Depth 2 project! This Python-based game, implemented with PyGame, takes the classic TicTacToe to a whole new level by introducing an exciting twist. In this variation, each cell of the traditional TicTacToe grid contains an additional TicTacToe field, creating a multi-layered gaming experience – TicTacToes within TicTacToes.

## Motivation:
The motivation behind this project stems from the desire to inject strategic depth and excitement into the conventional TicTacToe, which is known to result in a tie with perfect gameplay from both players. Even when scaling up the grid size, such as with a 4x4 board, the game remains predictable. Seeking to overcome this predictability, this project introduces a variant with special rules, challenging players to think strategically and making each move more impactful.

## Key Features:

- Depth 2 Gameplay: Experience a heightened level of complexity with TicTacToe boards nested within each cell, requiring players to consider multiple layers of moves.
- Strategic Challenges: The enhanced ruleset introduces strategic considerations, making the game more dynamic and engaging.
- Python Implementation with PyGame: The entire game is implemented in Python, utilizing the PyGame library for an interactive and visually appealing experience.
  
## Rules:

- The game begins with Player X, who places their cross (X) in any cell of the inner TicTacToe grids.
- The inner grid to be played in next is determined by the cell where the previous player made their move.
- For example, if Player X places a cross in the middle-left cell of an inner TicTacToe grid, Player O must make their move in the inner TicTacToe located in the middle-left cell of the outer grid.
- The game proceeds with players taking turns, and the inner TicTacToe to be played in next is determined by the cell where the previous player placed their symbol.
- A player can freely choose where to place their symbol within the designated inner TicTacToe.
- A cell in the outer grid is marked with the respective player's symbol, and victory is achieved if the inner TicTacToe is won in the conventional way.
- The overall game is won when a player achieves victory in the outer TicTacToe grid. 

## Contributions:
Contributions and feedback are welcome!

## Future goals:
The project aims to develop an AI for the game, adding a challenging computer opponent to further enhance the gaming experience after the game is fully completed.

## !Note!: 
The game's concept is not original, and this project serves as a practical learning experience. Read more about the idea, for instance, at https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe.

Enjoy the game!


