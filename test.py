from tictactoe import player

EMPTY = "EMPTY"
O = "O"
X = "X"

board = [[X, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, X, EMPTY]]

print(player(board))