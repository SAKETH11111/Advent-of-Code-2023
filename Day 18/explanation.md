# Day 18 Explanation

## Part 1

### Problem Description
The task is to navigate a grid and form a shape by following instructions. The shape is formed by connecting points on the grid based on the given directions and distances.

### Approach
1. **Read Input File**: Read the input file and split it into lines.
2. **Parse Instructions**: Parse each line to extract the direction and distance.
3. **Calculate Area**: Use Pick's theorem to calculate the area of the shape formed by the instructions.
4. **Calculate Perimeter**: Calculate the perimeter of the shape by summing up the distances in the instructions.
5. **Calculate Result**: Calculate the final result using the formula: area + (perimeter // 2) + 1.

### Code Explanation
- The code reads the input file and parses each line to extract the direction and distance.
- It calculates the area using Pick's theorem and the perimeter by summing up the distances.
- The final result is calculated using the formula: area + (perimeter // 2) + 1.

## Part 2

### Problem Description
In addition to the constraints in Part 1, the instructions are encoded in hexadecimal format. The task is to decode the instructions and calculate the area and perimeter accordingly.

### Approach
1. **Decode Instructions**: Decode the instructions from hexadecimal format to extract the direction and distance.
2. **Calculate Area**: Use Pick's theorem to calculate the area of the shape formed by the decoded instructions.
3. **Calculate Perimeter**: Calculate the perimeter of the shape by summing up the distances in the decoded instructions.
4. **Calculate Result**: Calculate the final result using the formula: area + (perimeter // 2) + 1.

### Code Explanation
- The code includes additional logic to decode the instructions from hexadecimal format.
- It calculates the area using Pick's theorem and the perimeter by summing up the distances.
- The final result is calculated using the formula: area + (perimeter // 2) + 1.

