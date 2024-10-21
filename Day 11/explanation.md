# Day 11 Explanation

## Part 1

### Problem Description
The task is to calculate the shortest path lengths between pairs of galaxies in a grid. The grid contains empty rows and columns, which can be expanded to increase the path length. The goal is to find the total path length for all pairs of galaxies.

### Approach
1. **Read Input File**: Read the input file, strip extra whitespaces, and split it into lines.
2. **Convert to Grid**: Convert the lines into a 2D grid of characters.
3. **Identify Empty Rows and Columns**: Identify and store the indices of empty rows and columns.
4. **Identify Galaxies**: Identify the locations of galaxies and assign them unique numbers.
5. **Calculate Shortest Path Lengths**: Iterate through pairs of galaxies and calculate the shortest path lengths, adjusting for expanded rows and columns.
6. **Print Results**: Print the total path length for all pairs of galaxies.

### Code Explanation
- The code reads the input file and converts it into a 2D grid of characters.
- It identifies empty rows and columns and stores their indices.
- It identifies the locations of galaxies and assigns them unique numbers.
- It iterates through pairs of galaxies and calculates the shortest path lengths, adjusting for expanded rows and columns.
- The total path length for all pairs of galaxies is calculated and printed.

## Part 2

### Problem Description
In addition to calculating the shortest path lengths, the task is to handle a larger expansion factor for the empty rows and columns. The goal is to find the total path length for all pairs of galaxies with the larger expansion factor.

### Approach
1. **Define Expansion Factor**: Define the expansion factor based on the part (10^6 - 1 for part 2).
2. **Calculate Shortest Path Lengths**: Iterate through pairs of galaxies and calculate the shortest path lengths, adjusting for the larger expansion factor.
3. **Print Results**: Print the total path length for all pairs of galaxies with the larger expansion factor.

### Code Explanation
- The code includes additional logic to handle the larger expansion factor for part 2.
- It iterates through pairs of galaxies and calculates the shortest path lengths, adjusting for the larger expansion factor.
- The total path length for all pairs of galaxies with the larger expansion factor is calculated and printed.

