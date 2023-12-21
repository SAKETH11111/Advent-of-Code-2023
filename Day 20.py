from collections import defaultdict, deque
import math 
import sys
 
# Read input
data = open("input.txt").read().strip()
lines = data.split('\n') 

# Convert input to a 2D grid
grid = [[c for c in row] for row in lines]
rows = len(grid) 
columns = len(grid[0])
 
# Function to calculate the least common multiple of a list of numbers 
def lcm(xs):  
    ans = 1
    for x in xs:
        ans = (ans * x) // math.gcd(x, ans)
    return ans

# Dictionary to store types
types = {}

# Rules dictionary
rules = {}

# Parse input to extract rules and types
for line in lines:
    src, dest = line.split('->')
    src = src.strip()
    dest = dest.strip().split(', ')
    rules[src] = dest
    types[src[1:]] = src[0]

# Function to adjust the type of a signal
def adjust(y):
    return types[y] + y if y in types else y

# Create dictionaries to store dependencies and inverse dependencies
from_dict = {}
inv_dict = defaultdict(list)

# Process rules and dependencies
for x, ys in rules.items():
    rules[x] = [adjust(y) for y in ys]
    for y in rules[x]:
        if y[0] == '&':
            if y not in from_dict:
                from_dict[y] = {}
            from_dict[y][x] = 'lo'
        inv_dict[y].append(x)

# Assertions for certain conditions
assert len(inv_dict['rx']) == 1
assert inv_dict['rx'][0][0] == '&'
watch = inv_dict[inv_dict['rx'][0]]

# Initialize counters and queues
lo_count = 0
hi_count = 0
queue = deque()
on_set = set()
prev_dict = {}
count_dict = defaultdict(int)
to_lcm_list = []

# Iterate through timestamps
for t in range(1, 10**8):
    queue.append(('broadcaster', 'button', 'lo'))

    while queue:
        x, from_, typ = queue.popleft()

        # Handle 'lo' type
        if typ == 'lo':
            lo_count += 1
            if x in prev_dict and count_dict[x] == 2 and x in watch:
                to_lcm_list.append(t - prev_dict[x])
            prev_dict[x] = t
            count_dict[x] += 1

        # Check if all signals in watch have been processed
        if len(to_lcm_list) == len(watch):
            print(lcm(to_lcm_list))
            sys.exit(0)

        # Handle 'hi' type
        if typ == 'hi':
            hi_count += 1

        # Process rules for the current signal
        if x not in rules:
            continue
        if x == 'broadcaster':
            for y in rules[x]:
                queue.append((y, x, typ))
        elif x[0] == '%':
            if typ == 'hi':
                continue
            else:
                if x not in on_set:
                    on_set.add(x)
                    new_typ = 'hi'
                else:
                    on_set.discard(x)
                    new_typ = 'lo'
                for y in rules[x]:
                    queue.append((y, x, new_typ))
        elif x[0] == '&':
            from_dict[x][from_] = typ
            new_typ = 'lo' if all(y == 'hi' for y in from_dict[x].values()) else 'hi'
            for y in rules[x]:
                queue.append((y, x, new_typ))
        else:
            assert False, x

    # Print result at timestamp 1000
    if t == 1000:
        print(lo_count * hi_count)
