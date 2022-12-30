import sys

def scan(grid, visibility, first, second, reverse):
    for i in range(len(first)):
        tallest = -1
        inner = range(len(second)-1,-1,-1) if reverse else range(len(second))

        for j in inner:
            tree_height = int(grid[i][j]) if first == grid else int(grid[j][i])
            if tree_height > tallest:
                if first == grid:
                    visibility[i][j] = 1
                else:
                    visibility[j][i] = 1
            tallest = max(tallest, tree_height)

def main():
    grid = []
    for line in sys.stdin:
        grid.append(line.strip())

    visibility = [[0]*len(grid[0]) for i in range(len(grid))]

    scan(grid, visibility, grid, grid[0], False)
    scan(grid, visibility, grid, grid[0], True)
    scan(grid, visibility, grid[0], grid, False)
    scan(grid, visibility, grid[0], grid, True)

    print(sum(sum(row) for row in visibility))

if __name__ == '__main__':
    main()