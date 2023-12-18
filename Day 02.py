from collections import defaultdict

# Read input file, strip extra whitespaces, and split into lines
input_data = open(0).read().strip()

# Initialize variables for part 1 and part 2
total_part1 = 0
total_part2 = 0

# Process each line in the input
for line in input_data.split('\n'):
    is_valid = True

    # Extract id and event details from the line
    identifier, events = line.split(':')

    # Initialize a defaultdict to store the maximum number of each color
    max_counts = defaultdict(int)

    # Process each event in the line
    for event in events.split(';'):
        # Process each set of balls in the event
        for balls in event.split(','):
            count, color = balls.split()
            count = int(count)

            # Update the maximum count for the current color
            max_counts[color] = max(max_counts[color], count)

            # Check if the count exceeds the allowed maximum
            if count > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                is_valid = False

    # Calculate the score for part 2
    score_part2 = 1
    for value in max_counts.values():
        score_part2 *= value

    # Update total for part 2
    total_part2 += score_part2

    # Update total for part 1 if the line is valid
    if is_valid:
        total_part1 += int(identifier.split()[-1])

# Print the results
print("--- Part 1 ---")
print(total_part1)
print("--- Part 2 ---")
print(total_part2)
