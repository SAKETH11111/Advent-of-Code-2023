from collections import defaultdict

# Read input file, strip extra whitespaces, and split into lines
input_data = open('0').read().strip()
lines = input_data.split('\n')

# Convert lines to a 2D grid G
grid = [[c for c in line] for line in lines]

# Get the number of rows and columns in the grid
num_rows = len(grid)
num_cols = len(grid[0])

# Initialize variables
total_part_value = 0
gear_numbers = defaultdict(list)

# Process each cell in the grid
for r in range(num_rows):
    gears = set()  # Positions of '*' characters next to the current number
    current_number = 0
    has_part = False

    for c in range(num_cols + 1):
        if c < num_cols and grid[r][c].isdigit():
            current_number = current_number * 10 + int(grid[r][c])

            for rr in [-1, 0, 1]:
                for cc in [-1, 0, 1]:
                    if 0 <= r + rr < num_rows and 0 <= c + cc < num_cols:
                        ch = grid[r + rr][c + cc]
                        if not ch.isdigit() and ch != '.':
                            has_part = True
                        if ch == '*':
                            gears.add((r + rr, c + cc))
        elif current_number > 0:
            for gear in gears:
                gear_numbers[gear].append(current_number)
            if has_part:
                total_part_value += current_number
            current_number = 0
            has_part = False
            gears = set()

# Print the result for part 1
print("---Part 1---")
print(total_part_value)

# Calculate and print the result for part 2
total_product = 0
for key, values in gear_numbers.items():
    if len(values) == 2:
        total_product += values[0] * values[1]

print("---Part 2---")
print(total_product)
