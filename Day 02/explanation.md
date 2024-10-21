# Day 02 Explanation

## Part 1

### Problem Description
The task is to process an input file to calculate two totals based on specific rules. The input file contains lines with a mix of characters and digits. The goal is to extract digits and calculate totals for part 1 and part 2.

### Approach
1. **Read Input File**: Read the input file, strip extra whitespaces, and split it into lines.
2. **Initialize Variables**: Initialize variables for part 1 and part 2.
3. **Process Each Line**: Iterate through each line in the input.
   - **Extract Digits**: For each character in the line, check if it is a digit and extract it.
   - **Check for Word Representation**: Check if the character sequence matches the word representation of a digit (e.g., "one", "two", etc.).
4. **Calculate Totals**: Calculate and update totals for part 1 and part 2.
5. **Print Results**: Print the results for part 1 and part 2.

### Code Explanation
- The code reads the input file and processes each line to extract digits.
- It checks for both numeric digits and word representations of digits.
- The totals for part 1 and part 2 are calculated based on the extracted digits.
- The results are printed for both parts.

## Part 2

### Problem Description
In addition to the numeric digits, the input file may contain word representations of digits (e.g., "one", "two", etc.). The task is to handle these word representations and calculate the totals accordingly.

### Approach
1. **Check for Word Representation**: For each character in the line, check if the character sequence matches the word representation of a digit.
2. **Update Totals**: Update the totals for part 1 and part 2 based on the extracted digits and word representations.

### Code Explanation
- The code includes additional logic to check for word representations of digits.
- It updates the totals for part 1 and part 2 based on the extracted digits and word representations.
- The results are printed for both parts.

