# Picture a grid with points at the center of each square.
# We start at (0,0), and each square is like a dot in the grid.
# The shape is formed by following instructions, like connecting the dots.

# Pick's theorem tells us the area (A) of the shape equals the points inside (I) plus half the points on the boundary (B), minus one.

# The solution is just the sum of points inside and on the boundary.
# Rearranging Pick's theorem, it's the area plus half the boundary points, plus one.
# The boundary points are like the perimeter, the sum of N in all commands.
# Note: each command covers N+1 squares, but the last square of each command is also covered by the
# starting square of the next command. Adding up N gives the right count of squares in the path.
# We calculate the area A in two ways:
# - Using the shoelace formula: a kind of zigzag math to find the area.
# - Using Green's theorem: another way to find the area by looking at how things change in the x and y directions.

from typing import List
from dataclasses import dataclass

@dataclass
class Instruction:
    direction: str
    distance: int

def parse_input(input_str: str, part2: bool) -> List[Instruction]:
    instructions = []
    for line in input_str.split('\n'):
        dir_, dist, hex_code = line.split()
        if not part2:
            instructions.append(Instruction(dir_, int(dist)))
        else:
            hex_code = hex_code[1:-1]
            dir_ = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(hex_code[-1])]
            dist = int(hex_code[1:-1], 16)
            instructions.append(Instruction(dir_, dist))
    return instructions

def shoelace_area(commands: List[Instruction]) -> int:
    # Compute the area A using the shoelace formula.
    vertices = []
    position = (0, 0)
    for command in commands:
        dir_, dist = command.direction, command.distance
        if dir_ == 'R':
            position = (position[0] + dist, position[1])
        elif dir_ == 'D':
            position = (position[0], position[1] - dist)
        elif dir_ == 'L':
            position = (position[0] - dist, position[1])
        elif dir_ == 'U':
            position = (position[0], position[1] + dist)
        vertices.append(position)

    # Apply the shoelace formula to compute the area.
    area = 0
    for i in range(len(vertices)):
        area -= vertices[i][0] * vertices[(i + 1) % len(vertices)][1]
        area += vertices[i][1] * vertices[(i + 1) % len(vertices)][0]
    area //= 2
    return area

def green_area(commands: List[Instruction]) -> int:
    # Compute the area A using Green's theorem.
    area = 0
    y = 0
    for command in commands:
        if command.direction == 'R':
            area += y * command.distance
        elif command.direction == 'L':
            area -= y * command.distance
        elif command.direction == 'U':
            y += command.distance
        elif command.direction == 'D':
            y -= command.distance
    return area

input_data = open("input.txt").read().strip()

# Process both parts of the puzzle.
for part2 in [False, True]:
    instructions = parse_input(input_data, part2)

    # Calculate the perimeter.
    perimeter = sum(command.distance for command in instructions)

    # Calculate the area using two different methods.
    area1 = shoelace_area(instructions)
    area2 = green_area(instructions)

    # Ensure both area calculations match.
    assert area1 == area2, f'shoelace={area1} green={area2}'

    # Calculate the final result.
    result = area1 + (perimeter // 2) + 1
    print(result)

