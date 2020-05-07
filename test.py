from tictactoe import player, actions, result, winner, terminal
from custom_errors import InvalidActionError
from copy import deepcopy

EMPTY = None
O = "O"
X = "X"

board = [[X, O, O],
          [X, X, O],
          [O, X, O]]

action = (1,0)

print('Winner is: ', winner(board))

print('Game over? ', terminal(board))
