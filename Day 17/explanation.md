# Day 17 Explanation

## Part 1

### Problem Description
The task is to navigate a grid from the top-left corner to the bottom-right corner, minimizing the cost. The grid contains numeric values representing the cost of each cell. The movement is restricted to up, down, left, and right directions.

### Approach
1. **Read Input File**: Read the input file and split it into lines.
2. **Convert to Grid**: Convert the lines into a 2D grid of numeric values.
3. **Initialize Priority Queue**: Use a priority queue to store the current position, direction, and cost.
4. **Dijkstra's Algorithm**: Implement Dijkstra's algorithm to find the shortest path from the top-left to the bottom-right corner.
   - **Pop from Queue**: Pop the current position, direction, and cost from the priority queue.
   - **Check Validity**: Check if the current position is valid and not visited.
   - **Update Cost**: Update the cost for the current position and push the new position, direction, and cost to the priority queue.
5. **Find Minimum Cost**: Find the minimum cost to reach the bottom-right corner.

### Code Explanation
- The code reads the input file and converts it into a 2D grid of numeric values.
- It initializes a priority queue and implements Dijkstra's algorithm to find the shortest path.
- The minimum cost to reach the bottom-right corner is calculated and returned.

## Part 2

### Problem Description
In addition to the constraints in Part 1, the movement is restricted to a maximum of 10 consecutive steps in the same direction.

### Approach
1. **Check Validity**: For each move, check if the number of consecutive steps in the same direction is within the allowed limit.
2. **Update Cost**: Update the cost for the current position and push the new position, direction, and cost to the priority queue if the move is valid.

### Code Explanation
- The code includes additional logic to check the number of consecutive steps in the same direction.
- It updates the cost for the current position and pushes the new position, direction, and cost to the priority queue if the move is valid.
- The minimum cost to reach the bottom-right corner is calculated and returned.

