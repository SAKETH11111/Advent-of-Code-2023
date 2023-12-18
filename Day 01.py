# Read input file, strip extra whitespaces, and split into lines
input_data = open('input.txt').read().strip()

# Initialize variables for part 1 and part 2
total_part1 = 0
total_part2 = 0

# Process each line in the input
for line in input_data.split('\n'):
    p1_digits = []
    p2_digits = []

    # Process each character in the line
    for i, character in enumerate(line):
        # Check if the character is a digit
        if character.isdigit():
            p1_digits.append(character)
            p2_digits.append(character)

        # Check if the character sequence matches the word representation of a digit
        for digit, word in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(word):
                p2_digits.append(str(digit + 1))

    # Calculate and update totals for part 1 and part 2
    total_part1 += int(p1_digits[0] + p1_digits[-1])
    total_part2 += int(p2_digits[0] + p2_digits[-1])

# Print the results
print("---Part 1---")
print(total_part1)
print("---Part 2---")
print(total_part2)
