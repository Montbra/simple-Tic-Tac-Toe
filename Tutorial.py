# Defining our main object of interation
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

#printing a column index, printing a row index, now #we have a coordinate to make a move, like c2

def game_board():
    print('   a  b  c')
    for count, row in enumerate(game, 1):
        print(count, row)

game[0][1] = 1

game_board()
