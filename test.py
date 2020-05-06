from tictactoe import player, actions

EMPTY = "EMPTY"
O = "O"
X = "X"

board = [[X, X, X],
          [X, X, EMPTY],
          [X, X, EMPTY]]

print(player(board))

moves = set()

for i in range(3):
  print(i)
  for j in range(3):
    print(j)
    if board[i][j] == EMPTY:
      print('board position', i, j, 'is :', board[i][j])
      moves.add((i, j))

print(moves)