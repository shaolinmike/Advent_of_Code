#! python3.11
"""
--- Day 13: Point of Incidence ---
With your help, the hot springs team locates an appropriate spring which
launches you neatly and precisely up to the edge of Lava Island.

There's just one problem: you don't see any lava.

You do see a lot of ash and igneous rock; there are even what look like
gray mountains scattered around. After a while, you make your way to a
nearby cluster of mountains only to discover that the valley between them
is completely full of large mirrors. Most of the mirrors seem to be aligned
in a consistent way; perhaps you should head in that direction?

As you move through the valley of mirrors, you find that several of them
have fallen from the large metal frames keeping them in place. The mirrors
are extremely flat and shiny, and many of the fallen mirrors have lodged
into the ash at strange angles. Because the terrain is all one color, it's
hard to tell where it's safe to walk or where you're about to run into a
mirror.

You note down the patterns of ash (.) and rocks (#) that you see as you
walk (your puzzle input); perhaps by carefully analyzing these patterns,
you can figure out where the mirrors are!

For example:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

To find the reflection in each pattern, you need to find a perfect
reflection across either a horizontal line between two rows or across a
vertical line between two columns.

In the first pattern, the reflection is across a vertical line between two
columns; arrows on each of the two columns point at the line between the
columns:

123456789
    ><
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><
123456789

In this pattern, the line of reflection is the vertical line between
columns 5 and 6. Because the vertical line is not perfectly in the middle
of the pattern, part of the pattern (column 1) has nowhere to reflect onto
and can be ignored; every other column has a reflected column within the
pattern and must match exactly: column 2 matches column 9, column 3 matches
8, 4 matches 7, and 5 matches 6.

The second pattern reflects across a horizontal line instead:

1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7

This pattern reflects across the horizontal line between rows 4 and 5. Row
1 would reflect with a hypothetical row 8, but since that's not in the
pattern, row 1 doesn't need to match anything. The remaining rows match:
row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.

To summarize your pattern notes, add up the number of columns to the left
of each vertical line of reflection; to that, also add 100 multiplied by
the number of rows above each horizontal line of reflection. In the above
example, the first pattern's vertical line has 5 columns to its left and
the second pattern's horizontal line has 4 rows above it, a total of 405.

Find the line of reflection in each of the patterns in your notes. What
number do you get after summarizing all of your notes?

Your puzzle answer was 33735.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You resume walking through the valley of mirrors and - SMACK! - run
directly into one. Hopefully nobody was watching, because that must have
been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one
smudge: exactly one . or # should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a
different reflection line to be valid. (The old reflection line won't
necessarily continue being valid after the smudge is fixed.)

Here's the above example again:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

The first pattern's smudge is in the top-left corner. If the top-left #
were instead ., it would have a different, horizontal line of reflection:

1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7

With the smudge in the top-left corner repaired, a new horizontal line of
reflection between rows 3 and 4 now exists. Row 7 has no corresponding
reflected row and can be ignored, but every other row matches exactly: row
1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth symbol
on row 2 from . to #:

1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7

Now, the pattern has a different horizontal line of reflection between rows
1 and 2.

Summarize your notes as before, but instead use the new different
reflection lines. In this example, the first pattern's new horizontal line
has 3 rows above it and the second pattern's new horizontal line has 1 row
above it, summarizing to the value 400.

In each pattern, fix the smudge and find the different line of reflection.
What number do you get after summarizing the new reflection line in each
pattern in your notes?
"""

import difflib

TEST_DATA = [ '#.##..##.',
              '..#.##.#.',
              '##......#',
              '##......#',
              '..#.##.#.',
              '..##..##.',
              '#.#.##.#.',
              '',
              '#...##..#',
              '#....#..#',
              '..##..###',
              '#####.##.',
              '#####.##.',
              '..##..###',
              '#....#..#',
            ]

DEBUG = False


def _diff_reflection(a, b):
    diff_idx = -1
    diff_val = None

    # diffs = [x for x in difflib.ndiff(''.join(a), ''.join(b))]
    diff_ratio = difflib.SequenceMatcher(None, ''.join(a), ''.join(b)).ratio()
    if 0.857 < diff_ratio < 1.0:
        for idx, val in enumerate(difflib.ndiff(a, b)):
            diff_idx = idx
            diff_val = val

    return diff_idx, diff_val


def _find_smudge(mirror_data, mirror_axis, axis=0):
    is_smudged = False

    a_side = mirror_axis - 1
    b_side = mirror_axis
    while is_smudged:
        if axis == 0:
            if a_side < 0 or b_side >= len(mirror_data[0]):
                diff_idx, diff_val = _diff_reflection(left_col, right_col)
                if diff_idx != -1:
                    left_col[diff_idx] = diff_val
                return is_smudged

            left_col = [row[a_side] for row in mirror_data]
            right_col = [row[b_side] for row in mirror_data]

            if left_col != right_col:
                is_smudged = False
                # Check for the smudge and fix it
                # diff_idx, diff_val = _diff_reflection(left_col, right_col)
                # if diff_idx != -1:
                    # left_col[diff_idx] = diff_val
                # diff_ratio = difflib.SequenceMatcher(None, ''.join(left_col), ''.join(right_col)).ratio()
                # if 0.857 < diff_ratio < 1.0:
                    # for idx, val in enumerate(difflib.ndiff(left_col, right_col)):
                        # if '-' in val or '+' in val:
                            # print(f'{idx} : {val}')
                            # left_col[idx] = val.split()[1]

        else:
            if a_side < 0 or b_side > len(mirror_data) - 1:
                diff_idx, diff_val = _diff_reflection(mirror_data[a_side], mirror_data[b_side])
                if diff_idx != -1:
                    left_col[diff_idx] = diff_val
                return is_smudged

            if ''.join(mirror_data[a_side]) != ''.join(mirror_data[b_side]):
                is_smudged = False
                diff_idx, diff_val = _diff_reflection(mirror_data[a_side], mirror_data[b_side])
                if diff_idx != -1:
                    left_col[diff_idx] = diff_val

        a_side -= 1
        b_side += 1

    return is_smudged


def desmudge_mirror(data):
    polished_mirrors = []

    for idx, mirror in enumerate(data):
        mirror_axis_x = -1
        mirror_axis_y = -1

        # Check x-axis
        for idx in range(0, len(mirror[0]) - 1):
            # Build Column data
            col_data_1 = [row[idx] for row in mirror]
            col_data_2 = [row[idx + 1] for row in mirror]

            if col_data_1 == col_data_2:
                result = _find_smudge(mirror, idx + 1, axis = 0)
                if result:
                    # Fix the smudge
                    mirror_axis_x = idx + 1
                    break
            else:
                diff_idx, diff_val = _diff_reflection(col_data_1, col_data_2)
                if diff_idx != -1:
                    col_data_1[diff_idx] = diff_val

        # Check y-axis
        for idx in range(0, len(mirror) - 1):
            if ''.join(mirror[idx]) == ''.join(mirror[idx + 1]):
                result = _find_smudge(mirror, idx + 1, axis = 1)
                if result:
                    # Fix the smudge
                    mirror_axis_y = idx + 1
                    break
            else:
                diff_idx, diff_val = _diff_reflection(mirror[idx], mirror[idx + 1])
                if diff_idx != -1:
                    mirror[diff_idx] = diff_val

        # return mirror_axis_x, mirror_axis_y

    return polished_mirrors


def find_reflection(mirror):
    mirror_axis_x = -1
    mirror_axis_y = -1

    # Check x-axis
    for idx in range(0, len(mirror[0]) - 1):
        # Build Column data
        col_data_1 = [row[idx] for row in mirror]
        col_data_2 = [row[idx + 1] for row in mirror]

        if col_data_1 == col_data_2:
            result = verify_reflection(mirror, idx + 1, axis = 0)
            if result:
                mirror_axis_x = idx + 1
                break

    # Check y-axis
    for idx in range(0, len(mirror) - 1):
        if ''.join(mirror[idx]) == ''.join(mirror[idx + 1]):
            result = verify_reflection(mirror, idx + 1, axis = 1)
            if result:
                mirror_axis_y = idx + 1
                break

    return mirror_axis_x, mirror_axis_y


def find_reflection_values(data):
    result = 0
    x_results = []
    y_results = []

    for idx, mirror in enumerate(data):
        x_axis, y_axis = find_reflection(mirror)
        if x_axis > 0:
            x_results.append(x_axis)
            if DEBUG: print(f'{idx:02} {x_axis} : {x_axis}')
        if  y_axis > 0:
            y_results.append(y_axis)
            if DEBUG: print(f'{idx:02} {y_axis} : {y_axis * 100}')
        if DEBUG: [print(f"\t\t\t{''.join(x)}") for x in mirror]
    result = sum(x_results) + (100 * sum(y_results))

    return result


def verify_reflection(mirror_data, mirror_axis, axis=0):
    is_reflection = True

    a_side = mirror_axis - 1
    b_side = mirror_axis
    while is_reflection:
        if axis == 0:
            if a_side < 0 or b_side >= len(mirror_data[0]):
                return is_reflection

            left_col = [row[a_side] for row in mirror_data]
            right_col = [row[b_side] for row in mirror_data]

            if left_col != right_col:
                is_reflection = False

        else:
            if a_side < 0 or b_side > len(mirror_data) - 1:
                return is_reflection

            if ''.join(mirror_data[a_side]) != ''.join(mirror_data[b_side]):
                is_reflection = False

        a_side -= 1
        b_side += 1

    return is_reflection


def parse_data(raw_data):
    data = []
    mirror = []

    for datum in raw_data:
        if datum != '':
            mirror.append([x for x in datum])
        else:
            data.append(mirror)
            mirror = []

    if mirror:
        data.append(mirror)

    return data


def main(raw_data, part_two = False):
    result = 0
    data = parse_data(raw_data)

    if part_two:
        data = desmudge_mirror(data)

    result = find_reflection_values(data)
    print(f'\nThe numbers of all the summarized notes is {result}')



if __name__ == "__main__":
    input = r"D:\Projects\Advent_of_Code\2023\day_13_input.txt"
    raw_data = []

    with open(input, "r") as input_file:
        raw_data = [line.strip() for line in input_file.readlines( )]

    # main(TEST_DATA)
    # main(raw_data)
    main(TEST_DATA, part_two = True)
    # main(raw_data, part_two = True)