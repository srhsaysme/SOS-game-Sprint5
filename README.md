# SOS-game-Sprint5
The final iteration of a game written in Python. Includes basic GUI, the option to record games in a text log, and full test suite for a multitide of use and misuse cases.

RULES:
Two players take turns attempting to create SOS patterns in a square grid. Red player always goes first and can place an S or O at any open position on the grid by entering the desired X and Y coordinates. The coordinates (1, 1) are at the top left of the grid. Then, blue player makes a similar move. This repeats until the game ends and a victor is decided. For a simple game, the game is over when one player completes an SOS pattern horizontally, vertically, or diagonally; the player that made the move is the victor. The game will also end if the game board is full and no one has made an SOS pattern, in which case the game is a draw. For a complex game, the players take turns until the grid is full, scoring a point for every SOS pattern they complete. When the game is over, whoever made more patterns wins.

When a new game is started, the user can determine the exact rules, including whether it will be a simple or complex game. One or both of the players can be controlled by the computer. Computer players will place letters in random unoccupied spaces. The size of the grid can also be given with the bottom most text field. The user can also tell the program to record the game, in which case the game will be logged move by move in a text file, gameRecord.txt.

DETAILS:
The main module of the program is in the file "Sprint5.py". The large commented section with methods from gameTesting class are unit tests that were used to prove the functionality of the program.

This was developed using an agile, sprint-based development style by me alone. To see the evolution of this project over time, see the repositories for the other sprints on my profile.
