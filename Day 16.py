# Read input file
input_data = open("input.txt").read().strip()
lines = input_data.split('\n')
grid = [[c for c in row] for row in lines]

rows = len(grid)
cols = len(grid[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def step(r, c, d):
    return (r + directions[d][0], c + directions[d][1], d)

def score(sr, sc, sd):
    positions = [(sr, sc, sd)]
    seen = set()
    seen_twice = set()

    while True:
        new_positions = []

        if not positions:
            break

        for (r, c, d) in positions:
            if 0 <= r < rows and 0 <= c < cols:
                seen.add((r, c))

                if (r, c, d) in seen_twice:
                    continue

                seen_twice.add((r, c, d))

                ch = grid[r][c]

                if ch == '.':
                    new_positions.append(step(r, c, d))
                elif ch == '/':
                    new_positions.append(step(r, c, {0: 1, 1: 0, 2: 3, 3: 2}[d]))
                elif ch == '\\':
                    new_positions.append(step(r, c, {0: 3, 1: 2, 2: 1, 3: 0}[d]))
                elif ch == '|':
                    if d in [0, 2]:
                        new_positions.append(step(r, c, d))
                    else:
                        new_positions.append(step(r, c, 0))
                        new_positions.append(step(r, c, 2))
                elif ch == '-':
                    if d in [1, 3]:
                        new_positions.append(step(r, c, d))
                    else:
                        new_positions.append(step(r, c, 1))
                        new_positions.append(step(r, c, 3))
                else:
                    assert False

        positions = new_positions

    return len(seen)

print(score(0, 0, 1))

answer = 0
for r in range(rows):
    answer = max(answer, score(r, 0, 1))
    answer = max(answer, score(r, cols-1, 3))

for c in range(cols):
    answer = max(answer, score(0, c, 2))
    answer = max(answer, score(rows-1, c, 0))

print(answer)
