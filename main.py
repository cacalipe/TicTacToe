from game_logic.configs import TicTacToeConfig

game:TicTacToeConfig = TicTacToeConfig()

board = game.board
counter = 0
turn = None

print('-='*20,'\nBOARD')
for row in range(0, 3):
    for col in range(0, 3):
        print(board[row][col], end=' ')
    print()
print('-='*20,'\nPlayer wins by completing a streak...\nInvite your friend to play with you!\nHow to play? Choose row and column to mark position\n','-='*20)

while True:
    counter += 1
    if not counter % 2 == 0:
        turn = game.player_a
    elif counter % 2 == 0:
        turn = game.player_b
    row = int(input(f'{turn[0]} turn, choose the row: ')) - 1
    col = int(input(f'{turn[0]} turn, choose the col: ')) - 1
    while row >= 3 or col >= 3 or board[row][col] == game.player_a[1] or board[row][col] == game.player_b[1]:
        print('-='*20,'\nInvalid chosen position, please choose another\n','-='*20)
        row = int(input(f'{turn[0]} turn, choose the row: ')) - 1
        col = int(input(f'{turn[0]} turn, choose the col: ')) - 1
    board[row][col] = turn[1]

    print('\nBOARD')
    for row in range(0, 3):
        for col in range(0, 3):
            print(board[row][col], end=' ')
        print()
    print('-='*20)
