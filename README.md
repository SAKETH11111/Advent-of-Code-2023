# Day 1
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to recover calibration values from a document.
   - Understand that calibration values are formed by combining the first and last digits of each line.

2. **Analyzing Document:**
   - Examine the document structure and the format of calibration values.
   - Notice that each line contains a mix of characters and digits.

3. **Digit Extraction:**
   - Plan a strategy to extract the first and last digits from each line.
   - Consider how to identify digits among characters.

4. **Sum Calculation:**
   - Understand that the task involves summing up all calibration values.
   - Plan a mechanism to calculate the sum.

### Part 2:

1. **Identifying Spelled Digits:**
   - Recognize that some digits are spelled out with letters.
   - Identify the words corresponding to each digit.

2. **Expanding Digit Extraction:**
   - Modify the digit extraction strategy to account for spelled-out digits.
   - Consider adding logic to identify and convert spelled-out digits.

3. **Sum Recalculation:**
   - Understand that the sum calculation needs to be adapted for the modified digit extraction.
   - Consider how the new digit extraction affects the overall sum.

# Day 2:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to identify games where the given set of cubes is sufficient.
   - Understand that each game has subsets of cubes revealed.

2. **Analyzing Game Records:**
   - Look at the example records of games to understand the format.
   - Realize that the Elf wants to know which games are possible with a specific cube configuration.

3. **Parsing Game Information:**
   - Plan a way to parse the game records, extracting relevant information.
   - Understand how the number of cubes in each subset affects game possibility.

4. **Checking Possibility:**
   - Consider a mechanism to check if a game is possible with the given cube configuration.
   - Note that if the Elf reveals more cubes than the specified limit, the game is impossible.

5. **Accumulating Game IDs:**
   - Plan to accumulate the IDs of possible games.
   - Understand that IDs are associated with each game.

6. **Scoring Mechanism:**
   - Understand the scoring mechanism for calculating the sum of game IDs.

### Part 2:

1. **Understanding Minimum Set:**
   - Recognize that the goal is to find the minimum set of cubes needed for each game.
   - Understand the concept of the power of a set.

2. **Analyzing Game Records (Part 2):**
   - Consider the example games to understand how the minimum set is determined.
   - Realize that the minimum set is associated with the power of that set.

3. **Parsing Game Information (Part 2):**
   - Plan a way to parse the game records for determining the minimum set.
   - Understand the structure of the records and how cubes are specified.

4. **Calculating Power of Sets:**
   - Understand the concept of the power of a set (product of cube counts).
   - Consider a mechanism to calculate and accumulate the power of minimum sets.

5. **Accumulating Scores:**
   - Plan to accumulate the scores associated with the power of minimum sets.
   - Understand that the final answer is the sum of these scores.

# Day 3: 
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the sum of numbers connected to symbols in an engine schematic.
   - Understand that numbers adjacent to symbols (except '.') are part numbers.

2. **Analyzing the Schematic:**
   - Consider the structure of the engine schematic, noticing symbols, numbers, and their relationships.
   - Realize that part numbers are connected horizontally, vertically, and diagonally to symbols.

3. **Iterative Processing:**
   - Plan a way to go through each cell in the schematic.
   - Understand the need to sum all part numbers adjacent to symbols.

4. **Handling Part Numbers:**
   - Consider a mechanism to accumulate the sum of part numbers.
   - Notice that numbers not adjacent to symbols should be excluded.

5. **Symbol Recognition:**
   - Devise a strategy to identify symbols ('*') and their adjacent part numbers.

6. **Data Storage:**
   - Think about storing information efficiently, possibly using a grid structure.

### Part 2:

1. **Understanding Gear Ratios:**
   - Realize that gears are '*' symbols adjacent to exactly two part numbers.
   - Recognize that the gear ratio is the product of these two numbers.

2. **Identifying Gears:**
   - Plan how to identify gears by locating symbols adjacent to exactly two part numbers.

3. **Calculating Gear Ratios:**
   - Consider a mechanism to calculate and accumulate gear ratios.

4. **Iterative Processing (Part 2):**
   - Extend the iterative process to handle gears and their ratios.

5. **Data Storage (Part 2):**
   - Use appropriate data structures to store gear information efficiently.

# Day 4: 
### Part 1:

1. **Understanding the Problem:**
   - Recognize that the problem involves scratchcards with two sets of numbers, and the goal is to find matches between them.
   - Understand that points are awarded for each match, with doubling points for subsequent matches.

2. **Parsing the Input:**
   - Identify the structure of the input, where each line represents a scratchcard with winning and owned numbers.

3. **Organizing Data:**
   - Consider creating a data structure to store the scratchcards, possibly a list of lists or tuples to represent each card.

4. **Matching Numbers:**
   - Devise a method to find common numbers between the winning and owned sets on each scratchcard.
   - Understand that points are awarded based on the number of matches.

5. **Calculating Points:**
   - Implement a mechanism to calculate points for each scratchcard.
   - Realize that the points are calculated based on the number of matches, with doubling for subsequent matches.

6. **Accumulating Total Points:**
   - Develop a way to accumulate the total points as scratchcards are processed.

7. **Final Output:**
   - Print or store the total points obtained from all the scratchcards.

### Part 2:

1. **Reassessing Rules:**
   - Understand that Part 2 introduces a change in rules where winning scratchcards can yield more scratchcards.
   - Realize that each winning scratchcard produces copies of subsequent scratchcards.

2. **Handling Copies:**
   - Consider how to manage the generation of copies for each winning scratchcard.
   - Understand that the process continues until no more scratchcards are won.

3. **Iteration through Scratchcards:**
   - Plan how to iteratively process both the original scratchcards and their copies.
   - Realize that this process repeats until no more scratchcards are won.

4. **Accumulating Total Scratchcards:**
   - Develop a mechanism to keep track of the total number of scratchcards obtained, including both originals and copies.

5. **Final Output (Part 2):**
   - Print or store the total number of scratchcards obtained after processing all originals and copies.


# Day 5:
### Part 1:

1. **Input Understanding:**
   - Recognize that the input describes a gardening problem where seeds need to be planted, and there are mappings between different gardening categories.

2. **Seed Extraction:**
   - Identify the "seeds:" line in the input as the starting point for the seeds that need to be planted.
   - Extract the seed numbers from this line.

3. **Function Mapping:**
   - Acknowledge that there are mappings provided for converting numbers between different gardening categories (seed to soil, soil to fertilizer, etc.).

4. **Function Application - Single Value:**
   - Understand that each mapping is defined as a range of source values and a corresponding range of destination values.
   - Apply these mappings iteratively to each seed value to find the final location category.

5. **Find Minimum Location:**
   - After applying all mappings, find the minimum location number among the converted seed values.
   - This minimum value represents the lowest location number.

### Part 2:

1. **Input Modification:**
   - Notice that in Part 2, the "seeds:" line describes ranges of seed numbers rather than individual seeds.

2. **Seed Range Extraction:**
   - Recognize the pairs in the "seeds:" line as indicating the start and length of seed ranges.
   - Extract these seed ranges.

3. **Function Mapping (Same as Part 1):**
   - Continue to use the mappings provided for converting numbers between different gardening categories.

4. **Function Application - Range:**
   - Apply the mappings to each seed range, considering the start and length of each range.
   - Obtain a list of converted seed values.

5. **Find Minimum Location (Same as Part 1):**
   - Determine the minimum value in the list of converted seed values.
   - This minimum value corresponds to the lowest location number.

6. **Result Comparison:**
   - Realize that the solution for Part 2 involves a broader consideration of seed ranges but follows a similar process to Part 1.

# Day 6:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the number of valid time-distance pairs.
   - Understand that the input consists of time and distance values.

2. **Parsing the Input:**
   - Identify the structure of the input, where time and distance values are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the time and distance values.
   - Understand the need to calculate valid pairs based on the given conditions.

4. **Handling Time-Distance Pairs:**
   - Consider a mechanism to calculate the number of valid pairs.
   - Notice that the conditions for validity are based on the product of time and distance.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the number of valid time-distance pairs for a combined value.
   - Understand that the input consists of combined time and distance values.

2. **Parsing the Input:**
   - Identify the structure of the input, where combined time and distance values are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the combined time and distance values.
   - Understand the need to calculate valid pairs based on the given conditions.

4. **Handling Combined Time-Distance Pairs:**
   - Consider a mechanism to calculate the number of valid pairs.
   - Notice that the conditions for validity are based on the product of combined time and distance.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 7:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the strength of poker hands.
   - Understand that the input consists of poker hands and bids.

2. **Parsing the Input:**
   - Identify the structure of the input, where poker hands and bids are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the poker hands and bids.
   - Understand the need to calculate the strength of each hand based on the given conditions.

4. **Handling Poker Hands:**
   - Consider a mechanism to calculate the strength of each hand.
   - Notice that the conditions for strength are based on the ranks and suits of the cards.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the strength of poker hands with additional rules.
   - Understand that the input consists of poker hands and bids.

2. **Parsing the Input:**
   - Identify the structure of the input, where poker hands and bids are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the poker hands and bids.
   - Understand the need to calculate the strength of each hand based on the given conditions.

4. **Handling Poker Hands:**
   - Consider a mechanism to calculate the strength of each hand.
   - Notice that the conditions for strength are based on the ranks and suits of the cards.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 8:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the least common multiple (LCM) of a set of numbers.
   - Understand that the input consists of steps and rules.

2. **Parsing the Input:**
   - Identify the structure of the input, where steps and rules are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the steps and rules.
   - Understand the need to calculate the LCM based on the given conditions.

4. **Handling Steps and Rules:**
   - Consider a mechanism to calculate the LCM.
   - Notice that the conditions for LCM are based on the steps and rules.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the least common multiple (LCM) of a set of numbers with additional rules.
   - Understand that the input consists of steps and rules.

2. **Parsing the Input:**
   - Identify the structure of the input, where steps and rules are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the steps and rules.
   - Understand the need to calculate the LCM based on the given conditions.

4. **Handling Steps and Rules:**
   - Consider a mechanism to calculate the LCM.
   - Notice that the conditions for LCM are based on the steps and rules.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 9:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to extrapolate the next value in a sequence.
   - Understand that the input consists of sequences of integers.

2. **Parsing the Input:**
   - Identify the structure of the input, where sequences of integers are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the sequences.
   - Understand the need to extrapolate the next value based on the given conditions.

4. **Handling Sequences:**
   - Consider a mechanism to extrapolate the next value in each sequence.
   - Notice that the conditions for extrapolation are based on the differences between consecutive elements.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to extrapolate the next value in a sequence in reverse order.
   - Understand that the input consists of sequences of integers.

2. **Parsing the Input:**
   - Identify the structure of the input, where sequences of integers are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the sequences.
   - Understand the need to extrapolate the next value based on the given conditions.

4. **Handling Sequences:**
   - Consider a mechanism to extrapolate the next value in each sequence.
   - Notice that the conditions for extrapolation are based on the differences between consecutive elements.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 10:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the length of the path marked by "S" on the grid.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the path based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the path on the grid.
   - Notice that the conditions for finding the path are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of tiles inside the path.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of tiles inside the path based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of tiles inside the path.
   - Notice that the conditions for finding the tiles are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 11:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of empty rows and columns in the grid.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of empty rows and columns based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of empty rows and columns.
   - Notice that the conditions for finding the empty rows and columns are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of empty rows and columns in the grid with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of empty rows and columns based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of empty rows and columns.
   - Notice that the conditions for finding the empty rows and columns are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 12:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of valid dot-block pairs.
   - Understand that the input consists of dots and blocks.

2. **Parsing the Input:**
   - Identify the structure of the input, where dots and blocks are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the dots and blocks.
   - Understand the need to find the number of valid pairs based on the given conditions.

4. **Handling Dot-Block Pairs:**
   - Consider a mechanism to find the number of valid pairs.
   - Notice that the conditions for validity are based on the length of the blocks.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of valid dot-block pairs with additional rules.
   - Understand that the input consists of dots and blocks.

2. **Parsing the Input:**
   - Identify the structure of the input, where dots and blocks are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the dots and blocks.
   - Understand the need to find the number of valid pairs based on the given conditions.

4. **Handling Dot-Block Pairs:**
   - Consider a mechanism to find the number of valid pairs.
   - Notice that the conditions for validity are based on the length of the blocks.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 14:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the score of the grid.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to calculate the score based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to calculate the score of the grid.
   - Notice that the conditions for calculating the score are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the score of the grid with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to calculate the score based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to calculate the score of the grid.
   - Notice that the conditions for calculating the score are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 15:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the sum of hash values.
   - Understand that the input consists of commands.

2. **Parsing the Input:**
   - Identify the structure of the input, where commands are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the commands.
   - Understand the need to calculate the sum of hash values based on the given conditions.

4. **Handling Commands:**
   - Consider a mechanism to calculate the sum of hash values.
   - Notice that the conditions for calculating the hash values are based on the commands.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the sum of hash values with additional rules.
   - Understand that the input consists of commands.

2. **Parsing the Input:**
   - Identify the structure of the input, where commands are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the commands.
   - Understand the need to calculate the sum of hash values based on the given conditions.

4. **Handling Commands:**
   - Consider a mechanism to calculate the sum of hash values.
   - Notice that the conditions for calculating the hash values are based on the commands.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 16:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the score of the grid.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to calculate the score based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to calculate the score of the grid.
   - Notice that the conditions for calculating the score are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the score of the grid with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to calculate the score based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to calculate the score of the grid.
   - Notice that the conditions for calculating the score are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 17:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the shortest path in the grid.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the shortest path based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the shortest path in the grid.
   - Notice that the conditions for finding the path are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the shortest path in the grid with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the shortest path based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the shortest path in the grid.
   - Notice that the conditions for finding the path are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 18:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the area of the shape.
   - Understand that the input consists of instructions.

2. **Parsing the Input:**
   - Identify the structure of the input, where instructions are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the instructions.
   - Understand the need to calculate the area based on the given conditions.

4. **Handling Instructions:**
   - Consider a mechanism to calculate the area of the shape.
   - Notice that the conditions for calculating the area are based on the instructions.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the area of the shape with additional rules.
   - Understand that the input consists of instructions.

2. **Parsing the Input:**
   - Identify the structure of the input, where instructions are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the instructions.
   - Understand the need to calculate the area based on the given conditions.

4. **Handling Instructions:**
   - Consider a mechanism to calculate the area of the shape.
   - Notice that the conditions for calculating the area are based on the instructions.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 19:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to identify accepted parts based on rules.
   - Understand that the input consists of rules and parts.

2. **Parsing the Input:**
   - Identify the structure of the input, where rules and parts are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the rules and parts.
   - Understand the need to identify accepted parts based on the given conditions.

4. **Handling Rules and Parts:**
   - Consider a mechanism to identify accepted parts.
   - Notice that the conditions for acceptance are based on the rules.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to identify accepted parts based on rules with additional conditions.
   - Understand that the input consists of rules and parts.

2. **Parsing the Input:**
   - Identify the structure of the input, where rules and parts are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the rules and parts.
   - Understand the need to identify accepted parts based on the given conditions.

4. **Handling Rules and Parts:**
   - Consider a mechanism to identify accepted parts.
   - Notice that the conditions for acceptance are based on the rules.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 20:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the least common multiple (LCM) of a set of numbers.
   - Understand that the input consists of rules.

2. **Parsing the Input:**
   - Identify the structure of the input, where rules are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the rules.
   - Understand the need to calculate the LCM based on the given conditions.

4. **Handling Rules:**
   - Consider a mechanism to calculate the LCM.
   - Notice that the conditions for LCM are based on the rules.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to calculate the least common multiple (LCM) of a set of numbers with additional rules.
   - Understand that the input consists of rules.

2. **Parsing the Input:**
   - Identify the structure of the input, where rules are provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the rules.
   - Understand the need to calculate the LCM based on the given conditions.

4. **Handling Rules:**
   - Consider a mechanism to calculate the LCM.
   - Notice that the conditions for LCM are based on the rules.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 21:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of ways to get a copy of a point in a given number of steps.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of ways to get a copy of a point based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of ways to get a copy of a point in the grid.
   - Notice that the conditions for finding the ways are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of ways to get a copy of a point in a given number of steps with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of ways to get a copy of a point based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of ways to get a copy of a point in the grid.
   - Notice that the conditions for finding the ways are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 22:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of bricks that would not move.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of bricks that would not move based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of bricks that would not move in the grid.
   - Notice that the conditions for finding the bricks are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of bricks that would not move with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of bricks that would not move based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of bricks that would not move in the grid.
   - Notice that the conditions for finding the bricks are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 23:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the shortest path in the grid.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the shortest path based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the shortest path in the grid.
   - Notice that the conditions for finding the path are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the shortest path in the grid with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the shortest path based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the shortest path in the grid.
   - Notice that the conditions for finding the path are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 24:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of intersections in the grid.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of intersections based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of intersections in the grid.
   - Notice that the conditions for finding the intersections are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of intersections in the grid with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of intersections based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of intersections in the grid.
   - Notice that the conditions for finding the intersections are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

# Day 25:
### Part 1:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of valid paths in the grid.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of valid paths based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of valid paths in the grid.
   - Notice that the conditions for finding the paths are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.

### Part 2:

1. **Understanding the Task:**
   - Recognize that the goal is to find the number of valid paths in the grid with additional rules.
   - Understand that the input consists of a grid of characters.

2. **Parsing the Input:**
   - Identify the structure of the input, where the grid of characters is provided.

3. **Iterative Processing:**
   - Plan a way to iterate through the grid.
   - Understand the need to find the number of valid paths based on the given conditions.

4. **Handling the Grid:**
   - Consider a mechanism to find the number of valid paths in the grid.
   - Notice that the conditions for finding the paths are based on the characters in the grid.

5. **Data Storage:**
   - Think about storing information efficiently, possibly using lists or arrays.
