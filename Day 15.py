# Read input file
input_data = open("input.txt").read().strip()
cmds = input_data.split(',')

def hash_algorithm(s):
    current_value = 0
    for c in s:
        current_value = ((current_value + ord(c)) * 17) % 256
    return current_value

puzzle1_sum = 0
for cmd in cmds:
    puzzle1_sum += hash_algorithm(cmd)

print(puzzle1_sum)

BOX = [[] for _ in range(256)]
for cmd in cmds:
    if cmd[-1] == '-':
        name = cmd[:-1]
        h = hash_algorithm(name)
        BOX[h] = [(n, v) for (n, v) in BOX[h] if n != name]
    elif cmd[-2] == '=':
        name = cmd[:-2]
        h = hash_algorithm(name)
        len_ = int(cmd[-1])
        if name in [n for (n, v) in BOX[h]]:
            BOX[h] = [(n, len_ if name == n else v) for (n, v) in BOX[h]]
        else:
            BOX[h].append((name, len_))

puzzle2_sum = 0
for i, box in enumerate(BOX):
    for j, (n, v) in enumerate(box):
        puzzle2_sum += (i + 1) * (j + 1) * v

print(puzzle2_sum)
