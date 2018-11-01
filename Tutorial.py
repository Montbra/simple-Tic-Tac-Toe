# Defining our main object of interation
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

#printing a column index
print('   a  b  c')

#printing a row index
for count_Row, row in enumerate(game, 1):
    print(count_Row, row)

#now we have a coordinate to make a move, like c2