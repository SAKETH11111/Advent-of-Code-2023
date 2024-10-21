# Day 21 Explanation

## Part 1

### Problem Description
The task is to find the number of ways to reach a specific point in a grid after a certain number of steps. The grid contains obstacles, and the starting point is marked with 'S'. The goal is to count the number of ways to reach the target point in a given number of steps.

### Approach
1. **Read Input File**: Read the input file, strip extra whitespaces, and split it into lines.
2. **Initialize Variables**: Initialize variables to store the grid, starting point, and distances.
3. **Breadth-First Search (BFS)**: Use BFS to explore the grid and calculate distances from the starting point to all other points.
4. **Count Ways**: Count the number of ways to reach the target point in the given number of steps.
5. **Print Result**: Print the number of ways to reach the target point.

### Code Explanation
- The code reads the input file and processes each line to create a grid.
- It identifies the starting point marked with 'S' and initializes variables for BFS.
- BFS is used to explore the grid and calculate distances from the starting point.
- The number of ways to reach the target point in the given number of steps is counted and printed.

## Part 2

### Problem Description
In addition to counting the number of ways to reach the target point, the task is to handle larger grids and more steps. The goal is to optimize the solution for larger inputs.

### Approach
1. **Optimize BFS**: Optimize the BFS algorithm to handle larger grids and more steps efficiently.
2. **Handle Larger Inputs**: Modify the code to handle larger grids and more steps without significant performance degradation.
3. **Count Ways**: Count the number of ways to reach the target point in the given number of steps for larger inputs.
4. **Print Result**: Print the number of ways to reach the target point for larger inputs.

### Code Explanation
- The code includes optimizations to handle larger grids and more steps efficiently.
- It uses BFS to explore the grid and calculate distances from the starting point.
- The number of ways to reach the target point in the given number of steps is counted and printed for larger inputs.

