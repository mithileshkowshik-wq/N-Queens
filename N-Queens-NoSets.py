n = int(input("Enter n: "))
grid = [[False for _ in range(n)] for _ in range(n)]


def fill_row(r, n):
    if r == n:
        print_solution()
        return
        
    
    for c in range(0, n):

        grid[r][c] = True

        if is_valid(r, c, n):
            fill_row(r + 1, n)

        grid[r][c] = False


def is_valid(r, c, n):
    for i in range(n):
        if i == r:
            continue
        if grid[i][c]:
            return False

    for i in range(n):
        for j in range(n):
            if i == r and j == c:
                continue

            if r + c == i + j and grid[i][j]:
                return False

            if r - c == i - j and grid[i][j]:
                return False

    return True

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


        

