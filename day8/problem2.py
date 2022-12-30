import sys

def calculate_score(grid, a, b):
    dists = []

    count = 0
    for i in range(a+1, len(grid)):
        count += 1
        if grid[i][b] >= grid[a][b]:
            break
    dists.append(count)

    count = 0
    for i in range(a-1, -1, -1):
        count += 1
        if grid[i][b] >= grid[a][b]:
            break
    dists.append(count)

    count = 0
    for i in range(b+1, len(grid[0])):
        count += 1
        if grid[a][i] >= grid[a][b]:
            break
    dists.append(count)

    count = 0
    for i in range(b-1, -1, -1):
        count += 1
        if grid[a][i] >= grid[a][b]:
            break
    dists.append(count)

    return dists[0]*dists[1]*dists[2]*dists[3]

def main():
    grid = []
    for line in sys.stdin:
        grid.append(line.strip())

    best_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            best_score = max(best_score, calculate_score(grid, i, j))

    print(best_score)

if __name__ == '__main__':
    main()