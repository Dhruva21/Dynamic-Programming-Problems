grid_size = 8

# check if (row1, col1) is a valid spot for a queen by checking if there is a queen in the same column or diagonal. We don't need to check it for queens in the same row.
def checkValid(colums, row1, col1):
    for row2 in range(row1):
        col2 = colums[row2]
        # check if row2,col2 invalidated row2,col1 as a queen spot

        # check if rows have a queen in same column
        if col1 == col2:
            return False

        # check diagonals: if the distance between the columns equals the distance between the rows, then they're in the same diaginal.
        colDist = abs(col1 - col2)
        rowDist = row1 - row2
        if colDist == rowDist:
            return False
    return True

def placeQueens(row, columns, results):
    if row == grid_size:
        results.append(columns.copy())
    else:
        for col in range(grid_size):
            if checkValid(columns, row, col):
                columns[row] = col # place queen
                placeQueens(row + 1, columns, results) # and recurese