
import random


# generate the solution grid.
# place the bombs.
# check if there is a bomb there, if there is go back to the first step.
# place the bomb in the solution grid.
#Places a bomb in a random location.
# Update the numbers around them in the solution grid.
# y = row_index
# x = col_index

import random
def minesweeper(n):
    Board = [[0 for row in range(n)] for column in range(n)]
    for num in range(4):
        x = random.randint(0,4)
        y = random.randint(0,4)
        Board[y][x] = '#'
            # top centre, 1
        if (x >= 0 and x <= 4) and (y >= 1 and y <= 4):
            if Board[y - 1][x] != '#':
                Board[y - 1][x] += 1

            # top right, 2
        if (x >= 0 and x <= 3) and (y >= 1 and y <= 4):
            if Board[y - 1][x + 1] != '#':
                Board[y - 1][x + 1] += 1

            # centre right, 3
        if (x >= 0 and x <= 3) and (y >= 0 and y <= 4):
            if Board[y][x + 1] != '#':
                 Board[y][x + 1] += 1

            # bottom right, 4
        if (x >= 0 and x <= 3) and (y >= 0 and y <= 3):
            if Board[y + 1][x + 1] != '#':
                Board[y + 1][x + 1] += 1

            # bottom centre, 5
        if (x >= 0 and x <= 4) and (y >= 0 and y <= 3):
             if Board[y + 1][x] != '#':
                Board[y + 1][x] += 1

            # bottom left, 6
        if (x >= 1 and x <= 4) and (y >= 0 and y <= 3):
            if Board[y + 1][x - 1] != '#':
                Board[y + 1][x - 1] += 1

            # centre left, 7
        if (x >= 1 and x <= 4) and (y >= 0 and y <= 4):
            if Board[y ][x - 1] != '#':
                Board[y][x - 1] += 1

            # top left, 8
        if (x >= 1 and x <= 4) and (y >= 1 and y <= 4):
            if Board[y - 1][x - 1] != '#':
                Board[y - 1][x - 1] += 1

    # print in grid format
    # convert int to string, using list and map function
    for row in Board:
        print(list(map(str, row)))

minesweeper(5)

