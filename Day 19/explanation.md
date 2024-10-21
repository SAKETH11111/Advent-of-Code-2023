# Day 19 Explanation

## Part 1

### Problem Description
The task is to determine if a part is accepted based on a set of rules. Each part has attributes (x, m, a, s) and the rules specify conditions for these attributes. The goal is to sum the values of accepted parts.

### Approach
1. **Read Input File**: Read the input file and split it into lines.
2. **Parse Rules**: Parse the rules into a dictionary where the key is the state and the value is the rule.
3. **Check Acceptance**: For each part, check if it is accepted based on the rules.
4. **Sum Values**: Sum the values of accepted parts.

### Code Explanation
- The code reads the input file and splits it into lines.
- It parses the rules into a dictionary.
- It defines a function `accepted` to check if a part is accepted based on the rules.
- It iterates over the parts and sums the values of accepted parts.
- The result is printed.

## Part 2

### Problem Description
In addition to checking acceptance, the task is to calculate the sum of accepted parts using a breadth-first search approach.

### Approach
1. **New Range Calculation**: Define a function to calculate the new range for a variable based on a comparison operation.
2. **Breadth-First Search**: Use a deque for breadth-first search to calculate the sum of accepted parts.
3. **Sum Values**: Sum the values of accepted parts based on the new ranges.

### Code Explanation
- The code defines a function `new_range` to calculate the new range for a variable.
- It uses a deque for breadth-first search to calculate the sum of accepted parts.
- The result is printed.
