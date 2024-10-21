# Day 10 Explanation

## Part 1

### Problem Description
The task is to find the length of the path marked by "S" on the grid and count the number of tiles inside the path.

### Approach
1. **Read Input File**: Read the input file, split lines, and store each line as a string in the 'lines' list.
2. **Determine Grid Dimensions**: Determine the width and height of the grid based on the first line of the input.
3. **Create Grid Representation**: Create a dictionary 'tiles' to represent the grid, where each coordinate (x, y) maps to a character in the input.
4. **Define Movement Directions**: Define deltas for moving in the Up, Right, Down, Left directions.
5. **Find Starting Position**: Find the starting position of the path marked by "S" on the grid.
6. **Find Initial Direction**: Find the initial direction of the path based on the character next to the starting position.
7. **Find Path and Count Length**: Find the path on the grid and count its length.
8. **Replace Starting Character**: Replace the "S" character with the appropriate turn character based on the path direction.
9. **Count Tiles Inside Path**: Find and count tiles inside the path.

### Code Explanation
- The code reads the input file and processes each line to create a grid representation.
- It defines movement directions and finds the starting position and initial direction of the path.
- The path is found and its length is counted.
- The starting character is replaced with the appropriate turn character.
- The tiles inside the path are counted and the results are printed.

## Part 2

### Problem Description
In addition to finding the length of the path, the task is to count the number of tiles inside the path.

### Approach
1. **Count Tiles Inside Path**: Find and count tiles inside the path.
2. **Print Results**: Print the results for both parts.

### Code Explanation
- The code includes additional logic to count the tiles inside the path.
- The results are printed for both parts.

