from collections import defaultdict

# Read input file, strip extra whitespaces, and split into lines
input_data = open('0').read().strip()
lines = input_data.split('\n')

# Initialize variables
total_points = 0
accumulated_counts = defaultdict(int)

# Process each line in the input
for i, line in enumerate(lines):
    # Update the count for the current line index
    accumulated_counts[i] += 1

    # Split the line into the first part and the rest
    first_part, rest = line.split('|')

    # Extract id and card numbers from the first part
    identifier, card_part = first_part.split(':')
    card_numbers = [int(x) for x in card_part.split()]

    # Extract numbers from the rest part
    rest_numbers = [int(x) for x in rest.split()]

    # Calculate the common values between card and rest
    common_values = len(set(card_numbers) & set(rest_numbers))

    # Update total points based on common values
    if common_values > 0:
        total_points += 2**(common_values - 1)

    # Update counts for subsequent lines
    for j in range(common_values):
        accumulated_counts[i + 1 + j] += accumulated_counts[i]

# Print the results
print('---Part 1---')
print(total_points)
print("--Part 2---")
print(sum(accumulated_counts.values()))
