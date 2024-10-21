# Day 12 Explanation

## Part 1

### Problem Description
The task is to process an input file containing a grid of characters. The goal is to find the number of valid paths from the start position to the end position, following specific rules.

### Approach
1. **Read Input File**: Read the input file, strip extra whitespaces, and split it into lines.
2. **Convert to Grid**: Convert the lines into a 2D grid of characters.
3. **Initialize Variables**: Initialize variables to store the current position, block position, and the length of the current block.
4. **Recursive Function**: Implement a recursive function to explore all possible paths from the current position.
   - **Base Case**: If the current position is the end position, return 1.
   - **Recursive Case**: For each possible move ('.' or '#'), recursively call the function with the updated position and block length.
5. **Memoization**: Use memoization to store the results of previously computed states to avoid redundant calculations.
6. **Count Valid Paths**: Count the number of valid paths from the start position to the end position.
7. **Print Result**: Print the total number of valid paths.

### Code Explanation
- The code reads the input file and converts it into a 2D grid of characters.
- It initializes variables to store the current position, block position, and the length of the current block.
- A recursive function is implemented to explore all possible paths from the current position.
- Memoization is used to store the results of previously computed states.
- The total number of valid paths is counted and printed.

## Part 2

### Problem Description
In addition to the original task, the input file may contain multiple grids. The goal is to handle these multiple grids and count the number of valid paths for each grid.

### Approach
1. **Handle Multiple Grids**: For each grid in the input file, repeat the process described in Part 1.
2. **Concatenate Grids**: Concatenate the grids to form a larger grid.
3. **Count Valid Paths**: Count the number of valid paths for the concatenated grid.
4. **Print Result**: Print the total number of valid paths for the concatenated grid.

### Code Explanation
- The code includes additional logic to handle multiple grids in the input file.
- It concatenates the grids to form a larger grid.
- The total number of valid paths for the concatenated grid is counted and printed.

