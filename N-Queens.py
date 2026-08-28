n = int(input("Enter n: "))
grid = [[False for _ in range(n)] for _ in range(n)]
cols = set()
diag1 = set()
diag2 = set()

def fill_row(r, n):
    if r == n:
        print_solution()
        return
        
    
    for c in range(0, n):
        
        if is_valid(r, c):

            grid[r][c] = True
            cols.add(c)
            diag1.add(r + c)
            diag2.add(r - c)

            fill_row(r + 1, n)

            grid[r][c] = False
            cols.remove(c)
            diag1.remove(r + c)
            diag2.remove(r - c)


def is_valid(r, c):
    if (c not in cols) and (r + c not in diag1) and (r - c not in diag2):
        return True
    else:
        return False
    

def print_solution():
    for row in grid:
        for cell in row:
            if cell == True:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

fill_row(0, n)

        

