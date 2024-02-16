#!/usr/bin/env python3

import itertools
import sys

def generate_combinations(length):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return [''.join(combination) for combination in itertools.product(characters, repeat=length)]

def write_combinations_to_file(filename, combinations):
    with open(filename, 'w') as file:
        file.write('\n'.join(combinations) + '\n')

def main():
    # Check if the number of command line arguments is exactly 1
    if len(sys.argv) != 2:
        print("Usage: {} <number>".format(sys.argv[0]))
        sys.exit(1)

    # Get the number from the command line argument
    number = int(sys.argv[1])

    # Check if the number is within the valid range (2 to 32)
    if 2 <= number <= 32:
        print("Valid number:", number)

        # Create a file with the specified number and generate combinations
        filename = "{}.txt".format(number)
        chunk_size = 100000  # Adjust the chunk size based on system resources

        for len_combination in range(1, number + 1):
            combinations = generate_combinations(len_combination)
            write_combinations_to_file(filename, combinations)
            print("Combinations of length {} have been generated and written to {}".format(len_combination, filename))

        print("Total combinations generated:", len(combinations) * (number // chunk_size + 1))

    else:
        print("Invalid number! Please enter a number between 2 and 32.")
        sys.exit(1)

if __name__ == "__main__":
    main()
