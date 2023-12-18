# Importing the pairwise function from itertools
from itertools import pairwise

# Function to extrapolate the next value in a sequence based on the given differences
def seq(ints):
    # Check if all differences are zero, indicating the end of the sequence
    if all(ints == 0 for ints in ints):
        return 0
    # Calculate differences between consecutive elements in the sequence
    diffs = [b - a for a, b in pairwise(ints)]
    # Recursively call seq to extrapolate the next value
    return ints[-1] + seq(diffs)

# Function to calculate the sum of extrapolated values for each line in the input file
def p1(f):
    # Sum the extrapolated values for each line in the input file
    return sum(seq([int(x) for x in line.split()]) for line in f)

# Function to calculate the sum of extrapolated values in reverse order for each line in the input file
def p2(f):
    # Sum the extrapolated values in reverse order for each line in the input file
    return sum(seq([int(x) for x in line.split()[::-1]]) for line in f)

# Read the content of the input file
file = open("input.txt").read()

# Print the result of p1 and p2 for the input file
print(p1(file.split("\n")))
print(p2(file.split("\n")))
