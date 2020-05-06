from tictactoe import player, actions, result
from custom_errors import InvalidActionError
from copy import deepcopy

EMPTY = None
O = "O"
X = "X"

board = [[EMPTY, EMPTY, EMPTY],
          [X, EMPTY, O],
          [EMPTY, EMPTY, EMPTY]]

action = (1,0)

print(result(board, action))


