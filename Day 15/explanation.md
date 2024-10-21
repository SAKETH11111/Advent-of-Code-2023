# Day 15 Explanation

## Part 1

### Problem Description
The task is to process a list of commands to calculate a sum based on a custom hash algorithm. Each command is a string, and the hash algorithm processes each character in the string to produce a hash value. The goal is to sum the hash values of all commands.

### Approach
1. **Read Input File**: Read the input file and split it into a list of commands.
2. **Hash Algorithm**: Implement a custom hash algorithm that processes each character in a string to produce a hash value.
3. **Calculate Sum**: Iterate through the list of commands, apply the hash algorithm to each command, and calculate the sum of the hash values.
4. **Print Result**: Print the calculated sum.

### Code Explanation
- The code reads the input file and splits it into a list of commands.
- It defines a custom hash algorithm that processes each character in a string to produce a hash value.
- The code iterates through the list of commands, applies the hash algorithm to each command, and calculates the sum of the hash values.
- The result is printed.

## Part 2

### Problem Description
In addition to calculating the sum of hash values, the task involves processing commands to update a data structure called `BOX`. The `BOX` data structure is an array of lists, and each command can either add or remove entries from the lists.

### Approach
1. **Initialize BOX**: Initialize the `BOX` data structure as an array of 256 empty lists.
2. **Process Commands**: Iterate through the list of commands and process each command to update the `BOX` data structure.
   - **Remove Command**: If a command ends with '-', remove the corresponding entry from the `BOX`.
   - **Update Command**: If a command ends with '=', update the corresponding entry in the `BOX`.
3. **Calculate Sum**: Iterate through the `BOX` data structure and calculate the sum based on the entries in the lists.
4. **Print Result**: Print the calculated sum.

### Code Explanation
- The code initializes the `BOX` data structure as an array of 256 empty lists.
- It iterates through the list of commands and processes each command to update the `BOX` data structure.
- The code handles two types of commands: remove commands (ending with '-') and update commands (ending with '=').
- It calculates the sum based on the entries in the `BOX` data structure and prints the result.

