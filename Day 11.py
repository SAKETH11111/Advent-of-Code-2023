D = open("input.txt").read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]

# Get the number of rows (R) and columns (C) in the grid.
R = len(G)
C = len(G[0])

# Ensure that each row has the same number of columns.
for r in range(R):
    assert len(G[r]) == C

# Identify and store indices of empty rows (EMPTY_R).
EMPTY_R = []
r = 0
while r < R:
    empty = True
    for c in range(C):
        if G[r][c] == '#':
            empty = False
    if empty:
        EMPTY_R.append(r)
    r += 1

# Identify and store indices of empty columns (EMPTY_C).
EMPTY_C = []
c = 0
while c < C:
    empty = True
    for r in range(R):
        if G[r][c] == '#':
            empty = False
    if empty:
        EMPTY_C.append(c)
    c += 1

# Identify the locations of galaxies and assign them unique numbers (GAL).
GAL = []
for r in range(R):
    for c in range(C):
        if G[r][c] == '#':
            GAL.append((r, c))

# Iterate for both Part 1 and Part 2.
for part2 in [False, True]:
    # Define the expansion factor based on the part.
    expansion_factor = 10**6 - 1 if part2 else 2 - 1
    ans = 0

    # Iterate through pairs of galaxies and calculate shortest path lengths.
    for i, (r, c) in enumerate(GAL):
        for j in range(i, len(GAL)):
            r2, c2 = GAL[j]
            dij = abs(r2 - r) + abs(c2 - c)

            # Adjust path length for expanded rows (EMPTY_R).
            for er in EMPTY_R:
                if min(r, r2) <= er <= max(r, r2):
                    dij += expansion_factor

            # Adjust path length for expanded columns (EMPTY_C).
            for ec in EMPTY_C:
                if min(c, c2) <= ec <= max(c, c2):
                    dij += expansion_factor

            ans += dij

    if part2 is True:
      print("part 2:", ans)
    else:
      print("Part 1:", ans)
