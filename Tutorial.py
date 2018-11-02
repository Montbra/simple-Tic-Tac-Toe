# Defining our main object of interation
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

#printing a column index, printing a row index, now #we have a coordinate to make a move, like c2

def game_board(player=0, row=1, column=1, just_display=False):
    print('   1  2  3')
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game, 1):
        print(count, row)

game_board(just_display=True)
game_board(player=1, row=2, column=1)

# game[0][1] = 1

# game_board()
