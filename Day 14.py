# Read input file
input_data = open("input.txt").read().strip()
lines = input_data.split('\n')
grid = [[c for c in row] for row in lines]

def rotate(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [['?' for _ in range(rows)] for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            new_grid[c][rows-1-r] = grid[r][c]
    return new_grid

def roll(grid):
    rows = len(grid)
    cols = len(grid[0])
    for c in range(cols):
        for _ in range(rows):
            for r in range(rows):
                if grid[r][c] == 'O' and r > 0 and grid[r-1][c] == '.':
                    grid[r][c] = '.'
                    grid[r-1][c] = 'O'
    return grid

def calculate_score(grid):
    total_score = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'O':
                total_score += len(grid) - r
    return total_score

def display_grid(grid):
    for r in range(len(grid)):
        print(''.join(grid[r]))

grid_history = {}

target_cycles = 10**9
current_cycle = 0

while current_cycle < target_cycles:
    current_cycle += 1
    for j in range(4):
        grid = roll(grid)
        if current_cycle == 1 and j == 0:
            print(calculate_score(grid))  # part 1
        grid = rotate(grid)

    grid_hash = tuple(tuple(row) for row in grid)

    if grid_hash in grid_history:
        cycle_length = current_cycle - grid_history[grid_hash]
        amount = (target_cycles - current_cycle) // cycle_length
        current_cycle += amount * cycle_length

    grid_history[grid_hash] = current_cycle

print(calculate_score(grid))
