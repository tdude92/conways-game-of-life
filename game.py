def neighbors(x, y, grid, gridLength, gridWidth):
    out = 0
    if (x, y) == (0, 0):
        if grid[y][x + 1] == "0":
            out += 1
        if grid[y + 1][x] == "0":
            out += 1
        if grid[y + 1][x + 1] == "0":
            out += 1
    elif (x, y) == (gridLength - 1, 0):
        if grid[y][x - 1] == "0":
            out += 1
        if grid[y + 1][x] == "0":
            out += 1
        if grid[y + 1][x - 1] == "0":
            out += 1
    elif (x, y) == (0, gridWidth - 1):
        if grid[y][x + 1] == "0":
            out += 1
        if grid[y - 1][x] == "0":
            out += 1
        if grid[y - 1][x + 1] == "0":
            out += 1
    elif (x, y) == (gridLength - 1, gridWidth - 1):
        if grid[y][x - 1] == "0":
            out += 1
        if grid[y - 1][x] == "0":
            out += 1
        if grid[y - 1][x - 1] == "0":
            out += 1
    elif y == 0:
        if grid[y + 1][x - 1] == "0":
            out += 1
        if grid[y + 1][x] == "0":
            out += 1
        if grid[y + 1][x + 1] == "0":
            out += 1
        if grid[y][x - 1] == "0":
            out += 1
        if grid[y][x + 1] == "0":
            out += 1
    elif y == gridWidth - 1:
        if grid[y - 1][x - 1] == "0":
            out += 1
        if grid[y - 1][x] == "0":
            out += 1
        if grid[y - 1][x + 1] == "0":
            out += 1
        if grid[y][x - 1] == "0":
            out += 1
        if grid[y][x + 1] == "0":
            out += 1
    elif x == 0:
        if grid[y - 1][x + 1] == "0":
            out += 1
        if grid[y][x + 1] == "0":
            out += 1
        if grid[y + 1][x + 1] == "0":
            out += 1
        if grid[y - 1][x] == "0":
            out += 1
        if grid[y + 1][x] == "0":
            out += 1
    elif x == gridLength - 1:
        if grid[y - 1][x - 1] == "0":
            out += 1
        if grid[y][x - 1] == "0":
            out += 1
        if grid[y + 1][x - 1] == "0":
            out += 1
        if grid[y - 1][x] == "0":
            out += 1
        if grid[y + 1][x] == "0":
            out += 1
    else:
        if grid[y - 1][x - 1] == "0":
            out += 1
        if grid[y - 1][x] == "0":
            out += 1
        if grid[y - 1][x + 1] == "0":
            out += 1
        if grid[y + 1][x - 1] == "0":
            out += 1
        if grid[y + 1][x] == "0":
            out += 1
        if grid[y + 1][x + 1] == "0":
            out += 1
        if grid[y][x - 1] == "0":
            out += 1
        if grid[y][x + 1] == "0":
            out += 1
    return out

def isAlive(x, y, grid, gridLength, gridWidth):
    if grid[y][x] == "0":
        alreadyAlive = True
    else:
        alreadyAlive = False

    if neighbors(x, y, grid, gridLength, gridWidth) < 2:
        return "."
        # Any cell with < 2 neighbors dies.
    elif neighbors(x, y, grid, gridLength, gridWidth) in (2, 3) and alreadyAlive:
        return "0"
        # Any living cell with 2 or 3 neighbors lives.
    elif neighbors(x, y, grid, gridLength, gridWidth) > 3:
        return "."
        # Any cell with more than 3 neighbors dies.
    elif neighbors(x, y, grid, gridLength, gridWidth) == 3 and not alreadyAlive:
        return "0"
        # Any dead cell with 3 neighbors lives.
    else:
        return "."

if __name__ == "__main__":
    from copy import deepcopy
    from time import sleep

    gridLength = int(input("Grid Length: "))
    gridWidth = int(input("Grid Width: "))

    with open("seed.txt", "r") as seed:
        seedCells = seed.readlines()
        for i in range(len(seedCells)):
            seedCells[i] = list(map(int, seedCells[i][:len(seedCells[i]) - 1].split()))

    grid = [["0" if [x, y] in seedCells else "." for x in range(gridLength)] for y in range(gridWidth)]

    while True:
        for i in grid:
            print(*i) 
        print()

        gridCopy = deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                gridCopy[y][x] = isAlive(x, y, grid, gridLength, gridWidth) 
        
        grid = deepcopy(gridCopy)

        n = input("Press <Enter> to continue, input 'n' to stop.\n")
        
        if n == "n":
            break
