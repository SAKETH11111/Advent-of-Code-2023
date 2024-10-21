# Day 23 Explanation

## Part 1

### Problem Description
The task is to navigate a grid with obstacles and find the longest path from the start to the end. The grid contains various symbols representing different types of obstacles and paths.

### Approach
1. **Read Input File**: Read the input file, strip extra whitespaces, and split it into lines.
2. **Initialize Variables**: Initialize variables to store the grid, dimensions, and sets for visited cells and edges.
3. **Identify Valid Cells**: Iterate through the grid to identify valid cells that can be part of the path.
4. **Identify Start and End Points**: Identify the start and end points in the grid.
5. **Build Edges**: Build edges between valid cells based on the grid's structure and obstacles.
6. **Depth-First Search (DFS)**: Use DFS to find the longest path from the start to the end.
7. **Print Result**: Print the length of the longest path.

### Code Explanation
- The code reads the input file and processes the grid to identify valid cells and build edges.
- It uses DFS to find the longest path from the start to the end.
- The result is printed as the length of the longest path.

## Part 2

### Problem Description
In addition to finding the longest path, the task is to handle different types of obstacles and paths in the grid. The grid contains symbols representing different types of obstacles and paths, and the task is to navigate through them.

### Approach
1. **Handle Different Obstacles**: Extend the logic to handle different types of obstacles and paths in the grid.
2. **Build Edges with Conditions**: Build edges between valid cells based on the grid's structure and obstacles, considering additional conditions.
3. **Depth-First Search (DFS)**: Use DFS to find the longest path from the start to the end, considering the additional conditions.
4. **Print Result**: Print the length of the longest path, considering the additional conditions.

### Code Explanation
- The code includes additional logic to handle different types of obstacles and paths in the grid.
- It builds edges between valid cells based on the grid's structure and obstacles, considering additional conditions.
- The result is printed as the length of the longest path, considering the additional conditions.

