# Day 22 Explanation

## Problem Description
The task is to simulate the movement of bricks in a 3D space. Each brick is represented by a set of coordinates, and the goal is to determine how many bricks will fall and how many will remain in place after a series of movements.

## Approach
1. **Read Input File**: Read the input file, strip extra whitespaces, and split it into lines.
2. **Initialize Variables**: Initialize variables to store the grid, brick sets, and seen coordinates.
3. **Parse Input**: Parse the input to extract the coordinates of each brick and store them in a list of sets.
4. **Simulate Movements**: Simulate the movement of bricks by iterating through the brick sets and checking if they can move down. If a brick can move down, update its coordinates and the seen set.
5. **Count Bricks**: Count the number of bricks that remain in place and the number of bricks that fall.
6. **Print Results**: Print the results for the number of bricks that remain in place and the number of bricks that fall.

## Code Explanation
- The code reads the input file and processes each line to extract the coordinates of the bricks.
- It initializes variables to store the grid, brick sets, and seen coordinates.
- The input is parsed to extract the coordinates of each brick and store them in a list of sets.
- The movement of bricks is simulated by iterating through the brick sets and checking if they can move down. If a brick can move down, its coordinates are updated, and the seen set is updated.
- The number of bricks that remain in place and the number of bricks that fall are counted and printed.
