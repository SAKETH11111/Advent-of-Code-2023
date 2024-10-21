# Day 04 Explanation

## Part 1

### Problem Description
The task is to process an input file containing scratchcards with two sets of numbers. The goal is to find matches between the two sets and calculate points based on the number of matches. Points are awarded for each match, with doubling points for subsequent matches.

### Approach
1. **Read Input File**: Read the input file, strip extra whitespaces, and split it into lines.
2. **Initialize Variables**: Initialize variables to store total points and accumulated counts.
3. **Process Each Line**: Iterate through each line in the input.
   - **Update Count**: Update the count for the current line index.
   - **Split Line**: Split the line into the first part and the rest.
   - **Extract Numbers**: Extract id and card numbers from the first part, and extract numbers from the rest part.
   - **Calculate Common Values**: Calculate the common values between card and rest numbers.
   - **Update Points**: Update total points based on common values.
   - **Update Counts**: Update counts for subsequent lines based on common values.
4. **Print Results**: Print the total points.

### Code Explanation
- The code reads the input file and processes each line to extract numbers.
- It calculates the common values between card and rest numbers and updates the total points based on the number of matches.
- The results are printed for both parts.

## Part 2

### Problem Description
In addition to calculating points, the task is to handle winning scratchcards that yield more scratchcards. Each winning scratchcard produces copies of subsequent scratchcards.

### Approach
1. **Handle Copies**: Manage the generation of copies for each winning scratchcard.
2. **Iterate through Scratchcards**: Iteratively process both the original scratchcards and their copies.
3. **Update Counts**: Update counts for subsequent lines based on common values.
4. **Accumulate Total Scratchcards**: Keep track of the total number of scratchcards obtained, including both originals and copies.
5. **Print Results**: Print the total number of scratchcards obtained after processing all originals and copies.

### Code Explanation
- The code includes additional logic to handle winning scratchcards and generate copies.
- It updates the counts for subsequent lines based on common values and keeps track of the total number of scratchcards obtained.
- The results are printed for both parts.

