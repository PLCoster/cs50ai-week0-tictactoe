from tictactoe import player, actions, result, winner
from custom_errors import InvalidActionError
from copy import deepcopy

EMPTY = None
O = "O"
X = "X"

board = [[X, O, X],
          [X, X, None],
          [X, EMPTY, O]]

action = (1,0)

print('Winner is: ', winner(board))


