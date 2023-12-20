from collections import deque
 
# Read the input file
input_data = open("input.txt").read().strip()
lines = input_data.split('\n')

# Parse rules and parts
rules, parts = input_data.split('\n\n')

# Parse rules into a dictionary
rule_dict = {}
for rule in rules.split('\n'):
    name, rest = rule.split('{')
    rule_dict[name] = rest[:-1]

# Function to check if a part is accepted
def accepted(part):
    state = 'in'
    while True:
        rule = rule_dict[state]
        for cmd in rule.split(','):
            applies = True
            res = cmd
            if ':' in cmd:
                cond, res = cmd.split(':')
                var = cond[0]
                op = cond[1]
                n = int(cond[2:])
                if op == '>' and part[var] > n:
                    applies = True
                elif op == '<' and part[var] < n:
                    applies = True
                else:
                    applies = False

            if applies:
                if res == 'A':
                    return True
                if res == 'R':
                    return False
                state = res
                break

# Initialize the sum of values for accepted parts
ans = 0

# Iterate over parts and calculate the sum of values for accepted parts
for part in parts.split('\n'):
    part = part[1:-1]
    part = {x.split('=')[0]: int(x.split('=')[1]) for x in part.split(',')}
    if accepted(part):
        ans += part['x'] + part['m'] + part['a'] + part['s']

print("Part 1:", ans)


# Part 2

# Function to calculate the new range for a variable based on a comparison operation
def new_range(op, n, lo, hi):
    if op == '>':
        lo = max(lo, n + 1)
    elif op == '<':
        hi = min(hi, n - 1)
    elif op == '>=':
        lo = max(lo, n)
    elif op == '<=':
        hi = min(hi, n)
    return (lo, hi)

# Function to calculate new ranges for all variables
def new_ranges(var, op, n, xl, xh, ml, mh, al, ah, sl, sh):
    if var == 'x':
        xl, xh = new_range(op, n, xl, xh)
    elif var == 'm':
        ml, mh = new_range(op, n, ml, mh)
    elif var == 'a':
        al, ah = new_range(op, n, al, ah)
    elif var == 's':
        sl, sh = new_range(op, n, sl, sh)
    return (xl, xh, ml, mh, al, ah, sl, sh)

# Initialize the sum for accepted parts in Part 2
ans = 0

# Use deque for breadth-first search
Q = deque([('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000)])

# Breadth-first search to calculate the sum of accepted parts in Part 2
while Q:
    state, xl, xh, ml, mh, al, ah, sl, sh = Q.pop()

    if xl > xh or ml > mh or al > ah or sl > sh:
        continue

    if state == 'A':
        score = (xh - xl + 1) * (mh - ml + 1) * (ah - al + 1) * (sh - sl + 1)
        ans += score
        continue
    elif state == 'R':
        continue
    else:
        rule = rule_dict[state]
        for cmd in rule.split(','):
            applies = True
            res = cmd
            if ':' in cmd:
                cond, res = cmd.split(':')
                var = cond[0]
                op = cond[1]
                n = int(cond[2:])
                Q.append((res, *new_ranges(var, op, n, xl, xh, ml, mh, al, ah, sl, sh)))
                xl, xh, ml, mh, al, ah, sl, sh = new_ranges(var, '<=' if op == '>' else '>=', n, xl, xh, ml, mh, al, ah, sl, sh)
            else:
                Q.append((res, xl, xh, ml, mh, al, ah, sl, sh))
                break

print("Part 2:", ans)
