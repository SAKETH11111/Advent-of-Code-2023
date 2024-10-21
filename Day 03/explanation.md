# Day 03 Explanation

## Part 1

### Problem Description
The task is to find the sum of numbers connected to symbols in an engine schematic. The schematic is represented as a grid of characters, where numbers represent part numbers and symbols (except '.') represent gears. The goal is to sum all part numbers adjacent to symbols.

### Approach
1. **Read Input File**: Read the input file, strip extra whitespaces, and split it into lines.
2. **Convert to Grid**: Convert the lines into a 2D grid of characters.
3. **Initialize Variables**: Initialize variables to store the total sum of part numbers and a dictionary to store gear numbers.
4. **Process Each Cell**: Iterate through each cell in the grid.
   - **Identify Symbols**: Check if the current cell contains a symbol.
   - **Check Adjacent Cells**: For each symbol, check the adjacent cells (horizontally, vertically, and diagonally) for part numbers.
   - **Update Sum**: If a part number is found, add it to the total sum.
5. **Print Result**: Print the total sum of part numbers.

### Code Explanation
- The code reads the input file and converts it into a 2D grid of characters.
- It iterates through each cell in the grid, identifying symbols and checking adjacent cells for part numbers.
- The total sum of part numbers is calculated and printed.

## Part 2

### Problem Description
In addition to summing part numbers, the task is to identify gears represented by '*' symbols adjacent to exactly two part numbers. The gear ratio is the product of these two numbers.

### Approach
1. **Identify Gears**: For each '*' symbol, check if it is adjacent to exactly two part numbers.
2. **Calculate Gear Ratios**: Calculate the gear ratio as the product of the two part numbers.
3. **Update Total Product**: Update the total product of gear ratios.
4. **Print Result**: Print the total product of gear ratios.

### Code Explanation
- The code includes additional logic to identify gears and calculate gear ratios.
- It updates the total product of gear ratios based on the identified gears.
- The result is printed for both parts.

