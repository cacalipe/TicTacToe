
def check_winner(turn, board, game):
    winning_positions = game.winning_positions
    for combination in winning_positions:
        counter = 0
        for position in combination:
            if board[position[0]][position[1]] == turn[1]:
                counter += 1
        if counter >= 3:
            return f'{turn[0]} WON!'