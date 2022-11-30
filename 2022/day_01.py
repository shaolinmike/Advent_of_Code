"""
--- Day 1: ---

--- Part Two ---


"""


test_data = []


if __name__ == "__main__":
    input = r"D:\Projects\Advent_of_Code\2021\day_01_input.txt"

    raw_data = []

    with open(input, "r") as input_file:
        raw_data = [int(num) for num in input_file.read().split()]