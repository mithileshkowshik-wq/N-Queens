
def solveNQueens(n):
    output = []
    for l in range(0, n):
        #initializing grid
        grid = [[0 for _ in range(n)] for _ in range(n)]
        grid[0][l] = 'Q'
        Qcount = 1 # keeps a count of the number of queens on board
        eliminate(0, l, n, grid)
        #perfect until here

        for row in range(0, n):
            for col in range(0, n):
                if grid[row][col] == 0:
                    grid[row][col] = 'Q'
                    Qcount = Qcount + 1
                    eliminate(row, col, n, grid)
                    
        if Qcount == n:
            output.append(grid)
    for o in range(0, n):
            #initializing grid
            grid = [[0 for _ in range(n)] for _ in range(n)]
            grid[o][0] = 'Q'
            Qcount = 1 # keeps a count of the number of queens on board
            eliminate(o, 0, n, grid)
            #perfect until here
    
            for row in range(0, n):
                for col in range(0, n):
                    if grid[row][col] == 0:
                        grid[row][col] = 'Q'
                        Qcount = Qcount + 1
                        eliminate(row, col, n, grid)
                        print(grid)
                        
            if Qcount == n:
                output.append(grid)
            
        
    


def eliminate(i, j, n, grid):
    for k in range(0, n):
        if grid[i][k] != 'Q':
            grid[i][k] = '.'
    for m in range(0, n):
        if grid[m][j] != 'Q':
            grid[m][j] = '.'
    #eliminate diagonals
    for row in range(0, n):
        for col in range(0, n):
            if (row + col == i + j) and (grid[row][col] != 'Q'):
                grid[row][col] = '.'
    for row in range(0, n):
        for col in range(0, n):
            if (row - col == i - j) and (grid[row][col] != 'Q'):
                grid[row][col] = '.'

oof = solveNQueens(4)