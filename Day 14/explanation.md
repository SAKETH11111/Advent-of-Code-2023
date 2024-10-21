# Day 14 Explanation

## Part 1

### Problem Description
The task is to simulate the movement of objects in a grid. The grid contains objects represented by 'O' and empty spaces represented by '.'. The objects can move downwards if there is an empty space below them. The goal is to calculate the score based on the final positions of the objects.

### Approach
1. **Read Input File**: Read the input file and split it into lines to create a grid.
2. **Rotate Grid**: Define a function to rotate the grid 90 degrees clockwise.
3. **Roll Objects**: Define a function to simulate the movement of objects downwards.
4. **Calculate Score**: Define a function to calculate the score based on the final positions of the objects.
5. **Display Grid**: Define a function to display the grid for debugging purposes.
6. **Simulate Movement**: Simulate the movement of objects for a specified number of cycles and calculate the score.

### Code Explanation
- The code reads the input file and creates a grid.
- It defines functions to rotate the grid, simulate the movement of objects, calculate the score, and display the grid.
- The main loop simulates the movement of objects for a specified number of cycles and calculates the score.

## Part 2

### Problem Description
In addition to simulating the movement of objects, the task is to handle a large number of cycles efficiently. The goal is to detect cycles in the grid configuration and use them to skip unnecessary calculations.

### Approach
1. **Detect Cycles**: Use a dictionary to store the grid configurations and detect cycles.
2. **Skip Cycles**: When a cycle is detected, skip the unnecessary calculations by jumping ahead in the simulation.
3. **Calculate Final Score**: Calculate the final score based on the final positions of the objects after skipping cycles.

### Code Explanation
- The code includes additional logic to detect cycles in the grid configuration.
- It uses a dictionary to store the grid configurations and detect cycles.
- When a cycle is detected, it skips the unnecessary calculations by jumping ahead in the simulation.
- The final score is calculated based on the final positions of the objects after skipping cycles.
