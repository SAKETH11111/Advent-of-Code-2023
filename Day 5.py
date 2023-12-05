# Read input file, strip extra whitespaces, and split into lines
D = open("input.txt").read().strip()
L = D.split('\n')

# Split input into parts separated by empty lines
parts = D.split('\n\n')
seed, *others = parts

# Extract integers from the seed part
seed = [int(x) for x in seed.split(':')[1].split()]

# Define a class for functions
class Function:
    def __init__(self, S):
        # Extract lines after the function name
        lines = S.split('\n')[1:]
        # Store tuples of integers representing (dst, src, sz)
        self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]

    # Apply the function to a single value
    def apply_one(self, x: int) -> int:
        for (dst, src, sz) in self.tuples:
            if src <= x < src + sz:
                return x + dst - src
        return x

    # Apply the function to a range of values
    def apply_range(self, R):
        A = []
        for (dest, src, sz) in self.tuples:
            src_end = src + sz
            NR = []
            while R:
                (st, ed) = R.pop()
                # Check if (src,sz) cuts (st,ed)
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A + R

# Create Function objects for each function in the 'others' list
Fs = [Function(s) for s in others]

# Function to process lines in 'others' (currently unused in the code)
def f(R, o):
    for line in o:
        dest, src, sz = [int(x) for x in line.split()]
        src + sz

# Part 1: Apply all functions in Fs to each seed value and store the results in P1
P1 = []
for x in seed:
    for f in Fs:
        x = f.apply_one(x)
    P1.append(x)
print("---Part 1---")
print("", min(P1), "\n")

# Part 2: Apply all functions in Fs to each seed range and store the results in P2
P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
    # Inclusive on the left, exclusive on the right
    R = [(st, st + sz)]
    for f in Fs:
        R = f.apply_range(R)
    P2.append(min(R)[0])
print("---Part 2---")
print("", min(P2))


#print("Thanks for the code")