# Read the contents of the "input.txt" file, split lines, and store each line as a string in the 'lines' list.
lines = open("input.txt").read().splitlines()

# Determine the width and height of the grid based on the first line of the input.
width, height = len(lines[0]), len(lines)

# Create a dictionary 'tiles' to represent the grid, where each coordinate (x, y) maps to a character in the input.
tiles = {(x, y): lines[y][x] for y in range(height) for x in range(width)}

# Define deltas for moving in the Up, Right, Down, Left directions.
DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# Define possible turns corresponding to Up, Right, Down, Left directions.
TURNS = ["7|F", "J-7", "L|J", "F-L"]

# Function to add two coordinate tuples element-wise.
def add(a, b):
    return a[0] + b[0], a[1] + b[1]

# Function to check if a given coordinate is within the boundaries of the grid.
def on_board(p):
    return 0 <= p[0] < width and 0 <= p[1] < height

# Find the starting position of the path marked by "S" on the grid.
start_p = next(p for p, ch in tiles.items() if ch == "S")

# Find the initial direction of the path based on the character next to the starting position.
for i in range(4):
    np = add(start_p, DELTA[i])
    if on_board(np) and tiles[np] in TURNS[i]:
        start_d = i
        break
else:
    print("pipe not found")

# Find the path on the grid and count its length.
on_path = set()
p = start_p
d = start_d
while True:
    on_path.add(p)
    p = add(p, DELTA[d])
    if p == start_p:
        break
    d = (d + TURNS[d].index(tiles[p]) - 1) % 4
end_d = d
print("Part 1:", len(on_path)//2)

# Replace the "S" character with the appropriate turn character based on the path direction.
tiles[start_p] = TURNS[end_d][(start_d - end_d + 1) % 4]

# Find and count tiles inside the path.
count = 0
started_with_F = None
for y in range(height):
    # Flip on every vertical transition.
    inside = False
    for x in range(width):
        p = x, y
        if p in on_path:
            ch = tiles[p]
            if ch == "F":
                started_with_F = True
            elif ch == "L":
                started_with_F = False
            elif ch == "|" or (ch == "J" if started_with_F else ch == "7"):
                inside = not inside
        elif inside:
            count += 1
    if inside:
        print("Ended inside", y)
print("Part 2:", count)
